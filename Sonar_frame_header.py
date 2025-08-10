import ctypes
from enum import IntEnum


# --- ArisFrameHeader ---
class ArisFrameHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("FrameIndex", ctypes.c_uint32),
        ("FrameTime", ctypes.c_uint64),
        ("Version", ctypes.c_uint32),
        ("Status", ctypes.c_uint32),
        ("sonarTimeStamp", ctypes.c_uint64),
        ("TS_Day", ctypes.c_uint32),
        ("TS_Hour", ctypes.c_uint32),
        ("TS_Minute", ctypes.c_uint32),
        ("TS_Second", ctypes.c_uint32),
        ("TS_Hsecond", ctypes.c_uint32),
        ("TransmitMode", ctypes.c_uint32),
        ("WindowStart", ctypes.c_float),
        ("WindowLength", ctypes.c_float),
        ("Threshold", ctypes.c_uint32),
        ("Intensity", ctypes.c_int32),
        ("ReceiverGain", ctypes.c_uint32),
        ("DegC1", ctypes.c_uint32),
        ("DegC2", ctypes.c_uint32),
        ("Humidity", ctypes.c_uint32),
        ("Focus", ctypes.c_uint32),
        ("Battery", ctypes.c_uint32),
        ("UserValue1", ctypes.c_float),
        ("UserValue2", ctypes.c_float),
        ("UserValue3", ctypes.c_float),
        ("UserValue4", ctypes.c_float),
        ("UserValue5", ctypes.c_float),
        ("UserValue6", ctypes.c_float),
        ("UserValue7", ctypes.c_float),
        ("UserValue8", ctypes.c_float),
        ("Velocity", ctypes.c_float),
        ("Depth", ctypes.c_float),
        ("Altitude", ctypes.c_float),
        ("Pitch", ctypes.c_float),
        ("PitchRate", ctypes.c_float),
        ("Roll", ctypes.c_float),
        ("RollRate", ctypes.c_float),
        ("Heading", ctypes.c_float),
        ("HeadingRate", ctypes.c_float),
        ("CompassHeading", ctypes.c_float),
        ("CompassPitch", ctypes.c_float),
        ("CompassRoll", ctypes.c_float),
        ("Latitude", ctypes.c_double),
        ("Longitude", ctypes.c_double),
        ("SonarPosition", ctypes.c_float),
        ("ConfigFlags", ctypes.c_uint32),
        ("BeamTilt", ctypes.c_float),
        ("TargetRange", ctypes.c_float),
        ("TargetBearing", ctypes.c_float),
        ("TargetPresent", ctypes.c_uint32),
        ("FirmwareRevision", ctypes.c_uint32),
        ("Flags", ctypes.c_uint32),
        ("SourceFrame", ctypes.c_uint32),
        ("WaterTemp", ctypes.c_float),
        ("TimerPeriod", ctypes.c_uint32),
        ("SonarX", ctypes.c_float),
        ("SonarY", ctypes.c_float),
        ("SonarZ", ctypes.c_float),
        ("SonarPan", ctypes.c_float),
        ("SonarTilt", ctypes.c_float),
        ("SonarRoll", ctypes.c_float),
        ("PanPNNL", ctypes.c_float),
        ("TiltPNNL", ctypes.c_float),
        ("RollPNNL", ctypes.c_float),
        ("VehicleTime", ctypes.c_double),
        ("TimeGGK", ctypes.c_float),
        ("DateGGK", ctypes.c_uint32),
        ("QualityGGK", ctypes.c_uint32),
        ("NumSatsGGK", ctypes.c_uint32),
        ("DOPGGK", ctypes.c_float),
        ("EHTGGK", ctypes.c_float),
        ("HeaveTSS", ctypes.c_float),
        ("YearGPS", ctypes.c_uint32),
        ("MonthGPS", ctypes.c_uint32),
        ("DayGPS", ctypes.c_uint32),
        ("HourGPS", ctypes.c_uint32),
        ("MinuteGPS", ctypes.c_uint32),
        ("SecondGPS", ctypes.c_uint32),
        ("HSecondGPS", ctypes.c_uint32),
        ("SonarPanOffset", ctypes.c_float),
        ("SonarTiltOffset", ctypes.c_float),
        ("SonarRollOffset", ctypes.c_float),
        ("SonarXOffset", ctypes.c_float),
        ("SonarYOffset", ctypes.c_float),
        ("SonarZOffset", ctypes.c_float),
        ("Tmatrix", ctypes.c_float * 16),
        ("SampleRate", ctypes.c_float),
        ("AccellX", ctypes.c_float),
        ("AccellY", ctypes.c_float),
        ("AccellZ", ctypes.c_float),
        ("PingMode", ctypes.c_uint32),
        ("FrequencyHiLow", ctypes.c_uint32),
        ("PulseWidth", ctypes.c_uint32),
        ("CyclePeriod", ctypes.c_uint32),
        ("SamplePeriod", ctypes.c_uint32),
        ("TransmitEnable", ctypes.c_uint32),
        ("FrameRate", ctypes.c_float),
        ("SoundSpeed", ctypes.c_float),
        ("SamplesPerBeam", ctypes.c_uint32),
        ("Enable150V", ctypes.c_uint32),
        ("SampleStartDelay", ctypes.c_uint32),
        ("LargeLens", ctypes.c_uint32),
        ("TheSystemType", ctypes.c_uint32),
        ("SonarSerialNumber", ctypes.c_uint32),
        ("ReservedEK", ctypes.c_uint64),
        ("ArisErrorFlagsUint", ctypes.c_uint32),
        ("MissedPackets", ctypes.c_uint32),
        ("ArisAppVersion", ctypes.c_uint32),
        ("Available2", ctypes.c_uint32),
        ("ReorderedSamples", ctypes.c_uint32),
        ("Salinity", ctypes.c_uint32),
        ("Pressure", ctypes.c_float),
        ("BatteryVoltage", ctypes.c_float),
        ("MainVoltage", ctypes.c_float),
        ("SwitchVoltage", ctypes.c_float),
        ("FocusMotorMoving", ctypes.c_uint32),
        ("VoltageChanging", ctypes.c_uint32),
        ("FocusTimeoutFault", ctypes.c_uint32),
        ("FocusOverCurrentFault", ctypes.c_uint32),
        ("FocusNotFoundFault", ctypes.c_uint32),
        ("FocusStalledFault", ctypes.c_uint32),
        ("FPGATimeoutFault", ctypes.c_uint32),
        ("FPGABusyFault", ctypes.c_uint32),
        ("FPGAStuckFault", ctypes.c_uint32),
        ("CPUTempFault", ctypes.c_uint32),
        ("PSUTempFault", ctypes.c_uint32),
        ("WaterTempFault", ctypes.c_uint32),
        ("HumidityFault", ctypes.c_uint32),
        ("PressureFault", ctypes.c_uint32),
        ("VoltageReadFault", ctypes.c_uint32),
        ("VoltageWriteFault", ctypes.c_uint32),
        ("FocusCurrentPosition", ctypes.c_uint32),
        ("TargetPan", ctypes.c_float),
        ("TargetTilt", ctypes.c_float),
        ("TargetRoll", ctypes.c_float),
        ("PanMotorErrorCode", ctypes.c_uint32),
        ("TiltMotorErrorCode", ctypes.c_uint32),
        ("RollMotorErrorCode", ctypes.c_uint32),
        ("PanAbsPosition", ctypes.c_float),
        ("TiltAbsPosition", ctypes.c_float),
        ("RollAbsPosition", ctypes.c_float),
        ("PanAccelX", ctypes.c_float),
        ("PanAccelY", ctypes.c_float),
        ("PanAccelZ", ctypes.c_float),
        ("TiltAccelX", ctypes.c_float),
        ("TiltAccelY", ctypes.c_float),
        ("TiltAccelZ", ctypes.c_float),
        ("RollAccelX", ctypes.c_float),
        ("RollAccelY", ctypes.c_float),
        ("RollAccelZ", ctypes.c_float),
        ("AppliedSettings", ctypes.c_uint32),
        ("ConstrainedSettings", ctypes.c_uint32),
        ("InvalidSettings", ctypes.c_uint32),
        ("EnableInterpacketDelay", ctypes.c_uint32),
        ("InterpacketDelayPeriod", ctypes.c_uint32),
        ("Uptime", ctypes.c_uint32),
        ("ArisAppVersionMajor", ctypes.c_uint16),
        ("ArisAppVersionMinor", ctypes.c_uint16),
        ("GoTime", ctypes.c_uint64),
        ("PanVelocity", ctypes.c_float),
        ("TiltVelocity", ctypes.c_float),
        ("RollVelocity", ctypes.c_float),
        ("GpsTimeAge", ctypes.c_uint32),
        ("SystemVariant", ctypes.c_uint32),
        ("CompassRevision", ctypes.c_uint32),
        ("CompassReserved1", ctypes.c_float),
        ("padding", ctypes.c_char * 280),
    ]

    def get_beams_from_pingmode(self):
        if self.PingMode in {1, 2}:
            return 48
        elif self.PingMode in {3, 4, 5}:
            return 96
        elif self.PingMode in {6, 7, 8}:
            return 64
        elif self.PingMode in {9, 10, 11, 12}:
            return 128
        else:
            raise ValueError(f"Invalid PingMode: {self.PingMode}")


