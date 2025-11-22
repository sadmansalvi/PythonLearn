name = input("What's your name?\n")

if len(name) < 3 or len(name) >50:
    print("Must be 3-50 character")
else:
    print("Name looks good!")
