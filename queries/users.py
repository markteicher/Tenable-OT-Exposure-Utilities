# -*- coding: utf-8 -*-
"""
queries/users.py

Tenable OT Security – Users & System Logs GraphQL Queries

Covers:
- Users (local + directory-backed)
- System Logs (audit / operational logs)

Documentation sources:
- https://docs.tenable.com/OT-security/api/user.doc.html
- https://docs.tenable.com/OT-security/api/query.doc.html
"""

# ---------------------------------------------------------
# Users
# ---------------------------------------------------------

USERS_QUERY = """
query GetUsers($first: Int!, $after: String) {
  users(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      username
      displayName
      email
      role
      enabled
      lastLogin
      createdAt
      authType
      groups {
        nodes {
          id
          name
        }
      }
    }
  }
}
"""

# ---------------------------------------------------------
# System Logs (Audit / Operational)
# ---------------------------------------------------------

SYSTEM_LOGS_QUERY = """
query GetSystemLogs($first: Int!, $after: String) {
  systemLogs(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      id
      timeStamp
      severity
      message
      userName
      source
      category
      details
    }
  }
}
"""
