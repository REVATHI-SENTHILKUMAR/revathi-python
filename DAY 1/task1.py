class Customer:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def display_details(self):
        print(f"{self.account_num:<15} {self.name:<20} ${self.balance:<10.2f}")

def main():
    customers = []
    
    print("--- Bank Customer Entry System ---")
    try:
        num_customers = int(input("How many customers do you want to add? "))
        
        for i in range(num_customers):
            print(f"\nEnter details for Customer {i+1}:")
            name = input("Enter Name: ")
            acc_no = input("Enter Account Number: ")
            bal = float(input("Enter Initial Balance: "))
            
            # Create a new Customer object and add to list
            obj = Customer(name, acc_no, bal)
            customers.append(obj)

        # Displaying the results
        print("\n" + "="*50)
        print(f"{'Account No':<15} {'Name':<20} {'Balance':<10}")
        print("-" * 50)
        
        for cust in customers:
            cust.display_details()
            
        print("="*50)

    except ValueError:
        print("Invalid input! Please enter numbers for the count and balance.")

if __name__ == "__main__":
    main()
