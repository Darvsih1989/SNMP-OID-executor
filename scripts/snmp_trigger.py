#!/usr/bin/python3
import datetime
import subprocess

LOG_FILE = "/var/log/snmp_script.log"

# Create timestamp
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log every call from SNMP
with open(LOG_FILE, "a") as f:
    f.write(f"SNMP OID triggered at {now}\n")

# Example command (optional)
# output = subprocess.getoutput("hostname")

# Output returned to SNMP client
print("Script executed OK")




