
import unittest
import phone_book


class PhonebookTest(unittest.TestCase):

  def testThatPhoneBooKExist(self):
    self.assertIsNotNone(phone_book)

