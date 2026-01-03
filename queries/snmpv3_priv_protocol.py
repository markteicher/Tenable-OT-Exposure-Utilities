# queries/snmpv3_priv_protocol.py
#
# Tenable OT Security – SnmpV3PrivProtocol GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/snmpv3privprotocol.doc.html
#
# Purpose:
# - Supported SNMP v3 privacy (encryption) protocols

SNMP_V3_PRIV_PROTOCOL_ENUM_NAME = "SnmpV3PrivProtocol"

SNMP_V3_PRIV_PROTOCOL = [
    "NoPriv",
    "DES",
    "AES",
    "AES192",
    "AES256",
    "AES192C",
    "AES256C",
]
