# Securing Clawdbot on a VPS with Cloudflare (Tunnel + Access + SSH Hardening)

(Description: Illustration with dark space background featuring: a laptop on left with globe icon and orange checkmark shield, a red round character with antennae standing on servers in center, a cloud storage icon with orange checkmark in top right, and a golden lock on dark brick wall on right. Connected by dotted lines suggesting data flow. Color palette: dark navy/purple background with coral red, orange, and blue accents.)

Ok, so you've got Clawdbot running on a VPS (DigitalOcean, AWS etc) and you want it secure 🔒

## Practical Goal

- No public dashboard ports
- HTTPS everywhere
- Identity-based login in front of the dashboard (not just a token)
- WebSockets protected
- Pairing stays ON (defense-in-depth)
- SSH isn't getting farmed by bots
- Setup stays maintainable (systemd, logs, simple ops)

## The Important Part

Clawdbot can end up exposed to the internet (and people have found it on Shodan). So we need to secure it as if it's a public target by default.

## Threat Model (What We're Protecting Against)

When you run a dashboard on a VPS, the danger is not "a hacker manually targeting you". The real-world threats are boring but brutal:

- Internet-wide scanning (bots scan the whole internet 24/7)
- Ports show up on Shodan (meaning: reachable publicly)
- SSH brute force (root/ubuntu/random usernames)
- Token leakage (URLs land in history, logs, screenshots, clipboard, etc)
- Origin exposure (people bypass Cloudflare and hit the VPS IP directly)
- "works today" software becomes vulnerable tomorrow (dependencies, RCE, etc)
- Someone gets access once and then tries again later from another browser/device

### The Winning Mindset

- Reduce attack surface first
- Put identity-based access in front
- Keep pairing/device trust enabled
- Harden SSH as the last line

## Why Cloudflare Tunnel is the Right Primitive

Cloudflare Tunnel is great because it flips the networking model: Instead of exposing a service and trying to defend it…you keep it private and connect outward.

Cloudflare Tunnel creates an outbound connection from your VPS to Cloudflare. Meaning:

- you don't need inbound ports for the dashboard
- your VPS IP becomes much less valuable to attackers
- Cloudflare handles TLS / HTTPS
- WebSockets work properly
- it pairs perfectly with Cloudflare Access (identity gate)

Traffic flow looks like: Browser → Cloudflare → Tunnel → `http://127.0.0.1:18789`

This is the real security win: You stop being "a random open port on the internet" and become "a private service reachable only through an authenticated gate".

## Cloudflare Tunnel Setup (Production Style)

Assumptions:
- Your domain is on Cloudflare
- You want `https://dashboard.yourdomain.com` → `http://127.0.0.1:18789`

### Step 1: Install cloudflared

See: https://github.com/cloudflare/cloudflared

### Step 2: Authenticate
```shell
cloudflared tunnel login
```

That opens the browser flow and creates `~/.cloudflared/cert.pem`. You can check:
```shell
ls -la ~/.cloudflared
```

### Step 3: Create a tunnel
```shell
cloudflared tunnel create clawdbot
```

This creates credentials JSON: `~/.cloudflared/<UUID>.json`

### Step 4: Create the tunnel config
```shell
nano /home/deploy/.cloudflared/config.yml
```

Example:
```yaml
tunnel: clawdbot
credentials-file: /home/deploy/.cloudflared/<UUID>.json
ingress:
  - hostname: dashboard.yourdomain.com
    service: http://127.0.0.1:18789
  - service: http_status:404
```

That last line is important: it's the fallback.

### Step 5: Create DNS routing
```shell
cloudflared tunnel route dns clawdbot dashboard.yourdomain.com
```

### Step 6: Test tunnel in foreground
```shell
cloudflared tunnel run clawdbot
```

Then try opening: `https://dashboard.yourdomain.com/?token=yourtoken`

If you see 502 Bad Gateway: it means Cloudflare can't reach your origin (dashboard isn't running or not reachable on localhost).

### Step 7: Run as a system service (recommended)
```shell
sudo cloudflared --config /home/deploy/.cloudflared/config.yml service install
sudo systemctl enable --now cloudflared
```

Check status:
```shell
systemctl status cloudflared
```

## Protect the Dashboard with Cloudflare Access (Zero Trust)

### Important Idea

