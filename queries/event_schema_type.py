"""
queries/event_schema_type.py

Tenable OT Security – EventSchemaType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/eventschematype.doc.html

Purpose:
- Enumerates schema types used for OT event records
"""

EVENT_SCHEMA_TYPE_ENUM_NAME = "EventSchemaType"

EVENT_SCHEMA_TYPES = [
    "UnknownSchema",
    "NetworkSchema",
    "AssetSchema",
    "PortSchema",
    "SrcDstSchema",
    "ScheduleOnlySchema",
    "TagDataSchema",
    "IntrusionDetectionSchema",
]
