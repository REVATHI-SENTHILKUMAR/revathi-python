def print_diamond(n=3):
    for i in range(n):
        print(" " * (n - i - 1) * 7 + "*      " * (i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) * 7 + "*      " * (i + 1))

print_diamond()
