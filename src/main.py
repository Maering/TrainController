from trainController import TrainController
# init
user_input = 'help'
tc = TrainController()
b = True

# program
while b:
    try:
        user_input = input("Listening to command (space as separator between args): ")
        command, *args = user_input.split()
        b = tc.process(command, args)
    except:
        print("Something went wrong, please try again or type : help")