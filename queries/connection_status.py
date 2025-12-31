"""
queries/connection_status.py

Tenable OT Security – ConnectionStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/connectionstatus.doc.html

Purpose:
- Represents the connection state of a component or asset
"""

CONNECTION_STATUS_ENUM_NAME = "ConnectionStatus"

CONNECTION_STATUSES = [
    "Connected",
    "Disconnected",
]
