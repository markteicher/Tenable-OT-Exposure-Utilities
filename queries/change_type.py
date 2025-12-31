"""
queries/change_type.py

Tenable OT Security – ChangeType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/changetype.doc.html

Purpose:
- Enumerates block-level change types detected by Tenable OT
- Used by Block, change detection, and configuration-drift tracking
- Describes how a block changed between revisions
"""

CHANGE_TYPE_ENUM_NAME = "ChangeType"

CHANGE_TYPES = [
    "BlockUnchanged",
    "BlockAdded",
    "BlockDeleted",
    "BlockDataChanged",
    "BlockChangeUnknown",
]
