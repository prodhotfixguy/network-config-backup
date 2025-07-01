## Network Configuration Backup Script (Lab Project)

### Description:

This is a **personal learning project** built to practice Python scripting for network automation tasks. The script was designed to simulate automating the process of backing up running configurations from network devices such as Cisco switches and routers.

While this tool was not deployed in production, the project helped me gain experience working with:

- **Python scripting for network device interaction**
- **YAML-based inventory management**
- **File handling for configuration storage**
- **Environment variable management for sensitive data**
- **Version control workflows using Git (local repo only)**

---

### Features:

- Connects to a list of devices (defined in a YAML file)
- Uses SSH (via Paramiko or Netmiko—update depending on your script)
- Pulls running configurations
- Saves configs with timestamped filenames for archival
- Includes error handling for unreachable devices

---

### Technologies Used:

- Python 3.x
- YAML
- Git (local, personal use)

---

### Disclaimer:

This was a **lab project** built for educational purposes only and was **not deployed in a production environment**.