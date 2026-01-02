# queries/query_trigger.py
#
# Tenable OT Security – QueryTrigger GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/querytrigger.doc.html
#
# Purpose:
# - Defines how a query execution is triggered

QUERY_TRIGGER_ENUM_NAME = "QueryTrigger"

QUERY_TRIGGERS = [
    "Manual",
    "Periodic",
    "System",
]
