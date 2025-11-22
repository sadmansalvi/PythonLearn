numbers = [5, 2, 1, 1, 5, 7, 4]

numbers.append(20)

print(numbers)  #adds to last place

numbers.insert(0, 10)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.pop() #removes last item
print(numbers)

print(numbers.index(5)) # first appearance index

# or

print(5 in numbers) # boolean value output (much saver)

print(numbers.count(5))

numbers.sort()     #cant use print together with it as it will return none
print(numbers)
numbers.reverse() #descending order after sorting
print(numbers)

numbers2 = numbers.copy()

numbers.append(10)
print(numbers2)

numbers.clear()
print(numbers)


