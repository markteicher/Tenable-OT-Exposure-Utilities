# queries/snapshot_status.py
#
# Tenable OT Security – SnapshotStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/snapshotstatus.doc.html
#
# Purpose:
# - Status values returned for snapshot execution results

SNAPSHOT_STATUS_ENUM_NAME = "SnapshotStatus"

SNAPSHOT_STATUS = [
    "NoRoutesForClient",
    "InternalError",
    "DnsError",
    "HostUnreachableError",
    "TimeoutError",
    "NetworkError",
    "ProtocolError",
    "AuthenticationError",
    "LimitExceededError",
    "OpAllowedOnce",
    "NoPotentialClients",
    "NoAllowedClients",
    "EmptyClientResponseError",
    "MultipleErrors",
]
