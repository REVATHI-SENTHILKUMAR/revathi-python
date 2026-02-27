level1_score = float(input("Enter Level 1 score: "))

if level1_score > 7:
    print("Level 1 round is clear")
    
    level2_score = float(input("Enter Level 2 score: "))
    
    if level2_score > 8:
        print("You are selected")
    else:
        print("Rejected in Level 2")
        
else:
    print("Rejected in Level 1")
