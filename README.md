# Network Configuration Backup Tool (Python + Netmiko)

A simple, scalable Python script for automating network device configuration backups.  
Built with **Netmiko**, **YAML**, and **dotenv** for clean device management and secure credential handling.

---

## 📌 Features

- ✅ Backs up running configs from multiple network devices
- ✅ Uses **YAML** for device inventory (easily expandable)
- ✅ Passwords are securely handled via **environment variables** and a `.env` file (not committed to Git)
- ✅ Outputs time-stamped backups for easy versioning
- ✅ Supports any device platform supported by Netmiko (Cisco IOS, XE, NX-OS, etc.)

---

## 📂 Project Structure

network-config-backup/
├── your_script.py # Main Python script
├── devices.yaml # Device inventory (hostnames, IPs, creds, device types)
├── .env # Environment variables (kept secret, NOT in repo)
├── .gitignore # Git ignore rules
├── requirements.txt # Python dependency list
└── backups/ # Auto-generated backups (ignored by Git)

---

## ⚙️ Prerequisites

- Python 3.x
- Virtual environment (venv recommended)
- GitHub Personal Access Token (if pushing via HTTPS)

Python Packages:

pip install -r requirements.txt

---

