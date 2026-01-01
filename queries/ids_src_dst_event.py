"""
queries/ids_src_dst_event.py

Tenable OT Security – IDSSrcDstEvent GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/idssrcdstevent.doc.html

Purpose:
- Enumerates possible IDS events that involve source and destination context
"""

IDS_SRC_DST_EVENT_ENUM_NAME = "IDSSrcDstEvent"

IDS_SRC_DST_EVENTS = [
    "SynScan",
    "RdpConnectionWithAuthentication",
    "RdpConnectionNoAuthentication",
    "ModbusExceptionIllegalFunction",
    "ModbusExceptionIllegalDataAddress",
    "ModbusExceptionIllegalDataValue",
    "IEC104StartDataTransfer",
    "IEC104StopDataTransfer",
    "IEC104InterrogationCommand",
    "IEC104CounterInterrogationCommand",
    "IEC104ClockSynchronizationCommand",
    "IEC104ResetProcessCommand",
    "IEC104TestCommandWithTimeTag",
    "DNP3FcSelect",
    "DNP3FcOperate",
    "DNP3FcDirectOperate",
    "DNP3FcDirectOperateNoResponse",
    "DNP3FcColdRestart",
    "DNP3FcWarmRestart",
    "DNP3FcInitializeData",
    "DNP3FcInitializeApplication",
    "DNP3FcStartApplication",
    "DNP3FcStopApplication",
    "DNP3FcEnableUnsolicitedResponses",
    "DNP3FcDisableUnsolicitedResponses",
    "DNP3FcOpenFile",
    "DNP3FcCloseFile",
    "DNP3FcDeleteFile",
    "DNP3FcAuthenticateFile",
    "DNP3FcActivateConfiguration",
    "DNP3iinFcNotImplemented",
    "DNP3iinObjectUnknown",
    "DNP3iinParamError",
    "DNP3iinBufferOverflow",
    "DNP3iinAlreadyExecuting",
    "DNP3iinCorruptConfig",
    "FtpSuccessfulLogin",
    "FtpFailedLogin",
    "TelnetSuccessfulLogin",
    "TelnetFailedLogin",
    "TelnetLoginAttempt",
    "MmsDefineNamedVariableList",
    "MmsDeleteNamedVariableList",
    "ICCPCreateDataSet",
    "ICCPBilateralTableExchange",
    "IEC61850SubscriptionFailure",
    "IEC61850UnauthorizedWrite",
]
