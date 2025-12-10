#!/bin/bash

# Test the custom OID from a client
snmpget -v2c -c public $1 1.3.6.1.4.1.55555.1
