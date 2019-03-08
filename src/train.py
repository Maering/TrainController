from .enums import SPEED
from .enums import LIGHTS
from .enums import DIRECTION
from .enums import FUNCTIONSTATUS

class Train:
    def __init__(self, name, lokAddress):
        self.name = name

        if lokAddress < 0 or lokAddress > 9999:
            raise Exception('Invalid lokAddress')
        else:
            # [2:] to remove 0x at the beginning
            address = hex(lokAddress)[2:]

            # Split the address in two byte
            self.address0 = address[:2]
            self.address1 = address[2:]

        # Send as one byte
        self.speed = SPEED.UNDEFINED

        # Send as one byte, each parameters is a bit
        self.lights = LIGHTS.UNDEFINED
        self.direction = DIRECTION.UNDEFINED

        self.f1 = FUNCTIONSTATUS.UNDEFINED
        self.f2 = FUNCTIONSTATUS.UNDEFINED
        self.f3 = FUNCTIONSTATUS.UNDEFINED
        self.f4 = FUNCTIONSTATUS.UNDEFINED

    def __update__(self):

        byte = ''
        byte += '11'
        byte += self.direction
        byte += self.lights
        byte += self.f4
        byte += self.f3
        byte += self.f2
        byte += self.f1

        array = hex(byte)[2:]

        pass

    #################
    ### FUNCTIONS ###
    #################

    def reverse(self):
        pass

    def increaseSpeed(self):
        pass

    def decreaseSpeed(self):
        pass

    def switchLights(self):
        pass

    def switchFunction(self, fx):
        pass

    def __send__(self, order):
        pass