import os
import uuid
import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(
            data['account_number'],
            data['name'],
            data['balance']
        )

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, initial_deposit, name):
        account_number = str(uuid.uuid4())
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"\n✅ Account created! Account Number: {account_number}\n")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f'\nAccount Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance:.2f}\n')
        else:
            print('❌ Account not found.')

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"✅ ${amount:.2f} deposited. New balance: ${account.balance:.2f}")
            else:
                print("❌ Deposit amount must be positive.")
        else:
            print("❌ Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"✅ ${amount:.2f} withdrawn. Remaining balance: ${account.balance:.2f}")
            else:
                print("❌ Insufficient funds or invalid amount.")
        else:
            print("❌ Account not found.")

    def save_to_file(self):
        with open('accounts.txt', 'w') as file:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, file, indent=4)

    def load_from_file(self):
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as file:
                try:
                    data = json.load(file)
                    self.accounts = {acc_num: Account.from_dict(acc_data) for acc_num, acc_data in data.items()}
                except json.JSONDecodeError:
                    self.accounts = {}

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("""
        ==== Welcome to Python Bank ====
        1. Create Account
        2. View Account
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        """)

        try:
            ch = int(input('Enter your choice (1-5): '))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 5.")
            continue

        if ch == 1:
            name = input('Enter a name: ')
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(initial_deposit, name)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif ch == 2:
            acc_num = input('Enter your account number: ')
            bank.view_account(acc_num)

        elif ch == 3:
            acc_num = input('Enter your account number: ')
            try:
                amount = float(input('Enter amount to deposit: '))
                bank.deposit(acc_num, amount)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif ch == 4:
            acc_num = input('Enter your account number: ')
            try:
                amount = float(input('Enter amount to withdraw: '))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif ch == 5:
            print("👋 Thank you. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select between 1 and 5.")
