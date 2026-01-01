"""
queries/icp_sensor_field.py

Tenable OT Security – IcpSensorField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icpsensorfield.doc.html

Purpose:
- Enumerates selectable fields for ICP sensor objects
"""

ICP_SENSOR_FIELD_ENUM_NAME = "IcpSensorField"

ICP_SENSOR_FIELDS = [
    "id",
    "ip",
    "natIp",
    "externalIp",
    "internalIp",
    "name",
    "version",
    "osVersion",
    "systemUpdatesExist",
    "stockdogUpdateExists",
    "updatableSensor",
    "lastCheckForUpdates",
    "approved",
    "tunnelStatus",
    "connectionStatus",
    "statusTs",
    "error",
    "errorTs",
    "active",
    "updatingStatus",
    "baseName",
    "origin",
    "awaitingFirstUse",
    "bps",
    "shortVersion",
    "status",
    "site",
]
