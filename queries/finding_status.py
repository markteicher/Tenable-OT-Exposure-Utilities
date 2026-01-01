"""
queries/finding_status.py

Tenable OT Security – FindingStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/findingstatus.doc.html

Purpose:
- Enumerates lifecycle states of a finding
"""

FINDING_STATUS_ENUM_NAME = "FindingStatus"

FINDING_STATUSES = [
    "Active",
    "Resolved",
    "Resurfaced",
]
