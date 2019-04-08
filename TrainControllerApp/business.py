from bitarray import bitarray
from serial import Serial
from serial import PARITY_NONE
from serial import STOPBITS_TWO

# ------------------------------------------ #
# --------------- Controller --------------- #
# ------------------------------------------ #


class Controller:

    def __init__(self):
        self.trains = {}
        SerialHandler.getInstance().connect('/dev/ttyUSB0')
        SerialHandler.getInstance().send('xZzA1')  # configure Intellibox

    def __register_new_lok__(self, name, lokAddress):
        ''' lokAddress is in base10
            -----------------------
            returns : instancied train
        '''
        lokAddress = int(lokAddress)
        new_train = Train(name, lokAddress)
        if lokAddress in self.trains.keys():
            return self.trains[lokAddress]
        else:
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
            what    : [train, signal, crossing, etc...]
            name    : a name
            address : (base10)
            '''
            what = args.get('what')
            name = args.get('name')
            address = int(args.get('address'))

            if what == 'train':
                self.__register_new_lok__(name, address)
                print('train registred !')
            elif what == 'signal':
                pass  # next updates
            elif what == 'crossing':
                pass  # next updates

        elif action == 'train':
            '''
            lokid   :
            action  : [accelerate, decelerate, stop, reverse, togglelights, togglef1, togglef2, togglef3, togglef4]
            '''
            lokid = int(args.get('lokid'))
            train_action = args.get('action')

            # Get train
            train = self.trains[lokid]

            if train is not None:
                if train_action == 'accelerate':
                    train.increaseSpeed()
                elif train_action == 'decelerate':
                    train.decreaseSpeed()
                elif train_action == 'stop':
                    train.stop()
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
            what : [train, signal, crossing, etc...]
            List all target & registred material
            '''
            what = args.get('what')

            if what == 'train':
                self.__list_all_trains__()
            elif what == 'signal':
                pass  # next updates
            elif what == 'crossing':
                pass  # next updates

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

    def readResponse(self):
        ''' read line from serial port '''
        return SerialHandler.getInstance().readline()

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
        '''
        By default the train will have :
        - speed     : 0
        - forward   : true
        - lights    : false
        - f[1,2,3,4]: false
        '''
        # Validate lokAddress
        if lokAddress < 0 or lokAddress > 9999:
            raise Exception('Invalid lokAddress')
        else:
            self.lokAddress = lokAddress
            # [2:] to remove 0x at the beginning
            address = hex(lokAddress)[2:]

            # Split the address in two byte
            self.address_less_significant = address[:2] or '0000'  # low part
            self.address_most_significant = address[2:] or '0000'  # high part

        # Set name
        self.name = name

        # Send as one byte
        self.speed = 0
        self.speed_index = 0
        self.__setSpeed__(0)  # range from 0 to 127

        # Send as one byte, each parameters is a bit
        self.lights = False
        self.forward = False

        # Functions parameters
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.f4 = False

    # --------------------------------------- #
    # --------------- SETTERS --------------- #
    # --------------------------------------- #

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

    # --------------------------------------- #
    # --------------- GETTERS --------------- #
    # --------------------------------------- #

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

        # Simplest way to get an hex representation of bytes
        return hex(int(byte.to01(), 2))[2:]

    # ----------------------------------------- #
    # --------------- FUNCTIONS --------------- #
    # ----------------------------------------- #

    def update(self):
        order = P50XaUpdateLok(self)
        order.execute()

    def stop(self):
        self.__setSpeed__(0)
        self.speed_index = 0
        self.update()

    def reverse(self):
        self.__setSpeed__(0)
        self.speed_index = 0
        self.forward = not self.forward
        self.update()

    def increaseSpeed(self):
        self.__increaseSpeed__()
        self.update()

    def decreaseSpeed(self):
        self.__decreaseSpeed__()
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
        __string.append('Address : low({0}) high({1})'.format(
            self.address_less_significant,
            self.address_most_significant)
        )
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


class SerialHandler:
    '''
    https://gist.github.com/pazdera/1098129
    '''
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
            self.port = Serial()

    def connect(self, address):
        # Configure port
        self.port.port = address
        self.port.baudrate = 19200
        self.port.parity = PARITY_NONE
        self.port.stopbits = STOPBITS_TWO
        self.port.timeout = 0.100  # seconds

        # Open port
        self.port.open()

    def send(self, payload):
        if self.port.isOpen():
            payload = payload + '\r'
            print(
                str(self.port.port) +
                ":" +
                str(self.port.write(payload.encode('ascii'))) +
                " bytes written"
            )
            self.port.reset_input_buffer()
        else:
            raise IOError

    def readline(self):
        if self.port.out_waiting > 0:
            output = self.port.readline()
            print(output)
            return output
        else:
            return "empty"

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
#      * More information (french) :
#      http://www.espacerails.com/modelisme/article-44-intellibox--le-protocole-p50x.html


class P50XOrder:
    def __init__(self, action, *params):
        '''
        action  : known P50x command
        params  : parameters of the command
        '''
        self.action = action
        self.params = params

    def execute(self):
        ''' Send the order to RS232 '''
        _instance = SerialHandler.getInstance()
        message = ' '.join(self.params)
        message = ' '.join([self.action, message])
        message = message
        _instance.send(message)

    def __str__(self):
        __string = 'Action : {0}, Parameters ['.format(self.action)
        __params = ', '.join(self.params)
        return __string + __params + ']'


class P50XaGo(P50XOrder):
    def __init__(self):
        super().init('xGo')


class P50XaStop(P50XOrder):
    def __init__(self):
        super().init('xStop')


class P50XaUpdateLok(P50XOrder):
    def __init__(self, train):
        super().__init__(
            'L',
            str(train.lokAddress),
            str(int(train.lights)),
            str(int(train.forward)),
            str(int(train.f1)),
            str(int(train.f2)),
            str(int(train.f3)),
            str(int(train.f4))
        )
