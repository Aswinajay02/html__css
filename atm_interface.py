from flask import Flask, render_template, request

app = Flask(__name__)

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance:.2f}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}"

atm = ATM()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == '1':
            message = atm.check_balance()
        elif choice == '2':
            amount = float(request.form['amount'])
            message = atm.deposit(amount)
        elif choice == '3':
            amount = float(request.form['amount'])
            message = atm.withdraw(amount)
    return render_template('index.html', balance=atm.balance, message=message)

if __name__ == '__main__':
    app.run(debug=True)
