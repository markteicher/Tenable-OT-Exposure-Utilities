# queries/run_status.py
#
# Tenable OT Security – RunStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/runstatus.doc.html
#
# Purpose:
# - Represents the operational status of a run

RUN_STATUS_ENUM_NAME = "RunStatus"

RUN_STATUS = [
    "Unknown",
    "NoConfig",
    "Running",
    "Stopped",
    "Fault",
    "Test",
    "Backup",
    "Alert",
]
