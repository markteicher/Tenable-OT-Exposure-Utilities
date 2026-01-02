# queries/relationship_type.py
#
# Tenable OT Security – RelationshipType GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/relationshiptype.doc.html
#
# Purpose:
# - Defines the type of relationship between OT assets

RELATIONSHIP_TYPE_ENUM_NAME = "RelationshipType"

RELATIONSHIP_TYPES = [
    "Nesting",
    "IoTConnectors",
    "BACnet",
    "SnmpCrawler",
    "AgentGateway",
    "ProjectFile",
]
