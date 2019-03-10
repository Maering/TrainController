from trainController import TrainController

# init
user_input = 'help'
tc = TrainController()

# program
while user_input is not 'exit' :
    try:
        user_input = input("Listening to command (space as separator between args): ")
        command, *args = user_input.split()
        tc.process(command, args)
    except:
        print("Something went wrong, please try again or type : help")