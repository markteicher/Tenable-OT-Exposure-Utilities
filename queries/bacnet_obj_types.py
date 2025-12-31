"""
queries/bacnet_obj_types.py

Tenable OT Security – BACnet Object Types (ENUM)

Source documentation:
https://docs.tenable.com/OT-security/api/bacnetobjtype.doc.html

Purpose:
- Enumerates all BACnet object types recognized by Tenable OT
- Used when modeling BACnet assets, device capabilities, and object-level telemetry
- Supports asset classification, protocol analysis, and export workflows

Notes:
- This file is a direct transcription of the GraphQL enum
- Values must remain authoritative and unchanged
"""

BACNET_OBJ_TYPES = [
    "AnalogInputObject",
    "AnalogOutputObject",
    "DeviceObject",
]
