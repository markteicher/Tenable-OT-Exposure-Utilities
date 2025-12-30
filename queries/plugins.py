"""
queries/plugins.py

Tenable OT Security – Plugins + Plugin Details GraphQL Queries

Source documentation:
- Plugin:  https://docs.tenable.com/OT-security/api/plugin.doc.html
- PluginDetail: https://docs.tenable.com/OT-security/api/plugindetail.doc.html

Purpose:
- Export plugin inventory from Tenable OT (id, name, family, severity, scoring, etc.)
- Export full plugin details (description, solution, references, CVSS, CPE, dates, etc.)
- Cursor-based pagination supported (first/after)

Notes:
- Keep outputs "full-fidelity" for downstream JSON/CSV exporters.
- Do NOT assume fields beyond what the OT GraphQL docs expose.
"""

# ============================================================
# Plugins (Paged)
# ============================================================

PLUGINS_QUERY = """
query GetPlugins($first: Int!, $after: String) {
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
    }
  }
}
"""

# ============================================================
# Plugins With Affected Assets (Optional / Heavier)
# ============================================================

PLUGINS_WITH_AFFECTED_ASSETS_QUERY = """
query GetPluginsWithAffectedAssets($first: Int!, $after: String) {
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
      affectedAssets {
        nodes {
          id
          name
        }
      }
    }
  }
}
"""

# ============================================================
# Plugin Details (By Plugin ID)
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
# Plugin Details (Paged Plugins + Details Inline) — Heaviest
# Use only if OT API supports details inline under plugins.nodes.details
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
