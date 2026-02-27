#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# audit_applications.sh — Syncrescendence Grand Unification Application Audit
# Inventories all apps, cross-references brew/mas, generates Brewfile + report.
set -uo pipefail

# ── Config ──
REPORT="/tmp/app_audit_report.md"
BREWFILE="/tmp/Brewfile"
BACKUP="/tmp/app_backup_$(date +%Y%m%d_%H%M%S).txt"

# ── Colors ──
G='\033[0;32m' Y='\033[0;33m' B='\033[0;34m' C='\033[0;36m'
R='\033[0;31m' M='\033[0;35m' D='\033[0;90m' N='\033[0m' BOLD='\033[1m'

echo -e "${B}${BOLD}═══ Syncrescendence Grand Unification — Application Audit ═══${N}"
echo ""

# ── Helper: normalize app name to cask-style ──
normalize() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//'
}

# ══════════════════════════════════════════════════════════════
# PHASE A: INVENTORY
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase A: Inventorying applications...${N}"

declare -a all_apps=()
declare -a all_apps_paths=()

# /Applications (top-level .app only, skip directories without .app)
while IFS= read -r -d '' app; do
    name=$(basename "$app" .app)
    all_apps+=("$name")
    all_apps_paths+=("$app")
done < <(find /Applications -maxdepth 1 -name "*.app" -print0 2>/dev/null | sort -z)

# ~/Applications (top-level .app only)
while IFS= read -r -d '' app; do
    name=$(basename "$app" .app)
    all_apps+=("$name")
    all_apps_paths+=("$app")
done < <(find ~/Applications -maxdepth 1 -name "*.app" -print0 2>/dev/null | sort -z)

echo -e "  Found ${BOLD}${#all_apps[@]}${N} applications"

# Save backup
printf '%s\n' "${all_apps_paths[@]}" > "$BACKUP"
echo -e "  Backup saved to ${D}${BACKUP}${N}"

# ══════════════════════════════════════════════════════════════
# PHASE B: BREW CASK CROSS-REFERENCE
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase B: Cross-referencing with Homebrew casks...${N}"

declare -A app_to_cask=()    # "Google Chrome" → "google-chrome"
declare -A cask_list=()      # All installed cask names

# Get all installed cask names
while read -r cask; do
    cask_list["$cask"]=1
done < <(brew list --cask -1 2>/dev/null)

# Get cask → app artifact mapping (batch query)
cask_args=$(brew list --cask -1 2>/dev/null | tr '\n' ' ')
if [[ -n "$cask_args" ]]; then
    while IFS='|' read -r cask app_artifact; do
        [[ -z "$cask" || -z "$app_artifact" ]] && continue
        # Handle paths like "AeroSpace-v0.20.2-Beta/AeroSpace.app"
        app_clean=$(basename "$app_artifact" .app)
        app_to_cask["$app_clean"]="$cask"
    done < <(brew info --json=v2 --cask $cask_args 2>/dev/null | \
        jq -r '.casks[] | "\(.token)|\(.artifacts[] | .app? // empty | .[]? // empty)"' 2>/dev/null | \
        grep -v '^$')
fi

echo -e "  ${BOLD}${#cask_list[@]}${N} Homebrew casks installed (${#app_to_cask[@]} with app artifacts)"

# ══════════════════════════════════════════════════════════════
# PHASE C: MAC APP STORE CROSS-REFERENCE
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase C: Cross-referencing with Mac App Store...${N}"

declare -A mas_id_by_name=()    # "Things" → "904280696"
declare -A mas_name_by_id=()

while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    mas_id=$(echo "$line" | awk '{print $1}')
    # Extract name: everything between ID and version in parens
    mas_name=$(echo "$line" | sed 's/^[0-9]* *//' | sed 's/ *([^)]*) *$//')
    mas_id_by_name["$mas_name"]="$mas_id"
    mas_name_by_id["$mas_id"]="$mas_name"
done < <(mas list 2>/dev/null)

echo -e "  ${BOLD}${#mas_id_by_name[@]}${N} App Store apps found"

# ══════════════════════════════════════════════════════════════
# PHASE D: CATEGORIZE EACH APP
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase D: Categorizing applications...${N}"

declare -a cat_brew_managed=()     # Already managed by brew cask
declare -a cat_appstore=()         # Installed via App Store
declare -a cat_candidates=()       # Could be adopted by brew
declare -a cat_setapp=()           # Setapp-managed
declare -a cat_system=()           # Apple system apps (skip)
declare -a cat_unmanaged=()        # Manual installs, no brew/mas match

