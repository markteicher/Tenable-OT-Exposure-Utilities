# queries/status_type.py
#
# Tenable OT Security – StatusType GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/statustype.doc.html
#
# Purpose:
# - Generic enabled/disabled lifecycle status used by system objects

STATUS_TYPE_ENUM_NAME = "StatusType"

STATUS_TYPE = [
    "Uninitialized",
    "Enabled",
    "Disabled",
    "InvalidStatus",
]
