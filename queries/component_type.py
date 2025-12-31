"""
queries/component_type.py

Tenable OT Security – ComponentType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/componenttype.doc.html

Purpose:
- Enumerates high-level component types used by Tenable OT
"""

COMPONENT_TYPE_ENUM_NAME = "ComponentType"

COMPONENT_TYPES = [
    "Unknown",
    "Events",
    "Vulnerabilities",
    "Backplane",
]
