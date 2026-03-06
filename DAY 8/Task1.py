#1. No Parameter & No Return Value 

def total_1():
    p = float(input("Price: "))
    q = int(input("Qty: "))
    print(f"Total: {p * q}")

total_1()


#2. With Parameters & No Return Value

def total_2(p, q):
    print(f"Total: {p * q}")

total_2(10.5, 5)


#3. No Parameter & With Return Value

def total_3():
    p = float(input("Price: "))
    q = int(input("Qty: "))
    return p * q

result = total_3()
print(f"Total: {result}")

#4. With Parameters & With Return Value

def total_4(p, q):
    return p * q

result = total_4(20.0, 3)
print(f"Total: {result}")
