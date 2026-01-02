# queries/port_scan_range.py
#
# Tenable OT Security – PortScanRange GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/portscanrange.doc.html
#
# Purpose:
# - Enumerates supported port scan ranges

PORT_SCAN_RANGE_ENUM_NAME = "PortScanRange"

PORT_SCAN_RANGES = [
    "Basic",
    "Lean",
    "FullSweep",
]
