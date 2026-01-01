"""
queries/error_key.py

Tenable OT Security – ErrorKey GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/errorkey.doc.html

Purpose:
- Enumerates contextual keys used to describe errors returned by the OT Security GraphQL API
"""

ERROR_KEY_ENUM_NAME = "ErrorKey"

ERROR_KEY_VALUES = [
    "Protocol",
    "Operation",
    "Ip",
    "IcpId",
    "IcpUpdateSuccessCount",
    "IcpUpdateFailedCount",
    "OtAgentId",
    "Name",
    "Status",
    "FeedType",
]
