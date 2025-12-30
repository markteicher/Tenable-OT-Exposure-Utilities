# -*- coding: utf-8 -*-
"""
queries/events.py

Tenable OT Security – Event GraphQL Queries

Covers:
- Events
- Event Policies (activity policy events / event policies)
- Action Types

Documentation source:
https://docs.tenable.com/OT-security/api/
"""

# ---------------------------------------------------------
# Events
# ---------------------------------------------------------

EVENTS_QUERY = """
query GetEvents(
  $filter: EventsExpressionsParams
  $search: String
  $sort: [EventsSortParams!]
  $first: Int
  $after: String
) {
  events(
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
      time
      type
      severity
      category
      resolved
      resolvedTs
      resolvedUser
      comment
      logId
      hitId
      completion
      continuous
      hasDetails
      payloadSize

      srcIP
      dstIP
      srcMac
      dstMac
      port
      protocol
      protocolRaw
      protocolNiceName

      eventType {
        type
        group
        description
        schema
        category
        family
        canCapture
        actions
        exclusion
      }

      policy {
        id
        index
        title
        level
        disabled
        archived
        schema
        continuous
        snapshot
        system
        key
        paused
        disableAfterHit

        aggregatedEventsCount {
          last24h
          last7d
          last30d
        }

        eventTypeDetails {
          type
          group
          description
          schema
          category
          family
          canCapture
          actions
          exclusion
        }

        actions {
          nodes {
            aid
            type
          }
        }

        exclusions {
          nodes {
            id
          }
        }

        srcAssetGroup {
          group { id }
          negate
        }
        dstAssetGroup {
          group { id }
          negate
        }
        schedule {
          group { id }
          negate
        }
        protocolGroup {
          group { id }
          negate
        }
        portGroup {
          group { id name }
          negate
        }
        tagGroup {
          group { id name }
          negate
        }
        valueGroup {
          group { id }
          negate
        }
        ruleGroup {
          group { id name }
          negate
        }
      }

      srcAssets {
        nodes { id name }
      }
      dstAssets {
        nodes { id name }
      }

      srcInterface {
        id
        firstSeen
        lastSeen
        mac
        family
        directAsset { id }
        ips {
          nodes { ip }
        }
        dnsNames {
          nodes
        }
      }

      dstInterface {
        id
        firstSeen
        lastSeen
        mac
        family
        directAsset { id }
        ips {
          nodes { ip }
        }
        dnsNames {
          nodes
        }
      }

      srcNames { nodes }
      dstNames { nodes }
    }
  }
}
"""

# ---------------------------------------------------------
# Event Policies (policy inventory – for exporting rules/config)
# ---------------------------------------------------------

EVENT_POLICIES_QUERY = """
query GetEventPolicies(
  $filter: ActivityPolicyEventExpressionsParams
  $search: String
  $sort: [ActivityPolicyEventSortParams!]
  $first: Int
  $after: String
) {
  activityPolicyEvents(
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
      index
      title
      level
      disabled
      archived
      schema
      continuous
      snapshot
      system
      key
      paused
      disableAfterHit

      aggregatedEventsCount {
        last24h
        last7d
        last30d
      }

      eventTypeDetails {
        type
        group
        description
        schema
        category
        family
        canCapture
        actions
        exclusion
      }

      actions {
        nodes {
          aid
          type
        }
      }

      exclusions {
        nodes {
          id
        }
      }

      srcAssetGroup {
        group { id }
        negate
      }
      dstAssetGroup {
        group { id }
        negate
      }
      schedule {
        group { id }
        negate
      }
      protocolGroup {
        group { id }
        negate
      }
      portGroup {
        group { id name }
        negate
      }
      tagGroup {
        group { id name }
        negate
      }
      valueGroup {
        group { id }
        negate
      }
      ruleGroup {
        group { id name }
        negate
      }
    }
  }
}
"""

# ---------------------------------------------------------
# Action Types
# ---------------------------------------------------------

ACTION_TYPES_QUERY = """
query GetActionTypes {
  actionTypes {
    nodes {
      id
      name
      description
    }
  }
}
"""
