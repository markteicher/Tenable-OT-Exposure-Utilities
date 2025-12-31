"""
queries/asset_source_types.py

Tenable OT Security – Asset Source Types (AssetSourceType) GraphQL Queries

Source documentation:
https://docs.tenable.com/OT-security/api/assetsourcetype.doc.html

Purpose:
- Enumerate all asset source types used by Tenable OT (where an asset record originated)
- Useful for asset provenance filtering, reporting, and validation (Sensor vs CSV vs Nessus, etc.)
"""

# ---------------------------------------------------------------------
# Documented Enum Values (Authoritative List)
# ---------------------------------------------------------------------
# Source: AssetSourceType schema definition page
# Values:
# Unknown, Sensor, Local, Csv, Pcap, Nessus, ActiveOt, IotConnector,
# UserDefined, ErSpan, Scd, OtAgent, NetworkMapper, ProjectFile
# ---------------------------------------------------------------------

ASSET_SOURCE_TYPE_VALUES = [
    "Unknown",
    "Sensor",
    "Local",
    "Csv",
    "Pcap",
    "Nessus",
    "ActiveOt",
    "IotConnector",
    "UserDefined",
    "ErSpan",
    "Scd",
    "OtAgent",
    "NetworkMapper",
    "ProjectFile",
]

# ---------------------------------------------------------------------
# Optional Introspection Query (if introspection is enabled in your OT instance)
# ---------------------------------------------------------------------

ASSET_SOURCE_TYPES_QUERY = """
query AssetSourceTypes {
  __type(name: "AssetSourceType") {
    name
    enumValues {
      name
      description
    }
  }
}
""".strip()
