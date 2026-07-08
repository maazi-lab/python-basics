

class InsufficientFundsError(Exception):
    pass
class Account:
    def __init__(self, account_name, account_number, balance, **kwargs):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.more_details = kwargs
        self.transactions = []
    
    def deposit(self, *args):
        total_deposit = 0
        for amount in args:
            total_deposit += amount
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"Deposited: {total_deposit}. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"Withdrew: {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    def get_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
        
    def display_summary(self):
        print("=" * 50)
        print("ACCOUNT SUMMARY")
        print("=" * 50)
        print(f"Account Name: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        for key, value in self.more_details.items():
            print(f"{key}: {value}")
        print("=" * 50)
        print("TRANSACTION HISTORY")s
        print("=" * 50)
        for transaction in self.transactions:
            print(transaction)
        print("=" * 50)
try:
    account = Account("John Doe", "12345", 1000, address="Lagos", phone="08012345678", email="john@email.com")
    account.deposit(500, 300, 200)
    account.withdraw(400)
    account.check_balance()
    account.display_summary()
except InsufficientFundsError as e:
    print(f"Error: {e}")
    

# Another bank system project
class IvalidAmountError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass
def deposit(balance, amount):
    try:
        if amount <= 0:
            raise IvalidAmountError("Deposit amount must be greater than zero.")
        balance += amount
    except IvalidAmountError as mrak:
        print("Bank says:", mrak)
    else:
        print(f"Deposited {amount}. New balance: {balance}")
    finally:
        print("Transaction completed.")
    return balance
# withdraw function
def withdraw(balance, amount):
    try:
        if amount <= 0:
            raise IvalidAmountError("Withdrawal amount must be greater than zero.")
        if amount > balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        balance -= amount
    except IvalidAmountError as mrak:
        print("Bank says:", mrak)
    except InsufficientFundsError as e:
        print("Bank says:", e)
    else:
        print(f"Withdrew {amount}. New balance: {balance} Naira")
    finally:
        print("Transaction completed.")
    return balance
# account bank acount

def bank_account(owner, **details):
    print(f"\n Welcome to MrakTech Bank!")
    print(f"Account owner: {owner}")
    print(f"Account type: {details.get('account_type', 'Savings')}")
    print(f"Opening balance: {details.get('balance', 0)} naira")    