class InvalidAmountException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class InvalidPinException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class InsufficientFundsException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class Account:
    def __init__(self, firstName, secondName, pin) -> None:
        self.number = None
        if firstName and secondName:
            self.name = f"{firstName} {secondName}"
        self.pin = pin
        self.balance = 0

    def deposit(self, amountToBeDeposited: int):
        if self.is_valid_amount(amountToBeDeposited):
            self.balance += amountToBeDeposited
        else:
            raise InvalidAmountException("invalid amount to deposit")

    def withdraw(self, amountToBeWithdrawn, userPin):
        if self.is_valid(userPin, amountToBeWithdrawn):
            self.balance -= amountToBeWithdrawn

    def set_pin(self, userPin):
        if self.is_valid_pin(userPin):
            self.pin = userPin
        else:
            raise InvalidPinException("enter a valid pin")

    def get_pin(self):
        return self.pin

    def check_balance(self):
        return self.balance

    @staticmethod
    def is_valid_amount(amount: int) -> bool:
        if amount > 0:
            return True
        return False

    @staticmethod
    def is_valid_pin(pin):
        if pin and len(pin) <= 4:
            return True
        else:
            raise InvalidPinException("incorrect pin, please re-enter pin")

    def is_valid(self, userPin, amountToBeWithdrawn):
        if self.pin.lower() != userPin.lower():
            raise InvalidPinException("incorrect pin for the given account")
        if self.pin.lower() == userPin.lower() and 0 < amountToBeWithdrawn <= self.balance:
            return True
        else:
            raise InsufficientFundsException("insufficient funds, check your balance and try again")

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def __repr__(self):
        return f"account  {self.number}"
