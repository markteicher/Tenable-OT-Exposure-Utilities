"""
queries/iot_connector_type.py

Tenable OT Security – IotConnectorType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/iotconnectortype.doc.html

Purpose:
- Enumerates supported IoT connector types
"""

IOT_CONNECTOR_TYPE_ENUM_NAME = "IotConnectorType"

IOT_CONNECTOR_TYPES = [
    "Exacq",
    "MobotixCamera",
    "Agent",
    "Milestone",
    "Genetec",
]
