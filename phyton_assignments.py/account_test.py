from account import *

import unittest


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account("ayo", "fatoye", "1234")

    def test_deposit_negative_value_balance_is_unchanged(self):
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(-1)
        self.assertEqual(0, self.account.check_balance())

    def test_deposit_positive_value_balance_is_increased(self):
        self.account.deposit(100)
        self.assertEqual(100, self.account.check_balance())

    def test_withdraw_amount_greater_than_balance(self):
        self.account.deposit(100)
        self.account.set_pin("1234")
        with self.assertRaises(InvalidPinException):
            self.account.withdraw(120, "12345")
        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(120, "1234")

    def test_set_invalid_pin_throws_an_exception(self):
        with self.assertRaises(InvalidPinException):
            self.account.set_pin("12345")

    def test_set_valid_pin_sets_pin(self):
        self.account.set_pin("1234")
        self.assertEqual("1234", self.account.get_pin())

    def test_that_balance_can_be_checked(self):
        self.assertEqual(0, self.account.check_balance())
        self.account.deposit(100)
        self.assertEqual(100, self.account.check_balance())

    def test_that_account_number_is_valid(self):
        self.account.set_number(1234567891)
        self.assertEqual(1234567891, self.account.get_number())
