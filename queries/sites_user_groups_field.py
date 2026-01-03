# queries/sites_user_groups_field.py
#
# Tenable OT Security – SitesUserGroupsField GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/sitesusergroupsfield.doc.html
#
# Purpose:
# - Sortable / selectable fields for site ↔ user group relationships

SITES_USER_GROUPS_FIELD_ENUM_NAME = "SitesUserGroupsField"

SITES_USER_GROUPS_FIELD = [
    "id",
    "siteId",
    "siteName",
    "userGroupId",
    "userGroupName",
    "rolesNames",
    "zonesNames",
    "system",
    "status",
]
