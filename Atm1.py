import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        messagebox.showinfo("Balance", "Your balance is: ${}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        messagebox.showinfo("Deposit", "${} deposited. Your new balance is: ${}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            messagebox.showerror("Error", "Insufficient funds. Your balance is: ${}".format(self.balance))
        else:
            self.balance -= amount
            messagebox.showinfo("Withdraw", "${} withdrawn. Your new balance is: ${}".format(amount, self.balance))

def check_balance():
    atm.check_balance()

def deposit():
    amount = float(amount_entry.get())
    atm.deposit(amount)
    amount_entry.delete(0, tk.END)

def withdraw():
    amount = float(amount_entry.get())
    atm.withdraw(amount)
    amount_entry.delete(0, tk.END)

def quit():
    window.quit()

atm = ATM()

window = tk.Tk()
window.title("ATM Machine")

label = tk.Label(window, text="ATM Machine", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=2, pady=10)

balance_button = tk.Button(window, text="Check Balance", command=check_balance)
balance_button.grid(row=1, column=0, padx=10, pady=5)

deposit_button = tk.Button(window, text="Deposit", command=deposit)
deposit_button.grid(row=1, column=1, padx=10, pady=5)

withdraw_button = tk.Button(window, text="Withdraw", command=withdraw)
withdraw_button.grid(row=2, column=0, padx=10, pady=5)

amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=2, column=1, padx=10, pady=5)

amount_entry = tk.Entry(window)
amount_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

quit_button = tk.Button(window, text="Quit", command=quit)
quit_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
