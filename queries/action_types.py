"""
queries/action_types.py

Tenable OT Security – Action Types GraphQL Queries

Source documentation:
https://docs.tenable.com/OT-security/api/actiontype.doc.html

Purpose:
- Enumerate all action types supported by Tenable OT
- Used by event policies, response workflows, and audit analysis
- Enables mapping: Event → Policy → Action
"""

# ============================================================
# Action Types
# ============================================================

ACTION_TYPES_QUERY = """
query GetActionTypes {
  actionTypes {
    nodes {
      id
      name
      description

      category
      isSystem

      createdAt
      updatedAt
    }
  }
}
"""
