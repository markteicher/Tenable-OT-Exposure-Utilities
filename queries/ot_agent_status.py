"""
queries/ot_agent_status.py

Tenable OT Security – OtAgentStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/otagentstatus.doc.html

Purpose:
- Enumerates possible runtime and lifecycle states of an OT Agent
"""

OT_AGENT_STATUS_ENUM_NAME = "OtAgentStatus"

OT_AGENT_STATUS = [
    "PendingApproval",
    "Connected",
    "PreparingConnection",
    "WaitingForConnection",
    "PendingConfiguration",
    "Disconnected",
    "Scanning",
    "Updating",
    "ManuallyRegistered",
]
