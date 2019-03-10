from bitarray import bitarray
from Orders.orders import P50XUpdateLok

class Train:

    SPEEDS = []
    SPEEDS.insert(0, 0)  
    SPEEDS.insert(1, 1)
    SPEEDS.insert(2, 2)
    SPEEDS.insert(3, 10)
    SPEEDS.insert(4, 19)
    SPEEDS.insert(5, 29)
    SPEEDS.insert(6, 38)
    SPEEDS.insert(7, 48)
    SPEEDS.insert(8, 57)
    SPEEDS.insert(9, 67)
    SPEEDS.insert(10, 76)
    SPEEDS.insert(11, 86)
    SPEEDS.insert(12, 95)
    SPEEDS.insert(13, 105)
    SPEEDS.insert(14, 114)
    SPEEDS.insert(15, 127)

    def __init__(self, name, lokAddress):
        ''' By default the train will have his speed set to 0, going forward and everything turned off '''
        self.name = name
        self.state = None

        if lokAddress < 0 or lokAddress > 9999:
            raise Exception('Invalid lokAddress')
        else:
            # [2:] to remove 0x at the beginning
            address = hex(lokAddress)[2:]

            # Split the address in two byte
            self.address_less_significant = address[:2] or '0' # low part
            self.address_most_significant = address[2:] or '0' # high part

        # Send as one byte
        self.speed = 0
        self.speed_index = 0
        self.__setSpeed__(0) # range from 0 to 127

        # Send as one byte, each parameters is a bit
        self.lights = False
        self.forward = False

        # Functions parameters
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.f4 = False

    #################
    ###  SETTERS  ###
    #################
    def __setSpeed__(self, value):
        if value < 0 or value > 127:
            raise Exception
        else:
            self.speed = hex(value)[2:]

    def __increaseSpeed__(self):
        next_index = self.speed_index + 1
        if next_index <= 15:
            self.speed_index = next_index
            self.__setSpeed__(Train.SPEEDS[self.speed_index])

    def __decreaseSpeed__(self):
        next_index = self.speed_index - 1
        if next_index >= 0:
            self.speed_index = next_index
            self.__setSpeed__(Train.SPEEDS[self.speed_index])

    #################
    ###  GETTERS  ###
    #################

    @property
    def parameters(self):
        ''' Convert lok's parameters into a byte array '''
        byte = bitarray()

        # Activate functions
        byte.append(True)

        # Force control
        byte.append(True)

        # Append parameters
        byte.append(self.forward)
        byte.append(self.lights)
        byte.append(self.f4)
        byte.append(self.f3)
        byte.append(self.f2)
        byte.append(self.f1)

        # Simplest way to get an hex representation of an array composed of byte
        return hex(int(byte.to01(), 2))[2:]

    #################
    ### FUNCTIONS ###
    #################

    def update(self):
        order = P50XUpdateLok(self)
        order.execute()

    def reverse(self):
        self.__setSpeed__(0)
        self.speed_index = 0
        self.forward = not self.forward
        self.update()

    def increaseSpeed(self):
        self.__increaseSpeed__()
        self.update()

    def decreaseSpeed(self):
        self.__increaseSpeed__()
        self.update()

    def toggleLights(self):
        self.lights = not self.lights
        self.update()

    def toggleF1(self):
        self.f1 = not self.f1
        self.update()

    def toggleF2(self):
        self.f2 = not self.f2
        self.update()

    def toggleF3(self):
        self.f3 = not self.f3
        self.update()

    def toggleF4(self):
        self.f4 = not self.f4
        self.update()
    
    def __str__(self):
        __string = []
        __string.append('Train : {0}'.format(self.name))
        __string.append('Address : low({0}) high({1})'.format(self.address_less_significant, self.address_most_significant))
        __string.append('Speed : {0}'.format(self.speed))
        __string.append('Lights : {0}'.format(self.lights))
        __string.append('Forward : {0}'.format(self.forward))
        __string.append('Function f1 : {0}'.format(self.f1))
        __string.append('Function f2 : {0}'.format(self.f2))
        __string.append('Function f3 : {0}'.format(self.f3))
        __string.append('Function f4 : {0}'.format(self.f4))
        return '\r\n'.join(__string)