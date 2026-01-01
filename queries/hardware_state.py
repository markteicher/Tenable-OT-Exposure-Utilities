"""
queries/hardware_state.py

Tenable OT Security – HardwareState GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/hardwarestate.doc.html

Purpose:
- Enumerates hardware lifecycle states for assets
"""

HARDWARE_STATE_ENUM_NAME = "HardwareState"

HARDWARE_STATES = [
    "UnknownState",
    "Active",
    "EndOfLife",
    "Discontinued",
]
