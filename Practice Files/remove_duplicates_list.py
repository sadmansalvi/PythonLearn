numbers = [5, 10, 100, 10, 2, 5, 7]


#My method
for item in numbers:
    if numbers.count(item) > 1:
        numbers.remove(item)

print(numbers)


# or Mosh's method

uniques =[]
for item in numbers:
    if item not in uniques:
        uniques.append(item)

print(uniques)