from enum import IntEnum


class ArisFrameHeaderOffsets(IntEnum):
    ArisFrameHeaderOffset_FrameIndex = 0
    ArisFrameHeaderOffset_FrameTime = 4
    ArisFrameHeaderOffset_Version = 12
    ArisFrameHeaderOffset_Status = 16
    ArisFrameHeaderOffset_sonarTimeStamp = 20
    ArisFrameHeaderOffset_TS_Day = 28
    ArisFrameHeaderOffset_TS_Hour = 32
    ArisFrameHeaderOffset_TS_Minute = 36
    ArisFrameHeaderOffset_TS_Second = 40
    ArisFrameHeaderOffset_TS_Hsecond = 44
    ArisFrameHeaderOffset_TransmitMode = 48
    ArisFrameHeaderOffset_WindowStart = 52
    ArisFrameHeaderOffset_WindowLength = 56
    ArisFrameHeaderOffset_Threshold = 60
    ArisFrameHeaderOffset_Intensity = 64
    ArisFrameHeaderOffset_ReceiverGain = 68
    ArisFrameHeaderOffset_DegC1 = 72
    ArisFrameHeaderOffset_DegC2 = 76
    ArisFrameHeaderOffset_Humidity = 80
    ArisFrameHeaderOffset_Focus = 84
    # OBSOLETE: Unused.
    ArisFrameHeaderOffset_Battery = 88
    ArisFrameHeaderOffset_UserValue1 = 92
    ArisFrameHeaderOffset_UserValue2 = 96
    ArisFrameHeaderOffset_UserValue3 = 100
    ArisFrameHeaderOffset_UserValue4 = 104
    ArisFrameHeaderOffset_UserValue5 = 108
    ArisFrameHeaderOffset_UserValue6 = 112
    ArisFrameHeaderOffset_UserValue7 = 116
    ArisFrameHeaderOffset_UserValue8 = 120
    ArisFrameHeaderOffset_Velocity = 124
    ArisFrameHeaderOffset_Depth = 128
    ArisFrameHeaderOffset_Altitude = 132
    ArisFrameHeaderOffset_Pitch = 136
    ArisFrameHeaderOffset_PitchRate = 140
    ArisFrameHeaderOffset_Roll = 144
    ArisFrameHeaderOffset_RollRate = 148
    ArisFrameHeaderOffset_Heading = 152
    ArisFrameHeaderOffset_HeadingRate = 156
    ArisFrameHeaderOffset_CompassHeading = 160
    ArisFrameHeaderOffset_CompassPitch = 164
    ArisFrameHeaderOffset_CompassRoll = 168
    ArisFrameHeaderOffset_Latitude = 172
    ArisFrameHeaderOffset_Longitude = 180
    ArisFrameHeaderOffset_SonarPosition = 188
    ArisFrameHeaderOffset_ConfigFlags = 192
    ArisFrameHeaderOffset_BeamTilt = 196
    ArisFrameHeaderOffset_TargetRange = 200
    ArisFrameHeaderOffset_TargetBearing = 204
    ArisFrameHeaderOffset_TargetPresent = 208
    # OBSOLETE: Unused.
    ArisFrameHeaderOffset_FirmwareRevision = 212
    ArisFrameHeaderOffset_Flags = 216
    ArisFrameHeaderOffset_SourceFrame = 220
    ArisFrameHeaderOffset_WaterTemp = 224
    ArisFrameHeaderOffset_TimerPeriod = 228
    ArisFrameHeaderOffset_SonarX = 232
    ArisFrameHeaderOffset_SonarY = 236
    ArisFrameHeaderOffset_SonarZ = 240
    ArisFrameHeaderOffset_SonarPan = 244
    ArisFrameHeaderOffset_SonarTilt = 248
    ArisFrameHeaderOffset_SonarRoll = 252
    ArisFrameHeaderOffset_PanPNNL = 256
    ArisFrameHeaderOffset_TiltPNNL = 260
    ArisFrameHeaderOffset_RollPNNL = 264
    ArisFrameHeaderOffset_VehicleTime = 268
    ArisFrameHeaderOffset_TimeGGK = 276
    ArisFrameHeaderOffset_DateGGK = 280
    ArisFrameHeaderOffset_QualityGGK = 284
    ArisFrameHeaderOffset_NumSatsGGK = 288
    ArisFrameHeaderOffset_DOPGGK = 292
    ArisFrameHeaderOffset_EHTGGK = 296
    ArisFrameHeaderOffset_HeaveTSS = 300
    ArisFrameHeaderOffset_YearGPS = 304
    ArisFrameHeaderOffset_MonthGPS = 308
    ArisFrameHeaderOffset_DayGPS = 312
    ArisFrameHeaderOffset_HourGPS = 316
    ArisFrameHeaderOffset_MinuteGPS = 320
    ArisFrameHeaderOffset_SecondGPS = 324
    ArisFrameHeaderOffset_HSecondGPS = 328
    ArisFrameHeaderOffset_SonarPanOffset = 332
    ArisFrameHeaderOffset_SonarTiltOffset = 336
    ArisFrameHeaderOffset_SonarRollOffset = 340
    ArisFrameHeaderOffset_SonarXOffset = 344
    ArisFrameHeaderOffset_SonarYOffset = 348
    ArisFrameHeaderOffset_SonarZOffset = 352
    ArisFrameHeaderOffset_Tmatrix = 356
    ArisFrameHeaderOffset_SampleRate = 420
    ArisFrameHeaderOffset_AccellX = 424
    ArisFrameHeaderOffset_AccellY = 428
    ArisFrameHeaderOffset_AccellZ = 432
    ArisFrameHeaderOffset_PingMode = 436
    ArisFrameHeaderOffset_FrequencyHiLow = 440
    ArisFrameHeaderOffset_PulseWidth = 444
    ArisFrameHeaderOffset_CyclePeriod = 448
    ArisFrameHeaderOffset_SamplePeriod = 452
    ArisFrameHeaderOffset_TransmitEnable = 456
    ArisFrameHeaderOffset_FrameRate = 460
    ArisFrameHeaderOffset_SoundSpeed = 464
    ArisFrameHeaderOffset_SamplesPerBeam = 468
    ArisFrameHeaderOffset_Enable150V = 472
    ArisFrameHeaderOffset_SampleStartDelay = 476
    ArisFrameHeaderOffset_LargeLens = 480
    ArisFrameHeaderOffset_TheSystemType = 484
    ArisFrameHeaderOffset_SonarSerialNumber = 488
    # OBSOLETE: Obsolete
    ArisFrameHeaderOffset_ReservedEK = 492
    ArisFrameHeaderOffset_ArisErrorFlagsUint = 500
    ArisFrameHeaderOffset_MissedPackets = 504
    ArisFrameHeaderOffset_ArisAppVersion = 508
    ArisFrameHeaderOffset_Available2 = 512
    ArisFrameHeaderOffset_ReorderedSamples = 516
    ArisFrameHeaderOffset_Salinity = 520
    ArisFrameHeaderOffset_Pressure = 524
    ArisFrameHeaderOffset_BatteryVoltage = 528
    ArisFrameHeaderOffset_MainVoltage = 532
    ArisFrameHeaderOffset_SwitchVoltage = 536
    ArisFrameHeaderOffset_FocusMotorMoving = 540
    ArisFrameHeaderOffset_VoltageChanging = 544
    ArisFrameHeaderOffset_FocusTimeoutFault = 548
    ArisFrameHeaderOffset_FocusOverCurrentFault = 552
    ArisFrameHeaderOffset_FocusNotFoundFault = 556
    ArisFrameHeaderOffset_FocusStalledFault = 560
    ArisFrameHeaderOffset_FPGATimeoutFault = 564
    ArisFrameHeaderOffset_FPGABusyFault = 568
    ArisFrameHeaderOffset_FPGAStuckFault = 572
    ArisFrameHeaderOffset_CPUTempFault = 576
    ArisFrameHeaderOffset_PSUTempFault = 580
    ArisFrameHeaderOffset_WaterTempFault = 584
    ArisFrameHeaderOffset_HumidityFault = 588
    ArisFrameHeaderOffset_PressureFault = 592
    ArisFrameHeaderOffset_VoltageReadFault = 596
    ArisFrameHeaderOffset_VoltageWriteFault = 600
    ArisFrameHeaderOffset_FocusCurrentPosition = 604
    ArisFrameHeaderOffset_TargetPan = 608
    ArisFrameHeaderOffset_TargetTilt = 612
    ArisFrameHeaderOffset_TargetRoll = 616
    ArisFrameHeaderOffset_PanMotorErrorCode = 620
    ArisFrameHeaderOffset_TiltMotorErrorCode = 624
    ArisFrameHeaderOffset_RollMotorErrorCode = 628
    ArisFrameHeaderOffset_PanAbsPosition = 632
    ArisFrameHeaderOffset_TiltAbsPosition = 636
    ArisFrameHeaderOffset_RollAbsPosition = 640
    ArisFrameHeaderOffset_PanAccelX = 644
    ArisFrameHeaderOffset_PanAccelY = 648
    ArisFrameHeaderOffset_PanAccelZ = 652
    ArisFrameHeaderOffset_TiltAccelX = 656
    ArisFrameHeaderOffset_TiltAccelY = 660
    ArisFrameHeaderOffset_TiltAccelZ = 664
    ArisFrameHeaderOffset_RollAccelX = 668
    ArisFrameHeaderOffset_RollAccelY = 672
    ArisFrameHeaderOffset_RollAccelZ = 676
    ArisFrameHeaderOffset_AppliedSettings = 680
    ArisFrameHeaderOffset_ConstrainedSettings = 684
    ArisFrameHeaderOffset_InvalidSettings = 688
    ArisFrameHeaderOffset_EnableInterpacketDelay = 692
    ArisFrameHeaderOffset_InterpacketDelayPeriod = 696
    ArisFrameHeaderOffset_Uptime = 700
    ArisFrameHeaderOffset_ArisAppVersionMajor = 704
    ArisFrameHeaderOffset_ArisAppVersionMinor = 706
    ArisFrameHeaderOffset_GoTime = 708
    ArisFrameHeaderOffset_PanVelocity = 716
    ArisFrameHeaderOffset_TiltVelocity = 720
    ArisFrameHeaderOffset_RollVelocity = 724
    ArisFrameHeaderOffset_GpsTimeAge = 728
    ArisFrameHeaderOffset_SystemVariant = 732
    ArisFrameHeaderOffset_CompassRevision = 736
    ArisFrameHeaderOffset_CompassReserved1 = 740
