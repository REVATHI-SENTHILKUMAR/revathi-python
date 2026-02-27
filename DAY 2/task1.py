a = 15
b = 42
c = 27

biggest = max(a, b, c)

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print(f"The biggest number is: {biggest}")