# Known Apple system apps that ship with macOS or are Apple-only
declare -A apple_system_apps=(
    ["Safari"]=1 ["Finder"]=1 ["System Preferences"]=1 ["System Settings"]=1
    ["App Store"]=1 ["Automator"]=1 ["Calculator"]=1 ["Calendar"]=1
    ["Chess"]=1 ["Contacts"]=1 ["Dashboard"]=1 ["Dictionary"]=1
    ["FaceTime"]=1 ["Font Book"]=1 ["Home"]=1 ["Image Capture"]=1
    ["Launchpad"]=1 ["Mail"]=1 ["Maps"]=1 ["Messages"]=1
    ["Migration Assistant"]=1 ["Music"]=1 ["News"]=1 ["Notes"]=1
    ["Photo Booth"]=1 ["Photos"]=1 ["Podcasts"]=1 ["Preview"]=1
    ["QuickTime Player"]=1 ["Reminders"]=1 ["Shortcuts"]=1
    ["Siri"]=1 ["Stickies"]=1 ["Stocks"]=1 ["Time Machine"]=1
    ["TV"]=1 ["Voice Memos"]=1 ["Weather"]=1 ["Utilities"]=1
    ["AppleScript"]=1
)

# Detect Setapp: check if Setapp is installed and get managed apps
has_setapp=false
declare -A setapp_apps=()
if [[ -d "/Applications/Setapp" ]] || [[ -d "$HOME/Library/Application Support/Setapp" ]]; then
    has_setapp=true
    # Setapp stores receipts in its support directory
    while IFS= read -r receipt; do
        sapp=$(basename "$receipt" | sed 's/\..*$//')
        setapp_apps["$sapp"]=1
    done < <(find "$HOME/Library/Application Support/Setapp/Setapp" -name "*.plist" 2>/dev/null)
fi

