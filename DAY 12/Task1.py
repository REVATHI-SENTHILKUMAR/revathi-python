# Define the blueprint (Class)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

#Method A: Using a List Literal
students = [
    Student("Revathi", 20),
    Student("Pranav", 22),
    Student("Geetha", 21)
]

#Method B: Using .append() in a loop
more_students = []
names = ["Revathi", "Pranav"]
for name in names:
    more_students.append(Student(name, 23))

print(students)
