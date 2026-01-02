"""
queries/origin_select_field.py

Tenable OT Security – OriginSelectField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/originselectfield.doc.html

Purpose:
- Enumerates selectable fields for origin-based queries and expressions
"""

ORIGIN_SELECT_FIELD_ENUM_NAME = "OriginSelectField"

ORIGIN_SELECT_FIELDS = [
    "originId",
    "originName",
    "originNetworks",
    "originSupportActive",
]
