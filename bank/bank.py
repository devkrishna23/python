import random, datetime
from prettytable import PrettyTable


class LimitError(Exception):
    pass

class AccountNotFound(Exception):
    pass

class InvalidPinError(Exception):
    pass

class InvalidDateFormatError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class Bank:
    MAX_ACCOUNTS = 10000
    MIN_BALANCE = 100
    MIN_AGE = 18
    MAX_AGE = 80
    ACCOUNT_PREFIX = "230406"

    def __init__(self):
        self.accounts = {}
    
    def generate_account_number(self):
        while True:
            suffix = str(random.randint(0, 9999)).zfill(4)
            account_number = self.ACCOUNT_PREFIX + suffix
            if account_number not in self.accounts:
                break
        return account_number
    
    def generate_pin(self):
        return random.randint(1000, 9999)
    
    def transaction_log(self, account, type_of_txn, amount, time, note = ''):
        
        transaction = {
            "type": type_of_txn,
            "amount": amount,
            "time": time,
            "note": note
        }
        self.accounts[account]["transaction_history"].append(transaction)
    
    def validate_pin(self, account, pin):
        if pin != self.accounts[account]["pin"]:
            raise InvalidPinError("Invalid Pin")
        
    def validate_account(self, account):
        if account not in self.accounts:
            raise AccountNotFound("Account not found")
    
    def validate_amount(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount for deposit/withdrawal/transfer should be greater than 0")
    
    def validate_balance(self, account, amount):
        if self.accounts[account]["balance"] - amount  < self.MIN_BALANCE:
            raise InsufficientBalanceError(f"Balance after withdrawal/transfer should be more than ₹{self.MIN_BALANCE}")
    

    def account_creation(self, name, balance, dob, pin = None):

        if len(self.accounts) == self.MAX_ACCOUNTS:
            raise LimitError("Total account limit reached. Unable to create a new account.")

        try:
            dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
            today = datetime.date.today()
            age = today.year - dob_date.year - (
                (today.month, today.day) < (dob_date.month, dob_date.day)
            )

            if not (self.MIN_AGE <= age <= self.MAX_AGE):
                raise InvalidAgeError(f"Sorry account creation is only allowed between the ages of {self.MIN_AGE} and {self.MAX_AGE}")

            if balance < self.MIN_BALANCE:
                raise InvalidAmountError(f"Opening balance must be at least ₹{self.MIN_BALANCE}.")
            
            if pin is None or not (1000 <= pin <= 9999):
                pin = self.generate_pin()

            account_number = self.generate_account_number()
            created_at = datetime.datetime.now()
            self.accounts[account_number] = {
                "account_holder": name,
                "balance": balance,
                "transaction_history": [
                    {
                        "type": "Deposit",
                        "amount": balance,
                        "time": created_at,
                        "note": "Opening balance"
                    }
                ],
                "creation_time": created_at,
                "dob": dob_date,
                "pin": pin
            }
            return {
                "account_number": account_number,
                "pin": pin,
                "message": "✅ Account created successfully!"
            }
        except ValueError:
            raise InvalidDateFormatError("Invalid date format. Please use YYYY-MM-DD.")



    def deposit(self, account, pin, amount):
        self.validate_account(account)
        self.validate_pin(account, pin)
        self.validate_amount(amount)
        self.accounts[account]["balance"] += amount
        time = datetime.datetime.now()
        self.transaction_log(account, "Deposit", amount, time, "Cash deposit")
        return {
            "message": f"✅ ₹{amount} has been successfully deposited.",
            "balance": self.accounts[account]["balance"]
        }


    def withdrawal(self, account, pin, amount):
        self.validate_account(account)
        self.validate_pin(account, pin)
        self.validate_amount(amount)
        self.validate_balance(account, amount)
        self.accounts[account]["balance"] -= amount
        time = datetime.datetime.now()
        self.transaction_log(account, "Withdrawal", amount, time, "Cash withdrawal")
        return {
            "message": f"✅ ₹{amount} has been successfully withdrawn.",
            "balance": self.accounts[account]["balance"]
        }


    def transfer(self, account1, account2, pin, amount):
        self.validate_account(account1)
        self.validate_account(account2)
        self.validate_pin(account1 ,pin)
        self.validate_amount(amount)
        self.validate_balance(account1, amount)

        self.accounts[account1]["balance"] -= amount
        self.accounts[account2]["balance"] += amount
        time = datetime.datetime.now()
        self.transaction_log(account1, f"Transfer to {account2}", amount, time, "Cash transfer")
        self.transaction_log(account2, f"Transfer from {account1}", amount, time, "Cash transfer")
        return {
            "message": f"✅ ₹{amount} has been successfully transferred from {account1} to {account2}.",
            "balance_from": self.accounts[account1]["balance"],
            "balance_to": self.accounts[account2]["balance"]
        }
    
    def display_account_info(self, account, pin):
        self.validate_account(account)
        self.validate_pin(account, pin)
        acc = self.accounts[account]
        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        table.add_row(["Account Number", account])
        table.add_row(["Account Holder", acc["account_holder"]])
        table.add_row(["Balance", f"₹{acc['balance']}"])
        table.add_row(["Date of Birth", acc["dob"]])

        return table

    def display_balance(self, account, pin):
        self.validate_account(account)
        self.validate_pin(account, pin)
        return {"balance": self.accounts[account]["balance"],
        "message": f"💰 Your current balance is: ₹{self.accounts[account]['balance']}"}


    def display_transaction_history(self, account, pin):
        self.validate_account(account)
        self.validate_pin(account, pin)

        table = PrettyTable()
        table.field_names = ["Type", "Amount (₹)", "Time", "Note"]

        for transaction in self.accounts[account]["transaction_history"]:
            table.add_row([
                transaction['type'],
                f"{transaction['amount']}",
                transaction['time'].strftime('%Y-%m-%d %H:%M:%S'),
                transaction['note']
            ])
        
        return table
