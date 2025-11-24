from pathlib import Path

#Absolute path
#c:\Program Files\Microsoft
#/usr/local/bin    in mac

#Relative Path

path = Path()# returns a path object #if nothing inside parentheses it will indicate current directory
print(path.exists()) #returns a boolean

#path.mkdir("ema") #makes directory named ema

for file in path.glob('*.py'):    #searching files
    print(file)

for file in path.glob('*'):    #searching files and directories
    print(file)

