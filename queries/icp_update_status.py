"""
queries/icp_update_status.py

Tenable OT Security – IcpUpdateStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icpupdatestatus.doc.html

Purpose:
- Enumerates update status values for ICP update operations
"""

ICP_UPDATE_STATUS_ENUM_NAME = "IcpUpdateStatus"

ICP_UPDATE_STATUSES = [
    "Unknown",
    "Failed",
    "Updating",
    "Success",
]
