command = ""
started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car Started...Ready to go")

    elif command == "stop":
        if not started:
            print("Car is stopped already!")
        else:
            started = False
            print("Car Stopped")

    elif command == "help":
        print('''
start
stop
quit
        ''')

    elif command == "quit":
        break

    else:
        print("Sorry I don't understand that")
