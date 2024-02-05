import unittest
import phone_book1


class PhonebookTest(unittest.TestCase):

    def testThatPhoneBookExist(self):
        self.assertIsNotNone(phone_book1)

    def testThatPhoneBookCanAdd_contact(self):
        phone_book1.phonebook1.add_contact("ayo", "08171603814")
        self.assertEqual("ayo Number is 08171603814", phone_book1.phonebook1.search_contact("ayo"))

    def testThatphoneBookCanDelete_Contact(self):
        phone_book1.phonebook1.add_contact("dayo","27634352624")
        self.assertEqual("dayo Number is 27634352624",phone_book1.phonebook1.search_contact("dayo"))

    def testThatphoneBookCan_Contact_EditContact(self):
        phone_book1.phonebook1.add_contact("dayo", "27634352624")
        self.assertEqual("dayo Number is 27634352624", phone_book1.phonebook1.search_contact("dayo"))
        phone_book1.phonebook1.edit_contact("dayo","1234")
        self.assertEqual("dayo Number is 1234", phone_book1.phonebook1.search_contact("dayo"))

    def testThatphoneBookCan_Contact_DisplayContact(self):
        phone_book1.phonebook1.add_contact("dayo", "27634352624")
        self.assertEqual("dayo Number is 27634352624", phone_book1.phonebook1.search_contact("dayo"))
        phone_book1.Phonebook.delete_contact(phone_book1.phonebook1,"ayo")
        message = phone_book1.phonebook1.display_contacts()
        self.assertEqual("dayo <--> 27634352624",message)
