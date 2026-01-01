"""
queries/event_group_type.py

Tenable OT Security – EventGroupType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/eventgrouptype.doc.html

Purpose:
- Enumerates event grouping types used across OT event queries
"""

EVENT_GROUP_TYPE_ENUM_NAME = "EventGroupType"

EVENT_GROUP_TYPES = [
    "Activity",
    "NetworkInterfaceEvent",
    "InactiveNetworkInterfaceEvent",
    "IDSSrcDstEvent",
    "SnapshotEvent",
    "NetworkEvent",
    "ControllerDetailsEvent",
    "ModuleDetailsEvent",
    "PortEvent",
    "IDSSrcEvent",
    "IDSGeneralEvent",
    "TagEvent",
    "IntrusionDetectionEvent",
    "PcEvent",
    "IEC104",
    "Dnp3Event",
    "MMSICCPEvent",
    "RediscoveredAssetEvent",
]
