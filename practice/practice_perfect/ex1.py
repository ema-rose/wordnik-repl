def factorial(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total
print factorial(6)
