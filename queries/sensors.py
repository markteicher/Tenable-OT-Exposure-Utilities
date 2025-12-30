# -*- coding: utf-8 -*-
"""
queries/sensors.py

Tenable OT Security – Sensor & Appliance GraphQL Queries

Covers:
- Sensor Status
- ICP Sensor Fields
- Core OS Versions (ICP / EM appliance platform details)

Documentation sources:
- https://docs.tenable.com/OT-security/api/sensorstatus.doc.html
- https://docs.tenable.com/OT-security/api/icpsensorfield.doc.html
- https://docs.tenable.com/OT-security/api/coreosversion.doc.html
"""

# ---------------------------------------------------------
# Sensor Status (ICP / EM health & connectivity)
# ---------------------------------------------------------

SENSOR_STATUS_QUERY = """
query GetSensorStatus {
  sensorStatus {
    nodes {
      id
      name
      type
      status
      lastSeen
      firstSeen
      ip
      hostname
      version
      build
      uptime
      cpuUsage
      memoryUsage
      diskUsage
      packetsPerSecond
      eventsPerSecond
      droppedPackets
      captureEnabled
      healthy
      warning
      error
    }
  }
}
"""

# ---------------------------------------------------------
# ICP Sensor Fields (what each sensor can observe / collect)
# ---------------------------------------------------------

ICP_SENSOR_FIELDS_QUERY = """
query GetIcpSensorFields {
  icpSensorFields {
    nodes {
      id
      name
      description
      category
      fieldType
      dataType
      required
      supported
      deprecated
    }
  }
}
"""

# ---------------------------------------------------------
# Core OS Versions
# Used to determine appliance platform (physical vs virtual)
# ---------------------------------------------------------

CORE_OS_VERSIONS_QUERY = """
query GetCoreOsVersions {
  coreOsVersions {
    nodes {
      id
      name
      version
      build
      architecture
      platform
      virtualized
      supported
      endOfLife
    }
  }
}
"""
