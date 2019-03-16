from Trains.train import Train

class TrainController:

    def __init__(self):
        self.trains = {}
        pass

    def __register_new_lok__(self, name, lokAddress):
        ''' lokAddress is in base10 
            -----------------------
            returns : instancied train
        '''
        new_train = Train(name, int(lokAddress))
        self.trains[name] = new_train
        return new_train

    def __try_get_train__(self, name):
        ''' try to get the train with the given name '''
        if self.trains.__contains__(name):
            return self.trains[name]
        else:
            raise Exception

    def __list_all_trains__(self):
        ''' print all knows train '''
        for train in self.trains:
            print(train)

    # ------------- COMMANDS LINES -------------#

    def process(self, command, args):
        if command == 'register':
            '''
            args0 : type [train, signal, crossing, etc...]
            args1 : name
            args2 : address (base10)
            '''
            if args[0] == 'train':
                self.__register_new_lok__(args[1], args[2])
                print('train registred !')
            elif args[0] == 'signal':
                pass # next updates
            elif args[0] == 'crossing':
                pass # next updates

        elif command == 'train':
            ''' 
            args0 : name
            args1 : command [acc, dec, rev, tl, t1, t2, t3, t4]
            '''
            train = self.__try_get_train__(args[0])
            if train is not None:
                if args[1] == 'acc':
                    train.increaseSpeed()
                elif args[1] == 'dec':
                    train.decreaseSpeed()
                elif args[1] == 'rev':
                    train.reverse()
                elif args[1] == 'tl':
                    train.toggleLights()
                elif args[1] == 't1':
                    train.toggleF1()
                elif args[1] == 't2':
                    train.toggleF2()
                elif args[1] == 't3':
                    train.toggleF3()
                elif args[1] == 't4':
                    train.toggleF4()
            else:
                raise Exception
            
            print('train altered !')
        
        elif command == 'list':
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

        elif command == 'off':
            '''
            Turns off the system
            '''
            pass

        elif command == 'on':
            '''
            Turns on the system
            '''
            pass

        elif command == 'quit':
            '''
            Exit the program
            '''
            return False

        else:
            '''
            unkwown command, show help
            '''
            self.__help__()
        
        return True

    def __help__(self):
        ''' help of the function '''
        response = 'List of knows commands : \r\n\t'
        response += '\r\n\t'.join([
            'help',
            'register',
            'train',
            'list',
            'off',
            'on',                        
            'TODO: use -h after a command to see its help !'
            ])
        print(response)

    


