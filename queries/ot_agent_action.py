"""
queries/ot_agent_action.py

Tenable OT Security – OtAgentAction GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/otagentaction.doc.html

Purpose:
- Enumerates supported actions that can be executed on an OT Agent
"""

OT_AGENT_ACTION_ENUM_NAME = "OtAgentAction"

OT_AGENT_ACTIONS = [
    "LaunchScan",
    "AbortScan",
    "Update",
    "Approve",
]