search_count=0
for i in "${!all_apps[@]}"; do
    app="${all_apps[$i]}"
    app_path="${all_apps_paths[$i]}"

    # 1. Apple system app?
    if [[ -n "${apple_system_apps[$app]+x}" ]]; then
        cat_system+=("$app")
        continue
    fi

    # 2. Brew cask managed? (check artifact mapping)
    if [[ -n "${app_to_cask[$app]+x}" ]]; then
        cat_brew_managed+=("$app|${app_to_cask[$app]}")
        continue
    fi

    # 3. Mac App Store?
    if [[ -n "${mas_id_by_name[$app]+x}" ]]; then
        cat_appstore+=("$app|${mas_id_by_name[$app]}")
        continue
    fi

    # 3b. Fuzzy match App Store (strip trailing numbers, try variations)
    app_stripped=$(echo "$app" | sed 's/[0-9]*$//' | sed 's/ *$//')
    if [[ "$app_stripped" != "$app" ]] && [[ -n "${mas_id_by_name[$app_stripped]+x}" ]]; then
        cat_appstore+=("$app|${mas_id_by_name[$app_stripped]}")
        continue
    fi

    # 4. Setapp?
    if [[ "$has_setapp" == true ]]; then
        # Check if the app bundle has a Setapp receipt
        if [[ -f "$app_path/Contents/_MASReceipt/receipt" ]] && \
           strings "$app_path/Contents/_MASReceipt/receipt" 2>/dev/null | grep -qi "setapp"; then
            cat_setapp+=("$app")
            continue
        fi
        # Also check by name in Setapp receipts
        app_norm=$(normalize "$app")
        if [[ -n "${setapp_apps[$app]+x}" ]] || [[ -n "${setapp_apps[$app_norm]+x}" ]]; then
            cat_setapp+=("$app")
            continue
        fi
    fi

    # 5. Search for brew cask candidate
    normalized=$(normalize "$app")
    if [[ ${#normalized} -ge 2 ]]; then
        search_count=$((search_count + 1))
        echo -ne "\r  Searching brew for unmanaged apps... ($search_count)   "
        # Use brew search and check for exact or close match
        search_result=$(brew search --cask "/^${normalized}$/" 2>/dev/null || true)
        if [[ -n "$search_result" ]] && ! echo "$search_result" | grep -q "No formula or cask found"; then
            cat_candidates+=("$app|$normalized|$(echo "$search_result" | head -1)")
            continue
        fi
        # Try partial search
        search_result=$(brew search --cask "$normalized" 2>/dev/null | head -3 || true)
        if [[ -n "$search_result" ]] && ! echo "$search_result" | grep -q "No formula or cask found"; then
            # Check if any result looks like a match (contains the normalized name)
            best_match=$(echo "$search_result" | grep -i "$normalized" | head -1 || true)
            if [[ -n "$best_match" ]]; then
                cat_candidates+=("$app|$normalized|$best_match")
                continue
            fi
        fi
    fi

    # 6. Unmanaged
    cat_unmanaged+=("$app")
done

echo -e "\r  Categorization complete.                          "
echo ""

# ══════════════════════════════════════════════════════════════
# PHASE E: GENERATE REPORT
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase E: Generating report...${N}"

{
    echo "# Application Audit Report"
    echo "> Generated: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "> Machine: $(hostname)"
    echo ""
    echo "## Summary"
    echo ""
    echo "| Category | Count |"
    echo "|----------|-------|"
    echo "| Homebrew Cask (managed) | ${#cat_brew_managed[@]} |"
    echo "| Mac App Store | ${#cat_appstore[@]} |"
    echo "| Setapp | ${#cat_setapp[@]} |"
    echo "| Apple System | ${#cat_system[@]} |"
    echo "| Adoption Candidates (brew available) | ${#cat_candidates[@]} |"
    echo "| Unmanaged | ${#cat_unmanaged[@]} |"
    echo "| **Total** | **${#all_apps[@]}** |"
    echo ""

    echo "## Homebrew Cask Managed (${#cat_brew_managed[@]})"
    echo ""
    echo "| Application | Cask Name |"
    echo "|-------------|-----------|"
    for entry in "${cat_brew_managed[@]}"; do
        IFS='|' read -r name cask <<< "$entry"
        echo "| $name | \`$cask\` |"
    done
    echo ""

    echo "## Mac App Store (${#cat_appstore[@]})"
    echo ""
    echo "| Application | MAS ID |"
    echo "|-------------|--------|"
    for entry in "${cat_appstore[@]}"; do
        IFS='|' read -r name mid <<< "$entry"
        echo "| $name | $mid |"
    done
    echo ""

    if [[ ${#cat_setapp[@]} -gt 0 ]]; then
        echo "## Setapp Managed (${#cat_setapp[@]})"
        echo ""
        for app in "${cat_setapp[@]}"; do echo "- $app"; done
        echo ""
    fi

    echo "## Apple System (${#cat_system[@]})"
    echo ""
    for app in "${cat_system[@]}"; do echo "- $app"; done
    echo ""

    echo "## Adoption Candidates (${#cat_candidates[@]})"
    echo ""
    echo "These apps exist in Homebrew but are not currently managed by it."
    echo ""
    echo "| Application | Normalized | Brew Cask Match |"
    echo "|-------------|------------|-----------------|"
    for entry in "${cat_candidates[@]}"; do
        IFS='|' read -r name norm match <<< "$entry"
        echo "| $name | $norm | \`$match\` |"
    done
    echo ""

    echo "## Unmanaged (${#cat_unmanaged[@]})"
    echo ""
    echo "No Homebrew cask or App Store match found."
    echo ""
    for app in "${cat_unmanaged[@]}"; do echo "- $app"; done
    echo ""
} > "$REPORT"

echo -e "  Report saved to ${D}${REPORT}${N}"

# ══════════════════════════════════════════════════════════════
# PHASE F: GENERATE BREWFILE
# ══════════════════════════════════════════════════════════════
echo -e "${C}Phase F: Generating Brewfile...${N}"

{
    echo "# Brewfile — Syncrescendence Golden State"
    echo "# Generated: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "# Usage: brew bundle install --file=Brewfile"
    echo "# Diff:  brew bundle check --file=Brewfile"
    echo ""

    echo "# ── Taps ──"
    while read -r tap; do
        echo "tap \"$tap\""
    done < <(brew tap 2>/dev/null | sort)
    echo ""

    echo "# ── Formulae (CLI tools) ──"
    while read -r formula; do
        echo "brew \"$formula\""
    done < <(brew list --formula -1 2>/dev/null | sort)
    echo ""

    echo "# ── Casks (GUI applications) ──"
    while read -r cask; do
        echo "cask \"$cask\""
    done < <(brew list --cask -1 2>/dev/null | sort)
    echo ""

    if [[ ${#cat_candidates[@]} -gt 0 ]]; then
        echo "# ── Adoption Candidates (uncomment to adopt) ──"
        for entry in "${cat_candidates[@]}"; do
            IFS='|' read -r name norm match <<< "$entry"
            echo "# cask \"$match\"  # Currently manual: $name"
        done
        echo ""
    fi

    echo "# ── Mac App Store ──"
    for entry in "${cat_appstore[@]}"; do
        IFS='|' read -r name mid <<< "$entry"
        echo "mas \"$name\", id: $mid"
    done
    echo ""
} > "$BREWFILE"

echo -e "  Brewfile saved to ${D}${BREWFILE}${N}"

# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
echo ""
echo -e "${B}${BOLD}═══ Audit Complete ═══${N}"
echo ""
echo -e "  ${G}Brew Cask managed:${N}  ${#cat_brew_managed[@]}"
echo -e "  ${M}App Store:${N}          ${#cat_appstore[@]}"
if [[ ${#cat_setapp[@]} -gt 0 ]]; then
    echo -e "  ${C}Setapp:${N}             ${#cat_setapp[@]}"
fi
echo -e "  ${D}Apple System:${N}       ${#cat_system[@]}"
echo -e "  ${Y}Adoption ready:${N}     ${#cat_candidates[@]}"
echo -e "  ${R}Unmanaged:${N}          ${#cat_unmanaged[@]}"
echo ""
echo -e "  ${BOLD}Artifacts:${N}"
echo -e "    Report:   ${REPORT}"
echo -e "    Brewfile: ${BREWFILE}"
echo -e "    Backup:   ${BACKUP}"
echo ""

if [[ ${#cat_candidates[@]} -gt 0 ]]; then
    echo -e "${Y}${BOLD}Adoption candidates found!${N} To migrate them:"
    echo "  1. Review the candidates in the report"
    echo "  2. For each app you want to adopt:"
    echo "     rm -rf \"/Applications/<App>.app\" && brew install --cask <cask-name>"
    echo "  3. Or uncomment them in the Brewfile and run:"
    echo "     brew bundle install --file=$BREWFILE"
    echo ""
fi
