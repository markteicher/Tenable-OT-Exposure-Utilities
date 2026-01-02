# queries/selection_status.py
#
# Tenable OT Security – SelectionStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/selectionstatus.doc.html
#
# Purpose:
# - Represents the enablement state of a selection across plugins or families

SELECTION_STATUS_ENUM_NAME = "SelectionStatus"

SELECTION_STATUS = [
    "Enabled",
    "Disabled",
    "Mixed",
]
