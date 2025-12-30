"""
queries/sensor_status.py

Tenable OT Security – Sensor Status GraphQL Queries

Source documentation:
- SensorStatus: https://docs.tenable.com/OT-security/api/sensorstatus.doc.html
- Query root:   https://docs.tenable.com/OT-security/api/query.doc.html

Purpose:
- Export operational health and status of OT sensors (ICP / EM).
- Capture connectivity, last-seen times, versioning, and runtime state.
- Full-fidelity fields for JSON/CSV exporters (no opinionated pruning).

Notes:
- Sensor status is critical for validating coverage and data freshness.
- Use pagination when querying lists.
"""

# ============================================================
# All Sensor Status (Paged)
# ============================================================

SENSOR_STATUS_QUERY = """
query GetSensorStatus($first: Int!, $after: String) {
  sensorStatus(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      name
      type
      status
      state
      connected
      lastSeen
      lastSeenRaw
      firstSeen
      enabled
      version
      build
      uptime
      heartbeat
      error
      location
      site
      tags {
        nodes {
          id
          name
        }
      }
      interfaces {
        nodes {
          id
          name
          mac
          ips {
            nodes {
              ip
            }
          }
        }
      }
    }
  }
}
"""

# ============================================================
# Sensor Status by ID (Targeted / Drill-down)
# ============================================================

SENSOR_STATUS_BY_ID_QUERY = """
query GetSensorStatusById($id: ID!) {
  sensorStatusById(id: $id) {
    id
    name
    type
    status
    state
    connected
    lastSeen
    lastSeenRaw
    firstSeen
    enabled
    version
    build
    uptime
    heartbeat
    error
    location
    site
    tags {
      nodes {
        id
        name
      }
    }
    interfaces {
      nodes {
        id
        name
        mac
        ips {
          nodes {
            ip
          }
        }
      }
    }
  }
}
"""
