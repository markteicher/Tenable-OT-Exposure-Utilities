"""
queries/job_status.py

Tenable OT Security – JobStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/jobstatus.doc.html

Purpose:
- Represents execution status of background jobs in Tenable OT
"""

JOB_STATUS_ENUM_NAME = "JobStatus"

JOB_STATUS_VALUES = [
    "Pending",
    "Running",
    "Success",
    "Failure",
]
