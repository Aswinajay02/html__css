class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print("Your balance is: ${}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("${} deposited. Your new balance is: ${}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Your balance is: ${}".format(self.balance))
        else:
            self.balance -= amount
            print("${} withdrawn. Your new balance is: ${}".format(amount, self.balance))

def main():
    atm = ATM()
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        choice = int(input("Enter choice (1-4): "))
        
        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
