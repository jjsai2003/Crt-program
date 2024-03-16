class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def authenticate(self, user_id, pin):
        return user_id == self.user_id and pin == self.pin

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal of ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit of ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transfer of ${amount} to {recipient.user_id}")
            print(f"Transfer successful. Remaining balance: ${self.balance}")

# Example usage:
if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")
    
    atm = ATM(user_id, pin)

    if atm.authenticate(user_id, pin):
        print("Authentication successful.")
        while True:
            print("\nATM Options:")
            print("1. Display Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")
            
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                atm.display_transactions()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == '4':
                recipient_id = input("Enter recipient's user ID: ")
                amount = float(input("Enter amount to transfer: "))
                recipient = ATM(recipient_id, "")  # Creating temporary ATM object for recipient
                atm.transfer(amount, recipient)
            elif choice == '5':
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Authentication failed. Invalid user ID or PIN.")
