# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements (just like a list)
print(fruits[0])  # Output: apple



#The "Immutable" Rule
coordinates = (10, 20)

# This will cause an error:
# coordinates[0] = 15



to assign multiple variables at once. 
# Packing a tuple
person = ("Alice", 25, "Engineer")


# Unpacking the tuple into variables
name, age, profession = person


print(name)        # Output: Alice
print(profession)  # Output: Engineer


not_a_tuple = ("apple")  # This is a String
is_a_tuple = ("apple",)  # This is a Tuple
