# Define three numbers
a = 15
b = 42
c = 27

# Method 1: Using the built-in max function (Recommended)
biggest = max(a, b, c)

# Method 2: Using conditional logic
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print(f"The biggest number is: {biggest}")
