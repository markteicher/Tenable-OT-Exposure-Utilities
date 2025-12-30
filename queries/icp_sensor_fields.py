"""
queries/icp_sensor_fields.py

Tenable OT Security – ICP Sensor Fields

Docs:
- https://docs.tenable.com/OT-security/api/icpsensorfield.doc.html
- https://docs.tenable.com/OT-security/api/query.doc.html

Purpose:
- Enumerate all ICP sensor fields
- Used to understand what telemetry, attributes, and measurements
  ICP sensors are capable of emitting
- Foundational for validation, schema mapping, and export tooling
"""

# ============================================================
# All ICP Sensor Fields (Paged)
# ============================================================

ICP_SENSOR_FIELDS_QUERY = """
query GetIcpSensorFields($first: Int!, $after: String) {
  icpSensorFields(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      name
      key
      description

      category
      fieldType
      dataType
      unit

      required
      searchable
      filterable
      sortable

      minValue
      maxValue
      allowedValues

      deprecated
      deprecatedReason

      createdAt
      updatedAt
    }
  }
}
"""

# ============================================================
# ICP Sensor Field by ID (Deep Inspection)
# ============================================================

ICP_SENSOR_FIELD_BY_ID_QUERY = """
query GetIcpSensorFieldById($id: ID!) {
  icpSensorFieldById(id: $id) {
    id
    name
    key
    description

    category
    fieldType
    dataType
    unit

    required
    searchable
    filterable
    sortable

    minValue
    maxValue
    allowedValues

    deprecated
    deprecatedReason

    createdAt
    updatedAt
  }
}
"""
