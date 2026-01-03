# queries/snmpv3_security_level.py
#
# Tenable OT Security – SnmpV3SecurityLevel GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/snmpv3securitylevel.doc.html
#
# Purpose:
# - Supported SNMP v3 security levels

SNMP_V3_SECURITY_LEVEL_ENUM_NAME = "SnmpV3SecurityLevel"

SNMP_V3_SECURITY_LEVEL = [
    "NoAuthNoPriv",
    "AuthNoPriv",
    "AuthPriv",
]
