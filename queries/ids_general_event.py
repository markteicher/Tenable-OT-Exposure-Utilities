"""
queries/ids_general_event.py

Tenable OT Security – IDSGeneralEvent GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/idsgeneralevent.doc.html

Purpose:
- Enumerates possible events for IDS General policies
"""

IDS_GENERAL_EVENT_ENUM_NAME = "IDSGeneralEvent"

IDS_GENERAL_EVENTS = [
    "IpConflict",
    "DataSpikeDetected",
    "ConversationCountSpikeDetected",
]
