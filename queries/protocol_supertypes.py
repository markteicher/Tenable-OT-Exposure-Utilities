"""
queries/protocol_supertypes.py

Tenable OT Security – Protocol Supertypes (ProtocolSuperType enum)

Source documentation:
https://docs.tenable.com/OT-security/api/protocolsupertype.doc.html

Purpose:
- Define the authoritative ProtocolSuperType enum set
- Used to group low-level protocol types into higher-order protocol families
- Enables aggregation, normalization, and reporting across heterogeneous OT traffic
- Commonly applied in:
  - Event classification
  - Network policy analysis
  - Protocol usage summaries
  - Threat detection logic

Notes:
- ProtocolSuperType is intentionally broader than ProtocolType
- A single supertype may map to many ProtocolType enum values
"""

PROTOCOL_SUPERTYPES = [
    "UNKNOWN",
    "ETHERNET",
    "IP",
    "TCP",
    "UDP",
    "ICMP",
    "INDUSTRIAL_ETHERNET",
    "INDUSTRIAL_SERIAL",
    "FIELD_BUS",
    "BUILDING_AUTOMATION",
    "POWER_SYSTEMS",
    "SCADA",
    "SAFETY",
    "IOT",
    "NETWORK_MANAGEMENT",
    "REMOTE_ACCESS",
    "WEB",
    "FILE_TRANSFER",
    "DATABASE",
    "AUTHENTICATION",
    "TIME_SYNC",
    "DISCOVERY",
    "MONITORING",
]
