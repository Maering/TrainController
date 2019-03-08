from enum import Enum

class LIGHTS(Enum):
    UNDEFINED = '-1'
    OFF = '0'
    ON = '1'

class DIRECTION(Enum):
    UNDEFINED = '-1'
    BACKWARD = '0'
    FORWARD = '1'

class FUNCTIONSTATUS(Enum):
    UNDEFINED = '-1'
    OFF = '0'
    ON = '1'

class SPEED(Enum):
    UNDEFINED = -1
    STOP = 0
    EMERGENCY = 1
    SLOW0 = 2
    SLOW1 = 10
    SLOW2 = 19
    SLOW3 = 29
    CRUSE0 = 38
    CRUSE1 = 48
    CRUSE2 = 57
    CRUSE3 = 67
    CRUSE4 = 76
    FAST0 = 86
    FAST1 = 95
    FAST2 = 105
    FAST3 = 114
    FAST4 = 127
    