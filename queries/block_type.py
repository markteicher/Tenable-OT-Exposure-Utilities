"""
queries/block_type.py

Tenable OT Security – BlockType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/blocktype.doc.html

Purpose:
- Enumerates all OT logic, PLC, protocol, and vendor-specific block types
- Used for OT program structure analysis, configuration integrity, and forensic inspection
- Required for accurate parsing of PLC logic, IEC 61850 models, CIP projects, and vendor runtimes
"""

BLOCK_TYPES = [
    "BlockUnknown",
    "BlockDB",
    "BlockSDB",
    "BlockFC",
    "BlockSFC",
    "BlockFB",
    "BlockSFB",
    "BlockOB",
    "BlockSystem",
    "BlockMetadata",
    "BlockCode",
    "BlockDiagnostics",

    # CIP / Rockwell
    "BlockCipTag",
    "BlockCipTagBit",
    "BlockCipIoForcing",
    "BlockCipSfcForcing",
    "BlockCipTags",
    "BlockCipTask",
    "BlockCipTasks",
    "BlockCipProgram",
    "BlockCipPrograms",
    "BlockCipProject",
    "BlockCipRoutine",
    "BlockCipRoutines",
    "BlockCipForce",

    # Generic / File Structures
    "BlockDirectory",
    "BlockDataFile",

    # P2 / Proprietary
    "BlockP2Program",
    "BlockP2CodeLinesAdded",
    "BlockP2DeletedRange",
    "BlockP2CodeLinesUploaded",
    "BlockP2Point",
    "BlockP2PointValueChanged",
    "BlockP2PointStatusChanged",
    "BlockP2DeletedProgram",

    # Siemens / SRTP
    "BlockS7IOForcedField",
    "BlockSrtpSetState",
    "BlockSrtpCodeFilesDownloaded",
    "BlockSrtpCodeFilesUploaded",
    "BlockSrtpClear",

    # Emerson FACE
    "BlockFaceSection",
    "BlockFaceCategory",
    "BlockFaceTag",
    "BlockFacePlc",
    "BlockFaceNodeId",

    # ABB AC800
    "BlockABBAC800GlobalData",
    "BlockABBAC800Configuration",
    "BlockABBAC800Applications",
    "BlockABBAC800CompilingStation",
    "BlockABBAC800Signature",
    "BlockABBAC800Tag",
    "BlockABBAC800DomainSize",
    "BlockABBAC800ProjectPath",
    "BlockABBAC800IOForcedField",
    "BlockABBAC800ClearLatchedStatus",
    "BlockABBAC800ProgramInvocationState",

    # IEC 61850
    "BlockIEC61850StationName",
    "BlockIEC61850LD",
    "BlockIEC61850LN",
    "BlockIEC61850FC",
    "BlockIEC61850Function",
    "BlockIEC61850Attribute",

    # Vendor-specific / Conceptual
    "BlockConcept",
    "BlockMELSECConfiguration",
    "BlockMELSECProgram",
    "BlockYokogawaSection",
    "BlockToyopucProgram",
    "BlockToyopucProject",
    "BlockSiprotec4",

    # ABB RTU500
    "BlockAbbRTU500RCD",
    "BlockAbbRTU500RCDFileVersion",
    "BlockAbbRTU500RCDHash",
    "BlockAbbRTU500Title",
    "BlockAbbRTU500Object",
    "BlockAbbRTU500Section",
    "BlockAbbRTU500SubSection",
    "BlockAbbRTU500Parameter",
    "BlockAbbRTU500Project",
    "BlockAbbRTU500File",

    # FOX
    "BlockFoxDriversProject",
    "BlockFoxDriver",
]
