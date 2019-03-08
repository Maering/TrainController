class Singleton:
    """ https://gist.github.com/pazdera/1098129 """
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


# The factory settings configure the Intellibox for an IBM compatible PC and for using only the syntax of the Märklin 6050/6051 Interface.
#      * The default Intellibox serial interface settings are: 
#      * 8 data bits, 
#      * 2†stop bits,  
#      * baud rate 2400  bit/s,  
#      * no parity, 
#      * CTS line used, 
#      * DTR line not used.
#      * -------------------------------------------
#      * More information (french) : http://www.espacerails.com/modelisme/article-44-intellibox--le-protocole-p50x.html

import serial
from .order import Order
class SerialHandler(Singleton):
    def __init__(self, address):
        self.port = serial.Serial()

        # Configure port
        self.port.port = address
        self.port.baudrate = 2400
        self.port.parity = serial.PARITY_NONE
        self.port.stopbits = serial.STOPBITS_TWO

        # Open port
        self.port.open()

    def send(self, order):
        if self.port.isOpen():
            self.port.write(order.instruction)
            for param in order.params:
                self.port.write(param)
        else:
            raise IOError

    def read(self):
        print(self.port.readall())