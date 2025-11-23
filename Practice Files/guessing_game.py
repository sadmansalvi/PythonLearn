number = 9

guess_count = 1

while guess_count <= 3:
    guess = int(input("Make a guess"))
    guess_count += 1
    if guess == number:
        print("You won!")
        break
else:
    print('You Failed')


