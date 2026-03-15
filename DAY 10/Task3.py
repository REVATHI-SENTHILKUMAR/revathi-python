available_seats = 3

while available_seats > 0:
    print(f"\nSeats remaining: {available_seats}")
    age = int(input("Enter your age (or 0 to cancel): "))
    
    if age == 0:
        break
    
    if age < 12:
        price = 5
        print(f"Child ticket: {price}")
    elif age >= 65:
        price = 7
        print(f"Senior ticket: {price}")
    else:
        price = 10
        print(f"Adult ticket: {price}")
    
    available_seats -= 1
    print("Ticket Booked Successfully!")

if available_seats == 0:
    print("\nHousefull! No more tickets available.")
