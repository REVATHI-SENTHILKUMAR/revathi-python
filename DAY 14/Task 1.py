1. If Else

score = 85

if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")


2. Match Case

day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a weekday.")

3. While Loop

count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

4. For Loop

fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

5. List Datatype

students = ["sankar", "pranav", "geetha", "bala"]

print("Student List:", students)
print("First student:", students[0])


6. Function with Parameter and Return Type
python
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 10)
print(f"The area of the rectangle is: {result}")

