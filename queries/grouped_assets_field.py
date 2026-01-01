"""
queries/grouped_assets_field.py

Tenable OT Security – GroupedAssetsField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/groupedassetsfield.doc.html

Purpose:
- Enumerates fields used when grouping assets
"""

GROUPED_ASSETS_FIELD_ENUM_NAME = "GroupedAssetsField"

GROUPED_ASSETS_FIELDS = [
    "assetsCount",
    "type",
    "vendor",
    "os",
    "family",
    "risk",
    "criticality",
    "purdueLevel",
    "category",
    "firstSeen",
    "site",
]
