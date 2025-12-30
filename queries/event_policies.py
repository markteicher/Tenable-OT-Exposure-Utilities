"""
queries/event_policies.py

Tenable OT Security – Event Policies GraphQL Queries

Source documentation:
https://docs.tenable.com/OT-security/api/eventpolicy.doc.html

Purpose:
- Enumerate all event policies configured in Tenable OT
- Capture policy logic, scope, actions, and enforcement state
- Enables audit, governance, and response analysis
"""

# ============================================================
# Event Policies
# ============================================================

EVENT_POLICIES_QUERY = """
query GetEventPolicies {
  eventPolicies {
    nodes {
      id
      name
      description

      enabled
      archived
      system

      severity
      category

      continuous
      snapshot

      disableAfterHit
      paused

      createdAt
      updatedAt

      eventType {
        id
        type
        group
        description
        category
        family
        canCapture
      }

      actions {
        nodes {
          id
          type {
            id
            name
            description
            category
            isSystem
          }
        }
      }

      srcAssetGroup {
        group {
          id
          name
        }
        negate
      }

      dstAssetGroup {
        group {
          id
          name
        }
        negate
      }

      protocolGroup {
        group {
          id
          name
        }
        negate
      }

      portGroup {
        group {
          id
          name
        }
        negate
      }

      tagGroup {
        group {
          id
          name
        }
        negate
      }

      ruleGroup {
        group {
          id
          name
        }
        negate
      }

      exclusions {
        nodes {
          id
        }
      }

      aggregatedEventsCount {
        last24h
        last7d
        last30d
      }
    }
  }
}
"""
