# queries/removable_flags.py
#
# Tenable OT Security – RemovableFlags GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/removableflags.doc.html
#
# Purpose:
# - Flags that can be removed by a user

REMOVABLE_FLAGS_ENUM_NAME = "RemovableFlags"

REMOVABLE_FLAGS = [
    "AssetsPendingDeletion",
    "SensorPendingApproval",
    "OtAgentPendingApproval",
    "SoftLimit",
    "SensorUpdatesAvailable",
    "IcpPairingRequestPendingApproval",
    "WaitingForEmCertApproval",
    "SensorAwaitingFirstUse",
]
