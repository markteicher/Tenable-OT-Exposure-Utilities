"""
queries/asset_group_types.py

Tenable OT Security – Asset Group Types (AssetGroupType enum)

Source documentation:
https://docs.tenable.com/OT-security/api/assetgrouptype.doc.html

Purpose:
- Enumerate all supported AssetGroupType values in Tenable OT
- Used to classify how assets are grouped and scoped
- Drives:
  - Asset inventory segmentation
  - Policy targeting
  - Event correlation
  - Reporting and filtering logic

Notes:
- AssetGroupType defines *how* an asset group is constructed
- These types are referenced by:
  - Asset groups
  - Policies
  - Queries and filters
"""

ASSET_GROUP_TYPES = [
    "STATIC",
    "DYNAMIC",
    "SYSTEM",
    "DISCOVERY",
    "NETWORK",
    "SEGMENT",
    "ZONE",
    "SITE",
]
