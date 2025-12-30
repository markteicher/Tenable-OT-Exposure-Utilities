"""
queries/roles.py

Tenable OT Security – Roles GraphQL Queries

Source documentation:
https://docs.tenable.com/OT-security/api/role.doc.html

Purpose:
- Enumerate all roles (system + custom)
- Capture authorization boundaries
- Support access review and privilege analysis
"""

# ============================================================
# Roles
# ============================================================

ROLES_QUERY = """
query GetRoles {
  roles {
    nodes {
      id
      name
      description

      isSystem
      isReadOnly

      permissions
      scopes

      createdAt
      updatedAt
    }
  }
}
"""
