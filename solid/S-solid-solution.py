import datetime

class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class DepositService:
    def __init__(self, account: Account):
        self.account = account

    def execute(self, amount):
        self.account.balance += amount

class WithdrawService:
    def __init__(self, account: Account):
        self.account = account

    def execute(self, amount):
        if self.account.balance < amount:
            print ("Saldo insuficiente")
            return
        else:
            self.account.balance -= amount
            print ("Retiro exitoso!")
            return

class StatementService:
    def __init__(self, account: Account):
        self.account = account

    def execute(self):
        statement = f"Statement for Account: {self.account_number}\nBalance: {self.balance}\n"

        print(statement)

        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.account_number}\n"
            )
        print(f"Sending email with statement for account {self.account_number}...")
        return

class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, initial_balance):
        self.accounts.append(Account(account_number, initial_balance))
        return print ("Cuenta creada con exito!")


    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                deposit_service = DepositService(account)
                DepositService.execute(amount)
            else:
                print ("Cuenta Invalida!")
                return

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                withdraw_service = DepositService(account)
                WithdrawService.execute(amount)
            else:
                print ("Cuenta Invalida!")
                return 
            
    def status(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                statementservice = StatementService(account)
                StatementService.execute()
            else:
                print ("Cuenta Invalida!")
                return 
            
acc_num = input ("Ingrese un numero de cuenta: ")
acc_bal = input ("Ingrese un balance inicial de cuenta: ")

acc_num = float(acc_num)
acc_bal = float(acc_bal)

cuenta = BankSystem()
cuenta.create_account(acc_num, acc_bal)