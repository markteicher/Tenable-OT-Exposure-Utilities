# queries/user_scan_status.py
#
# Tenable OT Security – UserScanStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/userscanstatus.doc.html
#
# Purpose:
# - Represents the lifecycle and state of a user-initiated scan

USER_SCAN_STATUS_ENUM_NAME = "UserScanStatus"

USER_SCAN_STATUS = [
    "UnknownScanStatus",
    "EmptyScanStatus",
    "InitializingScanStatus",
    "ProcessingScanStatus",
    "CompletedScanStatus",
    "AbortedScanStatus",
    "ImportedScanStatus",
    "PendingScanStatus",
    "RunningScanStatus",
    "ResumingScanStatus",
    "CancelingScanStatus",
    "CanceledScanStatus",
    "PausingScanStatus",
    "PausedScanStatus",
    "QueuedScanStatus",
    "StoppingScanStatus",
    "StoppedScanStatus",
    "KillingScanStatus",
]
