course = 'Python for beginners'
print(len(course)) # general purpose for counting

print(course.upper()) #upper is a method specific to strings (Uppercase)
print(course.lower())
print(course.find('o')) #Find characters "if not found will show pos -1"
print(course.find('beginners')) #gives the starting index

print(course.replace('beginners', 'absolute beginners'))  #Case sensitive

#Checking existence of characters (in operator)

print('Python' in course) # gives a boolean output
print('python' in course)