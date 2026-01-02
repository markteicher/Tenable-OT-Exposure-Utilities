# queries/scan_action.py
#
# Tenable OT Security – ScanAction GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/scanaction.doc.html
#
# Purpose:
# - Actions that can be performed on a scan

SCAN_ACTION_ENUM_NAME = "ScanAction"

SCAN_ACTION = [
    "Launch",
    "Pause",
    "Resume",
    "Stop",
    "Kill",
]
