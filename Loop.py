i = ""
started = False
while i != "quit":
    i = input("> ").lower()
    if i == "help":
        print ('''
start: to start the car
stop: to stop the car
quit: to quit the game       
        ''')
    elif i == "start":
        if started == True:
            print("The car has already started!")
        else:    
            started = True
            print("Car started...")
    elif i == "stop":
        if started == False:
            print("The car is already stopped!")
        else:
            started = False
            print("the car has stopped")
    elif i == "quit":
        print("The game has ended, bye bye")
        break
    else:
        print("I don't really understand your command, pick one from help list or type help to learn the commands")
    
