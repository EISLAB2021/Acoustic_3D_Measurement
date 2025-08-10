"""
The struct and enum of the aris file header is translated from the C struct in the aris file header.
To keep consistency with origin, be careful with the submodule's commit hash.
Reference: ../aris_file_sdk/type-definitions/C/FileHeader.h
"""

import ctypes
from enum import IntEnum


class ArisFileHeader(ctypes.Structure):
    _pack_ = 1  # This corresponds to #pragma pack(push, 1)
    _fields_ = [
        ("Version", ctypes.c_uint32),
        ("FrameCount", ctypes.c_uint32),
        ("FrameRate", ctypes.c_uint32),
        ("HighResolution", ctypes.c_uint32),
        ("NumRawBeams", ctypes.c_uint32),
        ("SampleRate", ctypes.c_float),
        ("SamplesPerChannel", ctypes.c_uint32),
        ("ReceiverGain", ctypes.c_uint32),
        ("WindowStart", ctypes.c_float),
        ("WindowLength", ctypes.c_float),
        ("Reverse", ctypes.c_uint32),
        ("SN", ctypes.c_uint32),
        ("strDate", ctypes.c_char * 32),
        ("strHeaderID", ctypes.c_char * 256),
        ("UserID1", ctypes.c_int32),
        ("UserID2", ctypes.c_int32),
        ("UserID3", ctypes.c_int32),
        ("UserID4", ctypes.c_int32),
        ("StartFrame", ctypes.c_uint32),
        ("EndFrame", ctypes.c_uint32),
        ("TimeLapse", ctypes.c_uint32),
        ("RecordInterval", ctypes.c_uint32),
        ("RadioSeconds", ctypes.c_uint32),
        ("FrameInterval", ctypes.c_uint32),
        ("Flags", ctypes.c_uint32),
        ("AuxFlags", ctypes.c_uint32),
        ("Sspd", ctypes.c_uint32),
        ("Flags3D", ctypes.c_uint32),
        ("SoftwareVersion", ctypes.c_uint32),
        ("WaterTemp", ctypes.c_uint32),
        ("Salinity", ctypes.c_uint32),
        ("PulseLength", ctypes.c_uint32),
        ("TxMode", ctypes.c_uint32),
        ("VersionFGPA", ctypes.c_uint32),
        ("VersionPSuC", ctypes.c_uint32),
        ("ThumbnailFI", ctypes.c_uint32),
        ("FileSize", ctypes.c_uint64),
        ("OptionalHeaderSize", ctypes.c_uint64),
        ("OptionalTailSize", ctypes.c_uint64),
        ("VersionMinor", ctypes.c_uint32),
        ("LargeLens", ctypes.c_uint32),
        ("padding", ctypes.c_char * 568),
    ]


class ArisFileHeaderOffsets(IntEnum):
    ArisFileHeaderOffset_Version = 0
    ArisFileHeaderOffset_FrameCount = 4
    ArisFileHeaderOffset_FrameRate = 8
    ArisFileHeaderOffset_HighResolution = 12
    ArisFileHeaderOffset_NumRawBeams = 16
    ArisFileHeaderOffset_SampleRate = 20
    ArisFileHeaderOffset_SamplesPerChannel = 24
    ArisFileHeaderOffset_ReceiverGain = 28
    ArisFileHeaderOffset_WindowStart = 32
    ArisFileHeaderOffset_WindowLength = 36
    ArisFileHeaderOffset_Reverse = 40
    ArisFileHeaderOffset_SN = 44
    ArisFileHeaderOffset_strDate = 48
    ArisFileHeaderOffset_strHeaderID = 80
    ArisFileHeaderOffset_UserID1 = 336
    ArisFileHeaderOffset_UserID2 = 340
    ArisFileHeaderOffset_UserID3 = 344
    ArisFileHeaderOffset_UserID4 = 348
    ArisFileHeaderOffset_StartFrame = 352
    ArisFileHeaderOffset_EndFrame = 356
    ArisFileHeaderOffset_TimeLapse = 360
    ArisFileHeaderOffset_RecordInterval = 364
    ArisFileHeaderOffset_RadioSeconds = 368
    ArisFileHeaderOffset_FrameInterval = 372
    ArisFileHeaderOffset_Flags = 376
    ArisFileHeaderOffset_AuxFlags = 380
    ArisFileHeaderOffset_Sspd = 384
    ArisFileHeaderOffset_Flags3D = 388
    ArisFileHeaderOffset_SoftwareVersion = 392
    ArisFileHeaderOffset_WaterTemp = 396
    ArisFileHeaderOffset_Salinity = 400
    ArisFileHeaderOffset_PulseLength = 404
    ArisFileHeaderOffset_TxMode = 408
    ArisFileHeaderOffset_VersionFGPA = 412
    ArisFileHeaderOffset_VersionPSuC = 416
    ArisFileHeaderOffset_ThumbnailFI = 420
    ArisFileHeaderOffset_FileSize = 424
    ArisFileHeaderOffset_OptionalHeaderSize = 432
    ArisFileHeaderOffset_OptionalTailSize = 440
    ArisFileHeaderOffset_VersionMinor = 448
    ArisFileHeaderOffset_LargeLens = 452
