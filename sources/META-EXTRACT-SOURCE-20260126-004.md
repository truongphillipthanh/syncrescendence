# Extraction: SOURCE-20260126-004

**Source**: `SOURCE-20260126-x-article-fakenine_-securing_clawdbot_on_a_vps_with_cloudflare_tunnel_access_ssh_hardening.md`
**Atoms extracted**: 27
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (6)

### ATOM-SOURCE-20260126-004-0002
**Lines**: 20-22
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Clawdbot can be exposed to the internet and found on Shodan, necessitating its security as a public target by default.

### ATOM-SOURCE-20260126-004-0006
**Lines**: 50-54
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Cloudflare Tunnel eliminates the need for inbound ports for the dashboard, reduces the VPS IP's value to attackers, handles TLS/HTTPS, supports WebSockets, and integrates with Cloudflare Access for identity gating.

### ATOM-SOURCE-20260126-004-0009
**Lines**: 116-120
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Without Cloudflare Access, anyone can reach the endpoint, tokens become the primary gate and are prone to leakage, and bots can constantly hammer websocket endpoints.

### ATOM-SOURCE-20260126-004-0010
**Lines**: 122-126
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> With Cloudflare Access, identity is challenged before traffic reaches the VPS, enabling MFA enforcement, restriction by email/GitHub/Google identity, and geo-policies.

### ATOM-SOURCE-20260126-004-0012
**Lines**: 147-149
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Clawdbot treats each origin (hostname + browser context) as a unique device identity, requiring pairing for new devices like `dashboard.yourdomain.com`.

### ATOM-SOURCE-20260126-004-0025
**Lines**: 248-248
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.50, epistemic_stability=0.90

> For most VPS setups, the default fail2ban configuration is sufficient for basic protection.

## Concept (2)

### ATOM-SOURCE-20260126-004-0005
**Lines**: 45-47
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Cloudflare Tunnel is a networking model that flips traditional security by connecting outward from a private service to Cloudflare, rather than exposing the service and defending it.

### ATOM-SOURCE-20260126-004-0008
**Lines**: 110-112
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Cloudflare Tunnel provides connectivity, while Cloudflare Access provides authentication, transforming dashboard access from token-based to identity-based.

## Framework (4)

### ATOM-SOURCE-20260126-004-0003
**Lines**: 27-36
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Real-world threats to a dashboard on a VPS include internet-wide scanning, Shodan exposure, SSH brute force, token leakage, origin exposure (bypassing Cloudflare), software vulnerabilities, and persistent access attempts.

### ATOM-SOURCE-20260126-004-0014
**Lines**: 158-160
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> A robust security stack for Clawdbot combines Cloudflare Access for identity, Clawdbot token for secrets, and Clawdbot pairing for device trust, representing defense-in-depth.

### ATOM-SOURCE-20260126-004-0019
**Lines**: 213-217
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> A secure Clawdbot setup ensures the dashboard port is not reachable on the VPS IP, listens only on localhost, routes through Cloudflare Tunnel, and has Cloudflare Access enabled with strict allow policies and MFA.

### ATOM-SOURCE-20260126-004-0027
**Lines**: 257-266
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> A checklist for system security and operational hygiene includes: ensuring the dashboard port is not reachable on the VPS IP, the dashboard listens on localhost only, Cloudflare Tunnel routes `dashboard.yourdomain.com` to localhost, Cloudflare Access is enabled with strict allow and MFA, pairing is enabled for approved devices only, SSH has no root login or password auth (keys only), UFW is enabled with only SSH inbound, fail2ban is running, and cloudflared is running as a service.

## Praxis Hook (15)

### ATOM-SOURCE-20260126-004-0001
**Lines**: 10-16
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To secure Clawdbot on a VPS, ensure no public dashboard ports, use HTTPS everywhere, implement identity-based login, protect WebSockets, keep pairing enabled, harden SSH, and maintain the setup with systemd and logs.

### ATOM-SOURCE-20260126-004-0004
**Lines**: 39-42
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To secure a VPS, first reduce the attack surface, then implement identity-based access, keep pairing/device trust enabled, and finally harden SSH.

### ATOM-SOURCE-20260126-004-0007
**Lines**: 63-105
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up Cloudflare Tunnel, install `cloudflared`, authenticate to create `cert.pem`, create a tunnel to generate a UUID JSON, configure `config.yml` with hostname and service, route DNS, test in the foreground, and then run as a system service.

### ATOM-SOURCE-20260126-004-0011
**Lines**: 130-136
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up Cloudflare Access, navigate to Cloudflare Zero Trust, add a self-hosted application, specify the domain, and add policies to allow specific identities (e.g., email, GitHub) with optional MFA, followed by a deny-all fallback.

### ATOM-SOURCE-20260126-004-0013
**Lines**: 152-155
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The correct workflow for Clawdbot pairing involves opening the dashboard to trigger a pairing request, approving the device from a trusted channel/CLI, and then refreshing the page.

### ATOM-SOURCE-20260126-004-0015
**Lines**: 167-175
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To harden SSH, disable root login and password authentication by setting `PermitRootLogin no` and `PasswordAuthentication no` in `/etc/ssh/sshd_config`, ensuring `PubkeyAuthentication yes` is set, and restarting the SSH service.

### ATOM-SOURCE-20260126-004-0016
**Lines**: 180-191
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If using Cloudflare Tunnel, the dashboard does not require inbound ports; enable UFW and allow only OpenSSH, or restrict SSH access to a specific home IP if stable.

### ATOM-SOURCE-20260126-004-0017
**Lines**: 194-204
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Install and enable Fail2ban to automatically ban SSH brute-force attempts; the default configuration is often sufficient for most VPS setups.

### ATOM-SOURCE-20260126-004-0018
**Lines**: 207-210
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Regularly update the system using `sudo apt update` and `sudo apt upgrade -y` to prevent vulnerabilities from unpatched software.

### ATOM-SOURCE-20260126-004-0020
**Lines**: 228-228
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To deny SSH access on port 22 via UFW, use the command `sudo ufw deny 22/tcp`.

### ATOM-SOURCE-20260126-004-0021
**Lines**: 230-230
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To allow SSH access from a specific IP address, use the UFW command `sudo ufw allow from YOUR.IP.ADDRESS.HERE to any port 22 proto tcp`.

### ATOM-SOURCE-20260126-004-0022
**Lines**: 233-233
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> If your IP address changes frequently, keep SSH open but implement fail2ban to automatically ban brute-force attempts.

### ATOM-SOURCE-20260126-004-0023
**Lines**: 239-241
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> Install fail2ban using `sudo apt update`, then `sudo apt install -y fail2ban`, and enable it with `sudo systemctl enable --now fail2ban`.

### ATOM-SOURCE-20260126-004-0024
**Lines**: 245-246
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> Check the status of fail2ban using `sudo fail2ban-client status` or `sudo fail2ban-client status sshd`.

### ATOM-SOURCE-20260126-004-0026
**Lines**: 252-253
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To keep a system updated and avoid vulnerabilities, regularly run `sudo apt update` and `sudo apt upgrade -y`.
