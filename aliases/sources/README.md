# Source Aliases

Symlink navigation layer for SOURCES/.

## Structure

```
aliases/sources/
├── by-platform/    # youtube, podcast, substack, arxiv, x
├── by-tier/        # paradigm, strategic, tactical
└── by-chain/       # intelligence, information, insight, etc.
```

## Usage

These directories contain symlinks to files in `SOURCES/processed/`.
Symlinks are created during processing based on frontmatter metadata.

## Creating Symlinks

```bash
# Example: Link a source to platform alias
ln -s ../../../SOURCES/processed/SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy.md aliases/sources/by-platform/youtube/

# Example: Link same source to tier alias
ln -s ../../../SOURCES/processed/SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy.md aliases/sources/by-tier/paradigm/
```

## Note

Aliases are populated incrementally as sources are processed.
Initial structure is skeletal; expands through use.
