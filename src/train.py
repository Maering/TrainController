from bitarray import bitarray

class Train:
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
        self.setSpeed(0) # range from 0 to 127

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
    def setSpeed(self, value):
        if value < 0 or value > 127:
            raise Exception
        else:
            self.speed = hex(value)[2:]

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

    def reverse(self):
        pass

    def increaseSpeed(self):
        pass

    def decreaseSpeed(self):
        pass

    def toggleLights(self):
        self.lights = not self.lights

    def toggleF1(self):
        self.f1 = not self.f1

    def toggleF2(self):
        self.f2 = not self.f2

    def toggleF3(self):
        self.f3 = not self.f3

    def toggleF4(self):
        self.f4 = not self.f4

    def __send__(self, order):
        pass
    
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