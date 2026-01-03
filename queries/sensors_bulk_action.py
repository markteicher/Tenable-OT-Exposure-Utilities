# queries/sensors_bulk_action.py
#
# Tenable OT Security – SensorsBulkAction GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/sensorsbulkaction.doc.html
#
# Purpose:
# - Actions that can be applied in bulk to sensors

SENSORS_BULK_ACTION_ENUM_NAME = "SensorsBulkAction"

SENSORS_BULK_ACTION = [
    "Pause",
    "Resume",
    "EnableActive",
    "DisableActive",
    "Update",
]
