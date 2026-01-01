"""
queries/exclusion_type.py

Tenable OT Security – ExclusionType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/exclusiontype.doc.html

Purpose:
- Enumerates exclusion categories used by exclusion objects
"""

EXCLUSION_TYPE_ENUM_NAME = "ExclusionType"

EXCLUSION_TYPES = [
    "Unknown",
    "IntrusionDetection",
    "Activity",
    "Conversation",
    "IpConflict",
    "TagWrite",
    "Asset",
    "Scans",
    "OpenPort",
    "UsbChange",
    "IEC104",
    "DNP3",
    "IEC61850",
]
