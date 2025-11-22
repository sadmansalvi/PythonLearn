weight = float(input("Whats your weight: "))

decision = input("(L)bs or (K)g: ")


if decision.upper() == "L":
    weight_converted = weight * 0.45
elif decision.upper() == "K":
    weight_converted = weight * 2.2

print(f"Your weight is {weight_converted}")