from netmiko import ConnectHandler
import yaml
import os
from datetime import datetime
from dotenv import load_dotenv

# Load enivronment variables from the .env file
load_dotenv()

# Load devies from the YAML file
with open("devices.yaml", "r") as f:
    devices = yaml.safe_load(f)["devices"]

# Create timestamped backup directory
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_dir = f"backups/{timestamp}"
os.makedirs(backup_dir, exist_ok=True)

# Loop through each device and back up the config
for device in devices:
    print(f"Connecting to {device['name']} ({device['ip']})...")

    try:
        # Get password from environment variable
        password = os.getenv(device["password_env"])
        if not password:
            raise ValueError(f"Missing password for  {device['name']} ({device['ip']})... Check you .env file.")
        
        # Create connection handler
        connection = ConnectHandler(
            device_type=device["device_type"],
            ip=device["ip"],
            username=device["username"],
            password=password
        )

        # Run command and save config
        output = connection.send_command("show running-config")
        with open(f"{backup_dir}/{device['name']}.txt", "w") as f:
            f.write(output)
        connection.disconnect()
        print(f"Backup complete for {device['name']}.")
    except Exception as e:
        print(f"Failed to back up {device['name']}: {e}")

