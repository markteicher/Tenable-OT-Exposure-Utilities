"""
queries/log_record_field.py

Tenable OT Security – LogRecordField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/logrecordfield.doc.html

Purpose:
- Enumerates selectable fields for system log records
"""

LOG_RECORD_FIELD_ENUM_NAME = "LogRecordField"

LOG_RECORD_FIELDS = [
    "id",
    "timestamp",
    "message",
    "userName",
]
