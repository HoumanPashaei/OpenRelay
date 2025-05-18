# 🔐 SMTP Open Relay Checker

This is a lightweight tool to check whether an SMTP server is vulnerable to **Open Relay** — a misconfiguration that allows anyone to send emails through the server without authentication.

---

## ⚠️ What Is an Open Relay?

An open relay is an SMTP server configured to allow anyone on the internet to send email through it — including emails from unauthorized domains or senders. This can be abused by spammers and cause the server's IP to get blacklisted.

---

## 🔍 Step 1 — Discover the SMTP Port

Before running the tool, scan the server to discover which port is used for SMTP. Some administrators change the default ports (25, 465, 587) to uncommon ones.

### Use Nmap:

```bash
nmap -sS -p- --open --max-rate 100 -T2 --script smtp-commands,smtp-open-relay -Pn smtp.example.com
```

If you're in a hurry, scan only common SMTP ports:

```bash
nmap -sS -p 25,465,587,2525,1025,8025,26 --script smtp-commands,smtp-open-relay -Pn smtp.example.com
```

---

## 🚀 Features

- Sends a crafted email to test if relay is allowed without authentication
- Uses `colorama` for clear color-coded output
- Allows custom SMTP server, port, sender, and receiver via CLI
- Supports STARTTLS connections
- Requires no authentication

---

## 🧪 Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Checker

```bash
python relay_checker.py --server smtp.example.com --port 25 --sender fake@evil.com --receiver you@gmail.com
```

---

## ✋ Manual Test (Telnet)

```bash
telnet smtp.example.com 25
```

```
HELO test.com
MAIL FROM:<attacker@evil.com>
RCPT TO:<your.email@gmail.com>
DATA
Subject: Open Relay Test

Hello, this is a test message.

.
QUIT
```

---

## 📦 File Overview

```text
relay_checker.py     # Main script
requirements.txt     # Python dependencies
README.md            # You're reading it
```

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed by a bug bounty hunter and security enthusiast 🕵️‍♂️  
For legal testing only — use responsibly.
