while True:
    name = input("\nEnter student name (type 'quit' to stop): ")
    
    if name.lower() == 'quit':
        break
        
    score = int(input(f"Enter marks for {name} (0-100): "))
    
    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 50:
        grade = "B"
    elif score >= 35:
        grade = "Pass"
    else:
        grade = "Fail"
        
    print(f"Student: {name} | Grade: {grade}")

print("All records updated.")
