
balance = 1000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    option = input("Choose an option: ")

    if option == '1':
        print(f"Your current balance is: ${balance}")
    elif option == '2':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Success! New balance: ${balance}")
    elif option == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! Remaining: ${balance}")
        else:
            print("Error: Insufficient funds!")
    elif option == '4':
        print("Session ended. Have a nice day!")
        break
    else:
        print("Invalid selection.")
