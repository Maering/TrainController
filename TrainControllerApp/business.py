# ------------------------------------------ #
# --------------- Controller --------------- #
# ------------------------------------------ #
class Controller:

    def __init__(self):
        self.trains = {}
        pass

    def __register_new_lok__(self, name, lokAddress):
        ''' lokAddress is in base10 
            -----------------------
            returns : instancied train
        '''
        lokAddress = int(lokAddress)
        new_train = Train(name, lokAddress)
        self.trains[lokAddress] = new_train
        return new_train

    def __list_all_trains__(self):
        ''' print all knows train '''
        for train in self.trains:
            print(train)

    # ------------- actionS LINES -------------#

    def process(self, action, args):
        ''' 
        action  : [string] name of the action to perform
        args    : [dictionary]<string, object> dictionary of keys and values
        '''
        print(action)
        print(args)

        ''' process provided action and args '''
        if action == 'register':
            '''
            type    : [train, signal, crossing, etc...]
            name    : a name
            lokid   : (base10)
            '''
            if args[0] == 'train':
                self.__register_new_lok__(args[1], args[2])
                print('train registred !')
            elif args[0] == 'signal':
                pass # next updates
            elif args[0] == 'crossing':
                pass # next updates

        elif action == 'train':
            ''' 
            lokid   : 
            action  : [acc, dec, rev, tl, t1, t2, t3, t4]
            '''

            lokid = args.get('lokid')
            train_action = args.get('action')

            train = self.trains[lokid]

            if train is not None:
                if train_action == 'accelerate':
                    train.increaseSpeed()
                elif train_action == 'decelerate':
                    train.decreaseSpeed()
                elif train_action == 'reverse':
                    train.reverse()
                elif train_action == 'togglelights':
                    train.toggleLights()
                elif train_action == 'togglef1':
                    train.toggleF1()
                elif train_action == 'togglef2':
                    train.toggleF2()
                elif train_action == 'togglef3':
                    train.toggleF3()
                elif train_action == 'togglef4':
                    train.toggleF4()
            else:
                raise Exception
            
            print('train altered !')
        
        elif action == 'list':
            '''
            args0 : type [train, signal, crossing, etc...]
            List all target & registred material
            '''
            if args[0] == 'train':
                self.__list_all_trains__()
            elif args[0] == 'signal':
                pass # next updates
            elif args[0] == 'crossing':
                pass # next updates

        elif action == 'stop':
            '''
            Turns off the system
            '''
            # TODO:
            pass

        elif action == 'go':
            '''
            Turns on the system
            '''
            # TODO:
            pass

        elif action == 'quit':
            '''
            Exit the program
            '''
            return False

        else:
            '''
            unkwown action, show help
            '''
            self.__help__()

        return True

    def __help__(self):
        ''' help of the function '''
        response = 'List of knows actions : \r\n\t'
        response += '\r\n\t'.join([
            'help',
            'register',
            'train',
            'list',
            'stop',
            'go',                        
            'TODO: use -h after a action to see its help !'
            ])
        print(response)

# ------------------------------------- #
# --------------- Train --------------- #
# ------------------------------------- #
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
            self.address_less_significant = address[:2] or '0000' # low part
            self.address_most_significant = address[2:] or '0000' # high part

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

# ------------------------------------------ #
# --------------- SerialPort --------------- #
# ------------------------------------------ #
from serial import *
# The factory settings configure the Intellibox for an IBM compatible PC and
# for using only the syntax of the Märklin 6050/6051 Interface.
#      * The default Intellibox serial interface settings are:
#      * 8 data bits
#      * 2†stop bits
#      * baud rate 19200 bit/s
#      * no parity
#      * CTS line used
#      * DTR line not used.
#      * -------------------------------------------
#      * More information (french) : http://www.espacerails.com/modelisme/article-44-intellibox--le-protocole-p50x.html
class SerialHandler:
    """ https://gist.github.com/pazdera/1098129 """
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if SerialHandler.__instance is None:
            SerialHandler()
        return SerialHandler.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SerialHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SerialHandler.__instance = self
            self.port = serial.Serial()

    def connect(self, address):
        # Configure port
        self.port.port = address
        self.port.baudrate = 19200
        self.port.parity = serial.PARITY_NONE
        self.port.stopbits = serial.STOPBITS_TWO

        # Open port
        self.port.open()

    def send(self, __bytes):
        if self.port.isOpen():
            self.port.write(__bytes)
        else:
            raise IOError

    def read(self):
        print(self.port.readall())
