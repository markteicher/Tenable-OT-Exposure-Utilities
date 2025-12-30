"""
queries/asset_relationship_fields.py

Tenable OT Security – Asset Relationship Fields (AssetRelationshipField enum)

Source documentation:
https://docs.tenable.com/OT-security/api/assetrelationshipfield.doc.html

Purpose:
- Enumerate all relationship fields used to describe how assets are connected
- Enables modeling of OT topology, dependencies, and communication paths
- Used by:
  - Asset relationship queries
  - Network / topology analysis
  - Purdue-level and zone-based dependency mapping

AssetRelationshipField defines *what aspect* of the relationship
is being evaluated between two OT assets.
"""

ASSET_RELATIONSHIP_FIELDS = [
    "SRC_ASSET_ID",
    "DST_ASSET_ID",
    "SRC_INTERFACE_ID",
    "DST_INTERFACE_ID",
    "SRC_IP",
    "DST_IP",
    "SRC_MAC",
    "DST_MAC",
    "PROTOCOL",
    "PORT",
    "VLAN",
    "ZONE",
    "PURDUE_LEVEL",
    "RELATIONSHIP_TYPE",
    "RELATIONSHIP_DIRECTION",
    "FIRST_SEEN",
    "LAST_SEEN",
]
