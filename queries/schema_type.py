# queries/schema_type.py
#
# Tenable OT Security – SchemaType GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/schematype.doc.html
#
# Purpose:
# - Defines the schema context used by rules, policies, and detections

SCHEMA_TYPE_ENUM_NAME = "SchemaType"

SCHEMA_TYPE = [
    "UnknownSchema",
    "NetworkSchema",
    "AssetSchema",
    "PortSchema",
    "SrcDstSchema",
    "ScheduleOnlySchema",
    "TagDataSchema",
    "IntrusionDetectionSchema",
]
