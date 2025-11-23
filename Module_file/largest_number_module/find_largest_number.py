import utils
#or
from utils import find_max

numbers = [1, 2, 3, 10, -40, 6, 1000]

print(f"The maximum number on the array is {utils.find_max(numbers)}")

print(f"The maximum number on the array is {find_max(numbers)}")

