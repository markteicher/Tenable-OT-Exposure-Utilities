# queries/query_status.py
#
# Tenable OT Security – QueryStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/querystatus.doc.html
#
# Purpose:
# - Represents the lifecycle state of a query execution

QUERY_STATUS_ENUM_NAME = "QueryStatus"

QUERY_STATUSES = [
    "Unknown",
    "Created",
    "Ongoing",
    "Preparing",
    "Completed",
    "Failed",
]
