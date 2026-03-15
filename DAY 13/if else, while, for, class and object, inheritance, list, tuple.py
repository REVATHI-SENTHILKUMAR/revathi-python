#if-else
score = 55

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

#while

count = 1
while count <= 5:
    print(count)
    count += 1

#for

numbers = [1, 2, 3]

for num in numbers:
    print(f"Square of {num} is {num ** 2}")

#Class and Object

class Robot:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am revathi")

my_bot = Robot("Robo-1")
my_bot.greet()

class Robot:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am {self.name}!")

# Creating an object
my_bot = Robot("Robo-1")
my_bot.greet()


#Multilevel Inheritance
class Grandparent:
    def functionA(self):
        print("This is grandparent class")

class Parent(Grandparent):
    def functionB(self):
        print("This is parent class")

class Child(Parent): 
    def c(self)
     print("This is child class")

obj = Child()
obj.functionA()
obj.functionB()

#list
fruits = ["Apple", "Banana"]
fruits.append("Cherry") 
fruits[0] = "Strawberry" 
print(f"My List: {fruits}")

#tuple

colors = ("Red", "Green", "Blue")
print(f"My Tuple: {colors}")


