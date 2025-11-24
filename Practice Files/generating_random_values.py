import random #random is a builtin module

for i in range(3):
    print(random.random()) #prints random between 0 and 1

    print(random.randint(10,20))


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
