"""
queries/network_group_type.py

Tenable OT Security – NetworkGroupType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/networkgrouptype.doc.html

Purpose:
- Enumerates supported network group types for port and protocol grouping
"""

NETWORK_GROUP_TYPE_ENUM_NAME = "NetworkGroupType"

NETWORK_GROUP_TYPES = [
    "ProtocolList",
    "PortList",
    "ProtocolFunction",
    "PortFunction",
]
