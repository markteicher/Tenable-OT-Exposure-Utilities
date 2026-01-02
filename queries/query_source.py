# queries/query_source.py
#
# Tenable OT Security – QuerySource GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/querysource.doc.html
#
# Purpose:
# - Identifies how a query was initiated or triggered

QUERY_SOURCE_ENUM_NAME = "QuerySource"

QUERY_SOURCES = [
    "Passive",
    "Periodic",
    "UserInitiated",
    "EventTriggered",
    "AutoDiscovery",
]
