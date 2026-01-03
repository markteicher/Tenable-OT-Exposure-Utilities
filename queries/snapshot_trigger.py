# queries/snapshot_trigger.py
#
# Tenable OT Security – SnapshotTrigger GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/snapshottrigger.doc.html
#
# Purpose:
# - Defines what triggered a snapshot execution

SNAPSHOT_TRIGGER_ENUM_NAME = "SnapshotTrigger"

SNAPSHOT_TRIGGER = [
    "Passive",
    "Periodic",
    "UserInitiated",
    "EventTriggered",
    "AutoDiscovery",
]
