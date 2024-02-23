from account import Account


class Bank:
    default_account_number = 14346785324

    def __init__(self):
        self.name = ""
        self.accounts = []

    def deposit(self, account_number, amount_to_be_deposited):
        for account in self.accounts:
            if account.number == account_number:
                account.deposit(amount_to_be_deposited)
                break

    def withdraw(self, account_number, amount_to_be_withdrawn, pin):
        for account in self.accounts:
            if account.number == account_number and account.pin == pin:
                account.withdraw(amount_to_be_withdrawn, pin)
                break

    def transfer(self, sender_account_number, recipient_account_number, amount_to_be_transferred, pin):
        for account in self.accounts:
            if account.number == sender_account_number and account.pin == pin:
                account.withdraw(amount_to_be_transferred, pin)
                break
        for account in self.accounts:
            if account.number == recipient_account_number:
                account.deposit(amount_to_be_transferred)
                break

    def check_balance(self, account_number_to_be_checked, pin):
        for account in self.accounts:
            if account.number == account_number_to_be_checked and account.pin == pin:
                return account.check_balance()
        return 0

    def register_customer(self, first_name, last_name, pin):
        account = Account(first_name, last_name, pin)
        number = Bank.default_account_number
        account.set_number(number)
        self.accounts.append(account)
        Bank.default_account_number += 1
        return account

    def remove_account(self, account_number_to_remove, pin):
        for account in self.accounts:
            if account.number == account_number_to_remove and account.pin == pin:
                self.accounts.remove(account)
                break

    def find_account(self, account_number_to_find):
        for account in self.accounts:
            if account.number == account_number_to_find:
                return account
        return None
    @staticmethod
    def main(self):
        Bank.register_customer("ayo2", "fatoye", "1234")
        Bank.register_customer("ayo1", "fatoye", "2345")
        print(Account.accounts)




