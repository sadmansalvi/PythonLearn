def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome Aboard")


first_name = input("What's your first name?")
last_name = input("What's your last name?")


print("Start")
#greet_user(first_name, last_name)
print("Finish")


#keyword argument

greet_user(last_name = 'Smith', first_name = 'John')

calc_cost(total = 50, shipping = 5, discount = 0.1)

#If you are mixing positional and keyword arguments then positional should be first
greet_user(last_name = 'Smith', 'John') # BAD PRACTICE