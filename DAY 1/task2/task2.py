# Taking input for five subjects
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 =int(input("Enter marks for Subject 5: "))

# Calculating Sum
total_sum = sub1 + sub2 + sub3 + sub4 + sub5

# Calculating Average
average = total_sum / 5

# Displaying the results
print("-" * 30)
print(f"Total Sum: {total_sum}")
print(f"Average Marks: {average}")
