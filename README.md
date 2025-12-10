SNMP OID Executor

A lightweight and extensible solution that allows a Linux server running Net-SNMP to execute a Python script whenever a predefined custom OID is queried via SNMP.

This project demonstrates how to bind a script to an SNMP OID using the extend directive in snmpd.conf. When an SNMP GET request is made, Net-SNMP triggers the Python script and returns its output.

🚀 Features

Execute Python script on SNMP GET request

Custom enterprise OID implementation

Logging executed actions on the server

Simple testing tools (Bash + SNMP utilities)

Works with PRTG, LibreNMS, Zabbix, Nagios, or any SNMP client

📂 Project Structure

snmp-oid-executor/ │ ├── snmpd.conf.example # Example snmpd configuration ├── scripts/ │ └── snmp_trigger.py # Python script executed via SNMP ├── tests/ │ └── test_oid.sh # Test helper for calling the OID ├── docs/ │ └── architecture.md # Project architecture & flow └── README.md 

🧠 How It Works

An SNMP GET request is sent to a predefined OID.

Net-SNMP receives the request.

The OID is mapped via extend to a Python script.

SNMPD executes the script and captures its output.

The output is sent back to the SNMP client.

The script logs each execution to the server.

🛠 Installation (Ubuntu Server)

1. Install SNMP and tools

sudo apt update sudo apt install snmpd snmp libsnmp-dev 

2. Copy project files

sudo mkdir -p /opt/snmp-executor sudo cp -r scripts /opt/snmp-executor/ 

3. Make the Python script executable

sudo chmod +x /opt/snmp-executor/scripts/snmp_trigger.py 

4. Configure SNMPD

Open configuration:

sudo nano /etc/snmp/snmpd.conf 

Replace or add:

rocommunity public extend .1.3.6.1.4.1.55555.1 snmp_exec /usr/bin/python3 /opt/snmp-executor/scripts/snmp_trigger.py 

5. Restart SNMPD

sudo systemctl restart snmpd sudo systemctl status snmpd 

🧪 Testing the OID

From any SNMP-enabled machine:

snmpget -v2c -c public <SERVER_IP> 1.3.6.1.4.1.55555.1 

Expected Output:

SNMPv2-SMI::enterprises.55555.1 = STRING: "Script executed OK" 

Or use the included test script:

bash tests/test_oid.sh <SERVER_IP> 

📜 Logging

Every SNMP call generates a log entry:

/var/log/snmp_script.log 

Example log line:

SNMP OID triggered at 2025-01-15 10:22:14 

🔐 Security Notes

Change the community string in production

Restrict SNMP access via firewall:

sudo ufw allow from <monitoring_ip> to any port 161 

Use SNMPv3 for secure deployments

Never expose SNMP to the public internet

🧩 Customization

You can modify the Python script to:

Restart services

Collect server metrics

Trigger Ansible playbooks

Validate system health

Return JSON or structured text

🏁 Conclusion

This project is a practical example of integrating Linux automation with SNMP protocols. It provides a clean, extensible foundation for more advanced infrastructure automation and monitoring solutions.

If you'd like additional OIDs, multi-script support, SNMPv3 configs, or integration with monitoring tools—contributions and suggestions are welcome!
