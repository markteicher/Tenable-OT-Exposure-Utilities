# -*- coding: utf-8 -*-
"""
queries/assets.py

Tenable OT Security – Asset GraphQL Queries

Covers:
- Assets
- Asset Fields
- Asset Types
- Asset Categories

Documentation source:
https://docs.tenable.com/OT-security/api/
"""

# ---------------------------------------------------------
# Assets
# ---------------------------------------------------------

ASSETS_QUERY = """
query GetAssets(
  $filter: AssetExpressionsParams
  $search: String
  $sort: [AssetSortParams!]
  $first: Int
  $after: String
) {
  assets(
    filter: $filter
    search: $search
    sort: $sort
    first: $first
    after: $after
  ) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      name
      category
      type
      superType
      vendor
      model
      serial
      firmwareVersion
      criticality
      purdueLevel
      role
      safetyRated
      hidden

      firstSeen
      lastSeen
      lastUpdate

      ips {
        nodes
      }
      macs {
        nodes
      }

      os
      osDetails {
        name
        version
        architecture
      }

      runStatus
      runStatusTime

      location
      family
      description

      risk {
        totalRisk
        unresolvedEvents
      }

      segments {
        nodes {
          id
          name
          type
          key
          vlan
          subnet
          description
          systemName
          assetType
        }
      }

      revisions {
        nodes {
          id
          ordinal
          firstSeen
          lastSeen
          isBase
        }
      }
    }
  }
}
"""

# ---------------------------------------------------------
# Asset Fields
# ---------------------------------------------------------

ASSET_FIELDS_QUERY = """
query GetAssetFields {
  assetFields {
    nodes {
      key
      name
      description
      type
      searchable
      sortable
      filterable
    }
  }
}
"""

# ---------------------------------------------------------
# Asset Types
# ---------------------------------------------------------

ASSET_TYPES_QUERY = """
query GetAssetTypes {
  assetTypes {
    nodes {
      id
      name
      superType
      description
      family
      category
    }
  }
}
"""

# ---------------------------------------------------------
# Asset Categories
# ---------------------------------------------------------

ASSET_CATEGORIES_QUERY = """
query GetAssetCategories {
  assetCategories {
    nodes {
      id
      name
      description
    }
  }
}
"""
