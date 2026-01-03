# queries/snmpv3_auth_protocol.py
#
# Tenable OT Security – SnmpV3AuthProtocol GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/snmpv3authprotocol.doc.html
#
# Purpose:
# - Defines supported SNMP v3 authentication protocols

SNMP_V3_AUTH_PROTOCOL_ENUM_NAME = "SnmpV3AuthProtocol"

SNMP_V3_AUTH_PROTOCOL = [
    "NoAuth",
    "MD5",
    "SHA",
    "SHA224",
    "SHA256",
    "SHA384",
    "SHA512",
]
