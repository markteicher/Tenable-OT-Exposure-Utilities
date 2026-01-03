# queries/sensor_active_status.py
#
# Tenable OT Security – SensorActiveStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/sensoractivestatus.doc.html
#
# Purpose:
# - Represents the current active status of a sensor

SENSOR_ACTIVE_STATUS_ENUM_NAME = "SensorActiveStatus"

SENSOR_ACTIVE_STATUS = [
    "Enabled",
    "Disabled",
    "NotAvailable",
]
