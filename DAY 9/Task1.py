#1. No Parameter & No Return type 

nums = [25, 95, 65, 78, 86]

def find_max_type1():
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    print("Biggest:", biggest)

find_max_type1()


#2. With Parameters & No Return type

def find_max_type2(lst):
    biggest = lst[0]
    for n in lst:
        if n > biggest:
            biggest = n
    print("Biggest:", biggest)

find_max_type2([25, 95, 65, 78, 86])

#3. No Parameter & With Return type
nums = [25, 95, 65, 78, 86]

def find_max_type3():
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

res = find_max_type3()
print("Biggest:", res)


#4. With Parameters & With Return type

def find_max_type4(lst):
    biggest = lst[0]
    for n in lst:
        if n > biggest:
            biggest = n
    return biggest

res = find_max_type4([25, 95, 65, 78, 86])
print("Biggest:", res)
