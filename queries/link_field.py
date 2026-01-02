"""
queries/link_field.py

Tenable OT Security – LinkField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/linkfield.doc.html

Purpose:
- Enumerates selectable fields for Link queries
"""

LINK_FIELD_ENUM_NAME = "LinkField"

LINK_FIELDS = [
    "id",
    "asset1",
    "asset2",
    "protocols",
    "traffic",
    "convCount",
    "lastConv",
    "firstConv",
    "ports",
    "name",
    "firstSeen",
    "lastSeen",
    "lastHit",
    "lastSnapshot",
    "macs",
    "ips",
    "segments",
    "segmentsIds",
    "subnets",
    "type",
    "superType",
    "category",
    "purdueLevel",
    "vendor",
    "runStatus",
    "extendedRunStatus",
    "runStatusTime",
    "location",
    "description",
    "os",
    "family",
    "model",
    "firmwareVersion",
    "serial",
    "slot",
    "hardwareState",
    "lifecycleStatus",
    "discontinuedDate",
    "replacementProduct",
    "backplane",
    "backplaneName",
    "risk",
    "criticality",
    "hidden",
    "lastUpdate",
    "sources",
    "tags",
    "customField1",
    "customField2",
    "customField3",
    "customField4",
    "customField5",
    "customField6",
    "customField7",
    "customField8",
    "customField9",
    "customField10",
]
