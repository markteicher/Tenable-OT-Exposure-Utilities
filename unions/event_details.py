# unions/event_details.py
#
# Tenable OT Security – EventDetails GraphQL Union
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/eventdetails.doc.html
#
# Purpose:
# - Represents all possible detail payloads for OT security events

EVENT_DETAILS_UNION_NAME = "EventDetails"

EVENT_DETAILS_TYPES = [
    "SnapshotMismatchDetails",
    "CodeDetails",
    "TagWriteDetailsList",
    "SetPointStatusDetails",
    "IoForceDetailsList",
    "TagCreateDetails",
    "TagDeleteDetails",
    "TaskCreateDetails",
    "TaskDeleteDetails",
    "ProgramCreateDetails",
    "ProgramDeleteDetails",
    "RoutineCreateDetails",
    "RoutineDeleteDetails",
    "RungDeleteDetails",
    "ItemRenameDetails",
    "FirmwareChangeDetails",
    "StateChangeDetails",
    "KeySwitchChangeDetails",
    "CodeEditDetails",
    "UnauthorizedWriteDetails",
    "IntrusionDetectionDetails",
    "BaselineDeviationDetails",
    "RdpConnectionDetails",
    "ArpScanDetails",
    "PortScanDetails",
    "IpConflictDetails",
    "FirmwareDownloadDetails",
    "PlcClearDetails",
    "PlcCommissionDetails",
    "FaceStepDetails",
    "ClearLatchStatusDetails",
    "DeleteApplicationDetails",
    "ModuleChangeDetails",
    "ModbusExceptionDetails",
    "SpikeDetails",
    "InactiveAssetDetails",
    "UsbChangeDetails",
    "IEC104Details",
    "DNP3Details",
    "GePlcStateChangeDetails",
    "LoginDetails",
    "FailedLoginDetails",
    "SaiaFileDetails",
    "BachmannModuleDetails",
    "BachmannDownloadDetails",
    "MMSDefineNamedVariableList",
    "MMSDeleteNamedVariableList",
    "ICCPCreateDataSet",
    "ICCPBilateralTableExchange",
    "RediscoveredAsset",
    "HoneywellChannelDetails",
    "IEC61850SubscribeFailure",
    "IEC61850UnauthorizedWrite",
]
