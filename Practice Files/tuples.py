#tuples are unchangeable

numbers = [1, 2, 3]   #array

number = (1, 2, 3)  #only count and index are available

print(number[0])

# number[0] = 2     #Cant change tuple, better to use if you dont want someone to change your array

coordinates = (1, 2, 3) # suppose x, y, z

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

#or

x, y, z = coordinates #called unpacking(it can also be done with an array or list)

print(x)