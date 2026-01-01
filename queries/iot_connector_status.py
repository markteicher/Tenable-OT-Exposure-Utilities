"""
queries/iot_connector_status.py

Tenable OT Security – IotConnectorStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/iotconnectorstatus.doc.html

Purpose:
- Enumerates possible IoT connector statuses
"""

IOT_CONNECTOR_STATUS_ENUM_NAME = "IotConnectorStatus"

IOT_CONNECTOR_STATUSES = [
    "NotAvailable",
    "Connected",
    "Disconnected",
    "SecureModeFailure",
    "UnknownFailure",
]
