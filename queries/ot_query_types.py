"""
queries/ot_query_types.py

Tenable OT Security – OtQueryTypes GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/otquerytypes.doc.html

Purpose:
- Enumerates OT-specific query operation types used by the OT engine
"""

OT_QUERY_TYPES_ENUM_NAME = "OtQueryTypes"

OT_QUERY_TYPES = [
    "BpScanType",
    "CharacteristicsType",
    "IdentificationType",
    "RunStatusType",
    "SnapshotType",
]
