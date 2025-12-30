"""
queries/plugin_details.py

Tenable OT Security – Plugin Details GraphQL Queries

Source documentation:
- PluginDetail: https://docs.tenable.com/OT-security/api/plugindetail.doc.html
- Query root:   https://docs.tenable.com/OT-security/api/query.doc.html
- Plugin:       https://docs.tenable.com/OT-security/api/plugin.doc.html

Purpose:
- Export full plugin details for vulnerability intelligence enrichment.
- Supports:
  1) Fetch details via plugin(id) -> details
  2) Fetch details inline when available on plugins().nodes.details (heavier)

Notes:
- Keep outputs full-fidelity for JSON/CSV exporters.
"""

# ============================================================
# Plugin Details (By Plugin ID) — Preferred
# ============================================================

PLUGIN_DETAILS_BY_ID_QUERY = """
query GetPluginDetailsById($id: ID!) {
  plugin(id: $id) {
    id
    name
    source
    family
    severity
    vprScore
    comment
    owner
    totalAffectedAssets
    details {
      id
      name
      source
      family
      description
      solution
      seeAlso
      pluginType
      pluginPubDate
      pluginModDate
      vulnPubDate
      vulnModDate
      refs {
        name
        value
        url
      }
      cpe
      cvssVector
      cvssV3Vector
      cvssBaseScore
      cvssV3BaseScore
      cvssTemporalScore
      cvssV3TemporalScore
      cvssTemporalVector
      cvssV3TemporalVector
      cvssImpactScore
    }
  }
}
"""

# ============================================================
# Plugin Details Inline (Paged Plugins + Details) — Heaviest
# Use only if OT API exposes plugins.nodes.details
# ============================================================

PLUGINS_WITH_DETAILS_QUERY = """
query GetPluginsWithDetails($first: Int!, $after: String) {
  plugins(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      name
      source
      family
      severity
      vprScore
      comment
      owner
      totalAffectedAssets
      details {
        id
        name
        source
        family
        description
        solution
        seeAlso
        pluginType
        pluginPubDate
        pluginModDate
        vulnPubDate
        vulnModDate
        refs {
          name
          value
          url
        }
        cpe
        cvssVector
        cvssV3Vector
        cvssBaseScore
        cvssV3BaseScore
        cvssTemporalScore
        cvssV3TemporalScore
        cvssTemporalVector
        cvssV3TemporalVector
        cvssImpactScore
      }
    }
  }
}
"""
