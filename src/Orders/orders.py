from serialHandler import SerialHandler

class P50XOrder:
    def __init__(self, action, *params):
        ''' action must be an hexadecimal value corresponding to an action of the P50x protocol '''
        self.action = action
        self.params = params

    def execute(self):
        ''' Send the order to RS232 '''
        _instance = SerialHandler.getInstance()
        _instance.send(self.action)
        for param in self.params:
            _instance.send(param)

    def __str__(self):
        __string = 'Action : {0}, Parameters ['.format(self.action)
        __params = ', '.join(self.params)
        return __string + __params + ']'
        

class P50XUpdateLok(P50XOrder):
    def __init__(self, train):
        super().__init__(80, train.address_less_significant, train.address_most_significant, train.speed, train.parameters)