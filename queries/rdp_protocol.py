# queries/rdp_protocol.py
#
# Tenable OT Security – RdpProtocol GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/rdpprotocol.doc.html
#
# Purpose:
# - Enumerates RDP protocol types

RDP_PROTOCOL_ENUM_NAME = "RdpProtocol"

RDP_PROTOCOLS = [
    "Rdp",
    "Ssl",
    "Hybrid",
    "Rdstls",
    "HybridEx",
]
