"""
queries/event_category_type.py

Tenable OT Security – EventCategoryType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/eventcategorytype.doc.html

Purpose:
- Enumerates high-level categories for OT security events
"""

EVENT_CATEGORY_TYPE_ENUM_NAME = "EventCategoryType"

EVENT_CATEGORY_TYPE_VALUES = [
    "NoCategory",
    "ConfigurationEvents",
    "ScadaEvents",
    "NetworkEvents",
    "NetworkThreats",
]
