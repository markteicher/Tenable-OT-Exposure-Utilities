# queries/updatable_status.py
#
# Tenable OT Security – UpdatableStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/updatablestatus.doc.html
#
# Purpose:
# - Indicates whether a device or component can be updated

UPDATABLE_STATUS_ENUM_NAME = "UpdatableStatus"

UPDATABLE_STATUS = [
    "Undetermined",
    "Updatable",
    "NonUpdatable",
]
