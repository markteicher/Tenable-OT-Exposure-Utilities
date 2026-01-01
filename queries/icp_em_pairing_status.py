"""
queries/icp_em_pairing_status.py

Tenable OT Security – IcpEmPairingStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icpempairingstatus.doc.html

Purpose:
- Enumerates ICP-EM pairing and connection states
"""

ICP_EM_PAIRING_STATUS_ENUM_NAME = "IcpEmPairingStatus"

ICP_EM_PAIRING_STATUSES = [
    "NoPairing",
    "TryingToConnect",
    "WaitingForCertificateApproval",
    "PendingEmApproval",
    "CertificateMismatchError",
    "HostUnreachableError",
    "BadCredentialsError",
    "InternalServerError",
    "CantGetTargetVersionError",
    "UnsupportedTargetVersionError",
    "Connected",
    "DisconnectedError",
]
