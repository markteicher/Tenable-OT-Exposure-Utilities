"""
queries/em_pairing_status.py

Tenable OT Security – EmPairingStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/empairingstatus.doc.html

Purpose:
- Enumerates EM ↔ ICP pairing lifecycle states
"""

EM_PAIRING_STATUS_ENUM_NAME = "EmPairingStatus"

EM_PAIRING_STATUS = [
    "IcpPendingApproval",
    "PreparingConnection",
    "WaitingForIcpConnection",
    "IcpConnected",
    "IcpDisconnected",
]