Tunnel is NOT "auth". It's connectivity.

Cloudflare Access is what makes the dashboard go from "whoever knows the URL/token can try" to "only my identity can even reach the service".

### Why Access is Mandatory

**Without Access:**
- anyone on the internet can reach the endpoint
- token becomes your primary gate
- and tokens leak way more often than people think
- plus bots can hammer the websocket endpoints constantly

**With Access:**
- Cloudflare challenges identity before any traffic hits your VPS
- you can enforce MFA
- you can restrict by email / GitHub / Google identity
- you can add geo policies

### Setup Steps

On Cloudflare sidebar, click "Cloudflare Zero Trust"

1. Access → Applications → Add application
2. Select "Self-hosted"
3. Domain: `dashboard.yourdomain.com`
4. Add policy: Allow: your email (you@gmail.com) OR GitHub identity, optionally require MFA
5. Then a Deny-all fallback (recommended)

Optional (If you operate only in a couple countries):
- allow your country (ie: France, US)
- deny everything else

## Clawdbot Pairing: Why You See "1008 Pairing Required"

You may notice that:
- Local SSH bridge works fine
- Cloudflare URL shows: disconnected (1008): pairing required

That's expected and it's actually a good sign!

Clawdbot treats each origin (hostname + browser context) as a device identity. So `dashboard.yourdomain.com` is "a new device" compared to localhost.

### The Correct Workflow

1. open the dashboard once to trigger pairing request
2. approve device from your trusted channel / CLI
3. refresh and you're in

### Your Final Security Stack

Cloudflare Access (identity) → Clawdbot token (secret) → Clawdbot pairing (device trust)

That's defense-in-depth done right.

**Docs:**
- https://docs.clawd.bot/gateway/bridge-protocol
- https://docs.clawd.bot/gateway/pairing

## SSH Hardening: Stop Getting Farmed by Bots

NOTE: This assumes you are already logging in to your VPS via a dedicated user and SSH keys (and never root).

We want:
- no password brute force possible
- root login disabled
- keys only
- repeat offenders automatically banned

### Disable Root Login and Password Auth
```shell
sudo nano /etc/ssh/sshd_config
```

Set:
```plaintext
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

Restart:
```shell
sudo systemctl restart ssh
```

**Important:** keep your current SSH session open until you confirm a new login works.

## Firewall (UFW) Rules That Won't Lock You Out

If you're using Cloudflare Tunnel, your dashboard doesn't need inbound ports. So don't open them.

### Enable UFW with OpenSSH Allowed
```shell
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
```

### Best Practice: Allow SSH Only From Your Home IP (If Stable)
```shell
sudo ufw deny 22/tcp
sudo ufw status numbered
sudo ufw allow from YOUR.IP.ADDRESS.HERE to any port 22 proto tcp
```

If your IP changes often: keep SSH open but use fail2ban.

## Fail2ban: Automatically Ban Brute-Force Attempts

### Install
```shell
sudo apt update
sudo apt install -y fail2ban
sudo systemctl enable --now fail2ban
```

### Check
```shell
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

For most VPS setups, the default config is already doing useful work.

## Operational Hygiene

Keep system updated (avoid getting hacked via an unpatched vulnerability):
```shell
sudo apt update
sudo apt upgrade -y
```

## Final "Are We Done?" Checklist

- Dashboard port not reachable on VPS IP (no Shodan exposure)
- Dashboard listens on localhost only (127.0.0.1:18789)
- Cloudflare Tunnel routes `dashboard.yourdomain.com` → localhost
- Cloudflare Access enabled with strict allow + MFA
- Pairing enabled and approved devices only
- SSH: no root login, no password auth, keys only
- UFW enabled, only SSH inbound
- fail2ban running
- cloudflared running as a service

## Useful Links

### Cloudflare

- Tunnel overview: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/
- Get started: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/
- Local management: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/local-management/
- Tunnel as a service: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/local-management/as-a-service/
- Cloudflare Access: https://developers.cloudflare.com/cloudflare-one/policies/access/

### Clawdbot

- Bridge protocol: https://docs.clawd.bot/gateway/bridge-protocol
- Pairing: https://docs.clawd.bot/gateway/pairing
- Remote control UI: https://docs.clawd.bot/gateway/remote
- Control UI: https://docs.clawd.bot/web/control-ui