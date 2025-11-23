course = "Python for beginners"

print(course[0])

#You can also use negative indices in python which may not be available in other programming languages whatsoever

print(course[-1]) #This will give the last character

print(course[0:2]) #multiple characters will print 0 to 1 but not the last one - 2

print(course[0:len(course)]) # it will give whole

print(course[0:]) # Also whole

print(course[: 5])  # take 0 as default start

another = course[:] # copies a string to new var

print(course[1:-1])

