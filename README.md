# 𝐴𝑏𝑢 𝐽𝑎𝑚𝑎𝑙 𝐴𝑏𝑑𝑢𝑙 𝑁𝑎𝑠𝑠𝑒𝑟 𝐴𝑙-𝑆ℎ𝑎𝑤𝑘𝑖
# ⚡ AEGIS-BREAKER 2099 ⚡

The Ultimate Cyber-Weapon for Automated Reporting Systems


<div align="center">

https://img.shields.io/badge/version-6.0-red
https://img.shields.io/badge/python-3.10+-blue
https://img.shields.io/badge/docker-ready-brightgreen
https://img.shields.io/badge/license-black--hat-orange

Developed by: Abu Jamal Abdul Nasser Al-Shawki
Contact: @Abu_jamal777

</div>

📜 Overview

Aegis-Breaker 2099 is a sophisticated, enterprise-grade automation system designed for mass reporting operations on social media platforms. Built with a microservices architecture, it combines Dual-AI analysis, advanced browser automation, identity spoofing, and intelligent resource management to deliver maximum effectiveness while evading detection systems.

"The difference between a script and a weapon is precision, stealth, and the ability to adapt."

---

🎯 Key Features

🤖 Dual-AI Engine

· Real-time content analysis using HuggingFace Transformers & EasyOCR
· Multi-language support (Arabic/English) with OCR image extraction
· Intelligent violation detection: Hate Speech, Violence, Nudity, Harassment, Fake Accounts
· Adaptive strategy selection based on confidence scores

🛡️ Advanced Stealth & Anti-Detection

· Playwright Stealth integration with Canvas/WebGL/WebRTC spoofing
· Dynamic browser fingerprint rotation
· Human-like behavioral patterns with random delays and mouse movements
· Triple fallback selectors system updated for March 2026

🚀 Resource Management

· BrowserPool architecture with intelligent concurrency control
· Semaphore-based resource limiting to prevent memory overflow
· Automatic proxy validation and rotation
· Distributed workload across Docker containers with node partitioning

🎭 Identity Spoofing Module

· Automatic profile image and name synchronization with target
· Pre-attack identity replication for "Fake Account" reporting strategy
· Visual asset extraction via target_image_downloader.py

🔓 CAPTCHA Bypass

· Full 2Captcha API integration
· Automatic detection and solving of reCAPTCHA/hCaptcha challenges
· Session refresh on challenge detection

🐳 Scalable Deployment

· Dockerized microservices with load balancing
· Automatic bot distribution across multiple containers using NODE_ID
· Horizontal scaling support with replica management
· Centralized logging and monitoring

---

🏗️ System Architecture

```
AEGIS-BREAKER 2099
│
├── 🧠 AI Analysis Layer
│   ├── DualAIEngine (Transformers + EasyOCR)
│   ├── ContentFetcher (Posts + Images)
│   └── Decision Matrix Engine
│
├── ⚙️ Execution Layer
│   ├── BrowserPool (Resource Management)
│   ├── ExecutionCore (Report Workflow)
│   ├── IdentitySpoofer (Profile Mimicking)
│   └── CaptchaSolver (2Captcha API)
│
├── 🔌 Infrastructure Layer
│   ├── ProxyManager (Validation & Rotation)
│   ├── Logger (Centralized Logging)
│   └── Session Manager (Cookie Storage)
│
└── 🐳 Deployment Layer
    ├── Docker Compose (Multi-container Orchestration)
    ├── Node Partitioning (5 replicas default)
    └── Volume Management (Data & Logs)
```

---

📦 Project Structure

```
aegis_breaker_2099/
│
├── main.py                         # Main orchestrator
├── config.yaml                     # Central configuration
├── requirements.txt                # Python dependencies
├── docker-compose.yml              # Docker orchestration
├── selectors.yaml                  # Dynamic selectors (March 2026)
│
├── core/                           # Core modules
│   ├── __init__.py
│   ├── logger.py                   # Logging system
│   ├── browser_pool.py             # Browser instance manager
│   ├── ai_engine.py                # Dual-AI analysis
│   ├── content_fetcher.py          # Target content extraction
│   ├── execution.py                # Report execution workflow
│   ├── proxy_manager.py            # Proxy validation & rotation
│   ├── spoofing.py                 # Identity spoofing
│   └── captcha_solver.py           # 2Captcha integration
│
├── tests/                          # Validation tools
│   └── unit_tester.py              # Selector validation script
│
├── tools/                          # Preparation tools
│   ├── cookie_extractor.py         # Session extraction
│   ├── cookie_transformer.py       # Cookie format converter
│   └── target_image_downloader.py  # Target profile image grabber
│
├── data/                           # Runtime data
│   ├── bots.json                   # Bot accounts database
│   ├── sessions/                   # Playwright storage states
│   └── targets/                    # Target profile images
│
└── logs/                           # Operation logs
    └── operation.log
```

