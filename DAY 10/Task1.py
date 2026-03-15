print("--- Welcome to Python Cafe ---")

while True:
    print("\nMenu:")
    print("1. Idly")
    print("2. Dosa")
    print("3. Poori")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("Selection: Hot Idly served")
    elif choice == '2':
        print("Selection: Crispy Dosa served")
    elif choice == '3':
        print("Selection: Poori Masala served")
    elif choice == '4':
        print("Thank you! Visit again. ")
        break  # Stops the loop
    else:
        print("Invalid choice. Please select 1 to 4.")


