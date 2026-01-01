"""
queries/error_category.py

Tenable OT Security – ErrorCategory GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/errorcategory.doc.html

Purpose:
- Enumerates error categories returned by the OT Security GraphQL API
"""

ERROR_CATEGORY_ENUM_NAME = "ErrorCategory"

ERROR_CATEGORY_VALUES = [
    "InternalError",
    "AuthenticationError",
    "DnsError",
    "HostUnreachableError",
    "TimeoutError",
    "NetworkError",
    "LimitExceededError",
    "ServiceUnavailable",
    "Disconnected",
    "AlreadyInProgress",
    "ProtocolError",
    "EmptyClientResponseError",
    "NoPotentialClients",
    "NoAllowedClients",
    "NoRoutesForClient",
    "WrongCertificate",
    "MissingFormFields",
    "IpNotAllowed",
    "EntityNotFound",
    "IotConnectorIpAlreadyExists",
    "AgentConnectorDisconnected",
    "IotConnectorSecureModeError",
    "IotConnectorIcpIpNotAllowed",
    "NessusNotReady",
    "MissingFile",
    "InvalidFile",
    "NoSpaceLeftOnDevice",
    "FileTooBig",
    "NotContainingAnyAssets",
    "MergeConflict",
    "OldLicense",
    "EmOldLicense",
    "LicenseInactive",
    "EmLicenseInactive",
    "UpdateAlreadyInProgress",
    "OlderVersionUpdateAttempt",
    "FailedToAllocateOverlapping",
    "OverlappingNetsAlreadyInOrigin",
    "EmUpdateRequired",
    "IcpDisconnected",
    "OtAgentStatusNotSuitable",
    "NotDeletableWhileDefinedOnDuplicatedNetwork",
    "InvalidRequest",
]
