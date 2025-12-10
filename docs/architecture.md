
# SNMP OID Executor - Architecture

## Overview
This project demonstrates how to trigger a Python script on a Linux server
whenever an SNMP GET is performed on a specific custom OID.

## SNMP Flow
1. A monitoring system (PRTG, Zabbix, LibreNMS, or snmpget client) sends a GET request.
2. SNMPD receives the request.
3. The OID is mapped to an 'extend' command.
4. extend executes a Python script.
5. Output of the script is returned as SNMP data.
6. Script writes log entries to the Linux filesystem.

## Technologies
- Net-SNMP (snmpd)
- Python3
- Custom OID (.1.3.6.1.4.1.55555.1)
- Bash testing tools (snmpget)
