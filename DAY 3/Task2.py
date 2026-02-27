try:
    
    mark = float(input("Enter the student's mark: "))

    if 90 <= mark <= 100:
        print("Grade A")
    elif 80 <= mark <= 89:
        print("Grade B")
    elif 70 <= mark <= 79:
        print("Grade C")
    else:
        print("invalid mark")
except ValueError:
    print("invalid mark")