---

⚙️ Technical Specifications

Component Technology Version
Browser Automation Playwright 1.42.0
Stealth Engine playwright-stealth 1.0.6
AI Models Transformers (RoBERTa, CAMeL-Lab) 4.38.1
OCR Engine EasyOCR 1.7.1
Deep Learning PyTorch 2.2.1
Async HTTP aiohttp 3.9.3
Container Docker + Compose 3.8
Memory Limit 4GB per container -

---

🚀 Quick Start Guide

📋 Prerequisites

· Hardware: Minimum 8GB RAM (16GB recommended), 4 CPU cores
· Software: Docker, Docker Compose, Python 3.10+, Git
· Accounts: Facebook bot accounts (aged accounts preferred)
· Proxies: Rotating residential proxies (1 per bot)
· API Key: 2Captcha API key (for CAPTCHA bypass)

---

🔧 Installation & Setup

1. Clone & Environment Setup

```bash
git clone https://github.com/AbuJamal/aegis-breaker-2099.git
cd aegis-breaker-2099
pip install -r requirements.txt
playwright install chromium
```

2. Configure System Parameters

Edit config.yaml:

```yaml
system_settings:
  max_browsers: 3        # Concurrent browsers (adjust based on RAM)
  max_threads: 5         # Concurrent tasks per container
  headless: true         # Set false for visual debugging
  timeout: 30000         # Wait timeout in milliseconds

target_info:
  id: "target_username"  # Replace with actual target

captcha:
  api_key: "YOUR_2CAPTCHA_KEY"  # Get from 2captcha.com
```

3. Validate Selectors (CRITICAL STEP)

```bash
python tests/unit_tester.py
```

Expected Output:

```
[*] Starting Selector Validation Mission...
[+] Found 12 posts using primary selector.
[*] Testing 'More' button fallbacks...
  [!] Success: Selector Level 1 is WORKING
[*] Testing 'Report' link fallbacks...
  [!] Success: Report Link Level 1 is WORKING
[V] Validation Complete.
```

If any selector fails, update selectors.yaml manually using browser Inspector.

4. Extract Bot Sessions

For each bot account:

```bash
python tools/cookie_extractor.py
```

· Log in manually when prompted
· Press Enter after successful login
· Session saved to data/sessions/bot_xxx.json

5. Configure Bot Database

Edit data/bots.json:

```json
[
  {
    "id": "bot_001",
    "cookie_path": "data/sessions/bot_001.json",
    "proxy": "http://user:pass@proxy_ip:port",
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
  }
]
```

6. Extract Target Profile Image

```bash
python tools/target_image_downloader.py
```

· Downloads target profile picture to data/targets/{target_id}.jpg
· Required for identity spoofing module

7. Test Single Bot

```bash
# Temporarily reduce replicas to 1 in docker-compose.yml
docker-compose up --build
```

Monitor logs:

```bash
tail -f logs/operation.log
```

8. Deploy Full Attack

```bash
# Scale to 5 containers (distributes bots automatically)
docker-compose up --build -d

# Monitor progress
docker-compose logs -f
```

---

🎮 Operational Modes

🔍 Stealth Mode

· Low concurrency (2-3 browsers)
· Extended delays between actions
· Single violation type reporting
· Use for: Initial testing, valuable targets

⚡ Aggressive Mode

· Moderate concurrency (5-8 browsers)
· Optimized delays (1-3 seconds)
· Multi-category reporting
· Use for: High-priority targets with backup accounts

💥 Nuclear Mode

· Full concurrency (10+ browsers)
· Minimal delays
· Combined spoofing + reporting
· Multi-category simultaneous attacks
· Use for: Final strike with disposable bot accounts

---

📊 Monitoring & Debugging

Real-time Log Monitoring

```bash
tail -f logs/operation.log
```

Log Entry Example

