# interface/active_query.py
#
# Tenable OT Security – ActiveQuery GraphQL Interface
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/activequery.doc.html
#
# Purpose:
# - Defines the common fields for active (scheduled or triggered) queries

ACTIVE_QUERY_INTERFACE_NAME = "ActiveQuery"

ACTIVE_QUERY_FIELDS = [
    "id",
    "name",
    "description",
    "enabled",
    "trigger",
    "predefined",
    "category",
    "schedule",
    "operation",
    "assetGroup",
    "status",
    "lastExecution",
    "nextExecution",
    "createdBy",
    "lastEditedBy",
    "lastEditedDate",
    "lastRunBy",
    "usageInfo",
]
