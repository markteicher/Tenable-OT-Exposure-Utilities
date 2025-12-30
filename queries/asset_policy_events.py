"""
queries/asset_policy_events.py

Tenable OT Security – Asset Policy Events (AssetPolicyEvent enum)

Source documentation:
https://docs.tenable.com/OT-security/api/assetpolicyevent.doc.html

Purpose:
- Enumerate all asset-level policy event types in Tenable OT
- Used to track policy-driven changes affecting assets
- Enables correlation between:
  - Asset lifecycle events
  - Policy enforcement
  - Configuration drift
  - Risk and compliance signals

AssetPolicyEvent represents *what changed* on an asset
as a direct result of a policy evaluation or enforcement.
"""

ASSET_POLICY_EVENTS = [
    "ASSET_CREATED",
    "ASSET_UPDATED",
    "ASSET_DELETED",
    "ASSET_REDISCOVERED",
    "ASSET_BECAME_ACTIVE",
    "ASSET_BECAME_INACTIVE",
    "ASSET_HIDDEN",
    "ASSET_UNHIDDEN",
    "ASSET_CRITICALITY_CHANGED",
    "ASSET_TYPE_CHANGED",
    "ASSET_PURDUE_LEVEL_CHANGED",
    "ASSET_ZONE_CHANGED",
    "ASSET_SITE_CHANGED",
    "ASSET_TAG_ADDED",
    "ASSET_TAG_REMOVED",
    "ASSET_GROUP_ADDED",
    "ASSET_GROUP_REMOVED",
]
