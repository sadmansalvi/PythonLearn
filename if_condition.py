is_hot = False
is_cold = False

if is_hot: #: triggers an indent
    print("It's a hot day")
    print("Drink Plenty of water")    #these two lines are indented so will be printed on condition of is_hot

elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day")
print("Enjoy your day") #shift+tab will untrigger the indent