# interface/asset_group.py
#
# Tenable OT Security – AssetGroup GraphQL Interface
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/assetgroup.doc.html
#
# Purpose:
# - Defines the common fields and relationships for asset groups

ASSET_GROUP_INTERFACE_NAME = "AssetGroup"

ASSET_GROUP_FIELDS = [
    "id",
    "name",
    "type",
    "archived",
    "system",
    "key",
    "lastModifiedDate",
    "lastModifiedBy",
    "displayTag",
    "isStaticType",
    "filter",
    "policies",
    "queries",
    "zones",
    "usedInRestrictions",
    "usageInfo",
]
