#use 'try' construct to handle errors
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0!!!')
except ValueError:
    print('Invalid Value')

#but we don't want to crash our program just because some user passed a string instead of
#a number, with exit code 1, we want to show a proper error message to the user


