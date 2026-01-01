"""
queries/event_status.py

Tenable OT Security – EventStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/eventstatus.doc.html

Purpose:
- Represents execution / completion status of OT events
"""

EVENT_STATUS_ENUM_NAME = "EventStatus"

EVENT_STATUSES = [
    "CompletionUnknown",
    "CompletionSuccess",
    "CompletionError",
    "CompletionTimeout",
    "CompletionUnexpectedTermination",
]
