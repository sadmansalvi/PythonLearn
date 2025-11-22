numbers = [10, 20, -4, 23, 100]

maximum = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]


print(f"Maximum number is {maximum}")
