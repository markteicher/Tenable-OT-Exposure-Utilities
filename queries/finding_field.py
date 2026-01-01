"""
queries/finding_field.py

Tenable OT Security – findingField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/findingfield.doc.html

Purpose:
- Enumerates fields usable for finding-based queries, filters, and aggregations
"""

FINDING_FIELD_ENUM_NAME = "findingField"

FINDING_FIELDS = [
    "findingId",
    "findingPort",
    "findingProtocol",
    "findingSvcName",
    "findingStatus",
    "findingFirstHit",
    "findingLastHit",
    "findingFixedAt",
    "findingOutput",

    "pluginId",
    "pluginSource",
    "pluginFamily",
    "pluginName",
    "pluginSeverity",
    "pluginVprScore",
    "pluginVprLevel",
    "pluginModificationDate",
    "pluginComment",
    "pluginOwner",
    "pluginCvss3Score",

    "assetId",
    "assetName",
    "assetFirstSeen",
    "assetLastSeen",
    "assetLastHit",
    "assetLastSnapshot",
    "assetMacs",
    "assetIps",
    "assetSegments",
    "assetSegmentsIds",
    "assetSubnets",
    "assetType",
    "assetSuperType",
    "assetCategory",
    "assetPurdueLevel",
    "assetVendor",
    "assetRunStatus",
    "assetExtendedRunStatus",
    "assetRunStatusTime",
    "assetLocation",
    "assetDescription",
    "assetOs",
    "assetFamily",
    "assetModel",
    "assetFirmwareVersion",
    "assetSerial",
    "assetSlot",
    "assetHardwareState",
    "assetLifecycleStatus",
    "assetDiscontinuedDate",
    "assetReplacementProduct",
    "assetBackplane",
    "assetBackplaneName",
    "assetRisk",
    "assetCriticality",
    "assetHidden",
    "assetLastUpdate",
    "assetSources",
    "assetTags",
    "assetCustomField1",
    "assetCustomField2",
    "assetCustomField3",
    "assetCustomField4",
    "assetCustomField5",
    "assetCustomField6",
    "assetCustomField7",
    "assetCustomField8",
    "assetCustomField9",
    "assetCustomField10",
]
