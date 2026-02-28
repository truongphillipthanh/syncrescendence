#!/bin/bash
# Psyche Slack Environment Variables Template
# Place in ~/.openclaw/.env on Mac mini and chmod 600
#
# INSTRUCTIONS FOR SOVEREIGN:
# 1. Go to https://api.slack.com/apps
# 2. Create "Syncrescendence Psyche" app
# 3. Enable Socket Mode, get App-Level Token (starts with xapp-)
# 4. Install to workspace, get Bot Token (starts with xoxb-)
# 5. Copy tokens below, replacing placeholders
# 6. SSH to Mac mini: ssh home@192.168.1.2
# 7. Paste this file as ~/.openclaw/.env
# 8. chmod 600 ~/.openclaw/.env

# === REQUIRED TOKENS ===
# Generated in Slack Developer Portal (Step 3 above)
SLACK_APP_TOKEN_PSYCHE=xapp-YOUR_PSY_APP_TOKEN_HERE

# Generated in Slack Developer Portal (Step 4 above)
SLACK_BOT_TOKEN_PSYCHE=xoxb-YOUR_PSY_BOT_TOKEN_HERE

# === OPTIONAL: Discord alerts webhook (if configured) ===
# Create webhook in Discord #alerts channel, paste URL here
# DISCORD_ALERTS_WEBHOOK_URL=https://discord.com/api/webhooks/...

# === Service health check configuration ===
# Alert posting endpoint - can be Slack webhook or @psyche message
PSYCHE_ALERT_CHANNEL="#alerts"

# === Validation ===
# After setting, run: source ~/.openclaw/.env && echo $SLACK_BOT_TOKEN_PSYCHE
# Should show your token (not the literal string above)
