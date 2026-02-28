# OpenClaw Set Up for Under $20/Month
(Description: An artistic rendering of a bright red lobster floating against a sky background with white clouds, digitally illustrated with hyperrealistic details and warm lighting.)
## 5 Minute OpenClaw Set Up: AWS EC2
Here's exactly how to do it.
### What You Need
- An AWS account (free to create) ([aws.amazon.com](https://aws.amazon.com))
- An API key from Anthropic, OpenAI, or Moonshot AI
- 5 minutes
### Step 1: Launch an EC2 Instance
(Description: AWS management console interface showing the EC2 dashboard with navigation menu on the left side, search bar at the top, and blue "Launch instance" button visible. The interface displays "Amazon EC2" with the subtitle "Secure and resizable compute capacity for virtually any workload.")
Go to the AWS console and search for EC2. Click "Launch Instance."
- **Name:** Whatever you want (e.g. "openclaw-demo")
- **OS:** Ubuntu
- **Instance type:** c7i.large
- **Storage:** 20 GB minimum (default is 8, not enough)
### Step 2: Create a Key Pair
(Description: AWS key pair configuration dialog showing "Key pair (login)" section with a dropdown menu labeled "Select" and an orange "Create new key pair" button with a cursor pointer icon indicating a clickable element.)
Click "Create new key pair" and select RSA.
- Mac/Linux: choose .pem
- Windows: choose .ppk
Download it and keep it safe. This is the password to your server.
### Step 3: Configure Network Settings
(Description: AWS security group configuration panel showing network rules including a checkbox for "Allow SSH traffic from" set to "Anywhere (0.0.0.0/0)", with additional unchecked options for "Allow HTTPS traffic from the internet" and "Allow HTTP traffic from the internet".)
- Select edit
- Check "Allow SSH traffic"
- Add a new security group rule: Custom TCP, source "Anywhere", port range 8789
This opens the port so you can access OpenClaw.
### Step 4: Launch and Connect
(Description: AWS instance launch dialog with "Cancel" button on the left and a prominent orange "Launch instance" button on the right. A cursor pointer icon indicates the clickable launch button, with a small "View code" link below.)
Click launch. Go to your instance, click "Connect" twice, and a terminal opens in your browser. You're now inside your cloud server.
### Step 5: Install OpenClaw
(Description: Terminal screenshot showing the OpenClaw installation interface with ASCII art logo "OPENCLAW" at the top, followed by two menu sections: "OpenClaw onboarding" in red text and "Security" in red text, indicating the installation and security setup process.)
Go to [openclaw.ai](https://openclaw.ai), copy the install command, paste it into your EC2 terminal, and hit enter. Takes about 1 minute.
### Step 6: Run the Onboarding
(Description: Terminal screenshot displaying the onboarding menu with red text showing "quickstart" as an option and "Model/auth provider" section listing "OpenAI", "Anthropic (recommended + API key)", "MiniMax", and "Moonshot AI" as selectable model providers.)
- Select "Quick Start"
- Choose your model provider (Anthropic, OpenAI, Moonshot, etc.)
- Enter your API key
- Pick your model (I recommend Claude Opus 4.5)
- Choose how you want to communicate (Telegram, WhatsApp, Discord, Slack, terminal, web UI)
- Hatch your bot
### Step 7: Talk to It
Your AI comes online with a blank slate. It will ask who it is and who you are. Brain dump everything: your goals, your workflows, what you need help with. It saves everything to memory and starts working for you with that context.
That's it. Your own AI employee running 24/7 for less than $20/month.
Full walkthrough video linked below: [https://www.youtube.com/watch?v=M1taOWBocek](https://www.youtube.com/watch?v=M1taOWBocek)
---
**Metadata:**
- Posted: 1:58 PM · Feb 12, 2026
- Views: 1.4M
- Replies: 64
- Reposts: 261
- Likes: 2.3K
- Bookmarks: 9.7K