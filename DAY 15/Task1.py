class AgeException(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeException("Age must be 18 or above")
    print("You are eligible to vote")

except AgeException as e:
    print("Exception:", e)
