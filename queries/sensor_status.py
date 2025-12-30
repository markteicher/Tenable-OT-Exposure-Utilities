"""
queries/sensor_status.py

Tenable OT Security – Sensor Status GraphQL Queries

Docs:
- https://docs.tenable.com/OT-security/api/sensorstatus.doc.html
- https://docs.tenable.com/OT-security/api/query.doc.html

Purpose:
- Export full operational health of ICP / EM sensors
- Capture connectivity, versioning, and runtime resource utilization
- Designed for JSON / CSV export without lossy pruning
"""

# ============================================================
# All Sensor Status (Paged, Full Telemetry)
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
      enabled

      firstSeen
      lastSeen
      lastSeenRaw

      version
      build
      uptime
      heartbeat

      # ============================
      # Resource Utilization
      # ============================
      cpuUsage
      memoryUsage
      diskUsage

      # ============================
      # Queue / Processing Health
      # ============================
      eventQueueSize
      packetQueueSize
      droppedPackets

      # ============================
      # Error / Health Indicators
      # ============================
      error
      warnings
      healthScore

      # ============================
      # Location / Metadata
      # ============================
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
# Sensor Status by ID (Deep Drill-Down)
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
    enabled

    firstSeen
    lastSeen
    lastSeenRaw

    version
    build
    uptime
    heartbeat

    cpuUsage
    memoryUsage
    diskUsage

    eventQueueSize
    packetQueueSize
    droppedPackets

    error
    warnings
    healthScore

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
