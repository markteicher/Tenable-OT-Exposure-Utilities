"""
queries/format_type.py

Tenable OT Security – FormatType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/formattype.doc.html

Purpose:
- Enumerates display/formatting types for fields
"""

FORMAT_TYPE_ENUM_NAME = "FormatType"

FORMAT_TYPES = [
    "None",
    "Time",
    "Duration",
    "Bytes",
    "KBytes",
    "Grid",
    "Array",
    "Risk",
    "HyperLink",
    "Segment",
    "Enum",
    "Vendor",
    "Criticality",
]