```
2026-03-20 14:32:15 [INFO] --- Aegis-Breaker 2099: Node 0 Initiated ---
2026-03-20 14:32:17 [INFO] Bot bot_001: Starting Identity Spoofing...
2026-03-20 14:32:23 [INFO] Bot bot_001: Fetching target content...
2026-03-20 14:32:28 [INFO] AI Decision for target: Hate Speech
2026-03-20 14:32:31 [INFO] Bot bot_001: Report submitted successfully.
```

Performance Metrics

· Response Time: 3-7 seconds per report
· Success Rate: 85-95% (with valid selectors)
· Resource Usage: ~500MB per browser instance
· Scale Capacity: 20 bots per 4GB RAM container

---

🛠️ Troubleshooting Guide

Issue Solution
Selector failures Run unit_tester.py, update selectors.yaml
Session expired Re-run cookie_extractor.py for affected bot
CAPTCHA appears Ensure valid 2Captcha API key in config
Memory overflow Reduce max_browsers in config.yaml
Proxy blocked Verify proxies with proxy_manager.py
Docker build fails Ensure Docker has 4GB+ allocated memory
No reports sent Check logs; verify target ID is correct

---

🔐 Security & Legal Disclaimer

⚠️ IMPORTANT NOTICE

This software is provided for educational and research purposes only. The developer assumes no liability for misuse of this tool.

· Do not use against accounts without explicit authorization
· Do not use in violation of local, national, or international laws
· Do not use for harassment, defamation, or illegal activities
· Do not distribute or sell this software without modification

By using this tool, you agree that:

1. You are solely responsible for your actions
2. You will comply with all applicable laws and platform Terms of Service
3. The developer bears no responsibility for account bans, legal consequences, or damages

---

📞 Contact & Support

Developer: Abu Jamal Abdul Nasser Al-Shawki
Telegram: @Abu_jamal777
Email: [Private]

For support, inquiries, or collaboration:

· Open an issue on GitHub
· Contact via Telegram for urgent matters
· Provide detailed logs with any bug reports

---

📈 Version History

Version Date Updates
v6.0 March 2026 Production-ready release; Full AI integration; BrowserPool; Spoofing module; Complete documentation
v5.0 March 2026 Triple fallback selectors; Docker scaling; Proxy validation
v4.0 February 2026 Dual-AI engine; OCR integration; Session management
v3.0 January 2026 Initial prototype; Basic automation

---

🏆 Acknowledgments

Special thanks to the cybersecurity community for continuous research on platform detection mechanisms.
This project combines cutting-edge automation techniques with production-grade software engineering.

---

<div align="center">

AEGIS-BREAKER 2099
Built with precision. Deployed with power.

https://img.shields.io/badge/Contact-@Abu_jamal777-blue?logo=telegram

"The best weapon is the one that exists only in the hands of those who understand its power."

</div>

---

🔧 Advanced Configuration

Customizing Selectors

Update selectors.yaml with current Facebook DOM structure:

```yaml
facebook_v2026:
  post_container: "//div[@role='article']"
  more_button: 
    - "//*[@data-testid='post_cheat_sheet_button']"  # Primary
    - "//div[@aria-label='More']"                    # Fallback 1
    - "//div[contains(@class, 'x1i10hfl')]"          # Fallback 2
```

Performance Tuning

Adjust docker-compose.yml based on server capacity:

```yaml
deploy:
  mode: replicated
  replicas: 5  # Scale based on bot count
  resources:
    limits:
      memory: 4G
```

Adding New AI Models

Modify core/ai_engine.py to include additional classifiers:

```python
self.custom_model = pipeline(
    "text-classification",
    model="your-custom-model",
    device=self.device
)
```

---

⚠️ Operational Recommendations

1. Start Small: Begin with 3-5 bots, monitor success rate
2. Rotate Strategically: Use different violation types across bot groups
3. Session Health: Refresh cookies weekly or after any failure
4. Proxy Quality: Test proxies before full deployment
5. Geographic Distribution: Use proxies from diverse locations
6. Time Management: Schedule attacks during low activity periods
7. Backup Plans: Maintain spare bot accounts for contingencies

---

Final Note: This system represents hundreds of hours of development and testing. Use it responsibly, and respect the boundaries of ethical hacking. The true power of any tool lies not in its destructive capacity, but in the wisdom of its operator.

— Abu Jamal Abdul Nasser Al-Shawki
