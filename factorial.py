def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
x = 5
print("Factorial of", x, "is", factorial(x))