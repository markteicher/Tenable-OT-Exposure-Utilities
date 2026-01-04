# queries/tunnel_status.py
#
# Tenable OT Security – TunnelStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/tunnelstatus.doc.html
#
# Purpose:
# - Status of OT Security sensor tunnel

TUNNEL_STATUS_ENUM_NAME = "TunnelStatus"

TUNNEL_STATUS = [
    "NoTunnel",
    "Pending",
    "Paused",
    "Running",
]
