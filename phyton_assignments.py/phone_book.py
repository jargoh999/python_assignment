

import sys

class Phonebook:
    contacts = {}

    def add_contact(self, contact_name, phone_number):
        self.contacts[contact_name] = phone_number

    def search_contact(self, contact_name):
        if contact_name in self.contacts:
            return f"{contact_name} Number is {self.contacts[contact_name]}"
        return "this contact is not saved at the phonebook"

    def delete_contact(self, contact_name):
        if contact_name in self.contacts:
            del self.contacts[contact_name]

    def display_contacts(self):
        for contact, phone_number in self.contacts.items():
            print(contact + " <--> " + phone_number)

    def edit_contact(self, contact_name, phone_number):
        if contact_name in self.contacts:
            self.contacts[contact_name] = phone_number

    def display_menu(self):
        print("Select an option \n 1. save Contact \n 2. search Contact \n 3. delete Contact \n 4. Display Contacts \n 5. EditContact \n 6. BackToMenu")

    def main(self):
        self.display_menu()
        while True:
            options = int(input())
            if options == 1:
                print("enter the name of the contact to be saved")
                contact_name = input()
                print("enter a phonenumber to be saved")
                phone_number = input()
                self.add_contact(contact_name, phone_number)
                print("Saved successfully >>>>")
            elif options == 2:
                print("enter the name of the contact to be searched")
                contact_to_be_searched = input()
                print(self.search_contact(contact_to_be_searched))
            elif options == 3:
                print("enter the name of the contact to be deleted")
                contact_to_be_deleted = input()
                self.delete_contact(contact_to_be_deleted)
            elif options == 4:
                print("displaying your contacts")
                self.display_contacts()
            elif options == 6:
                print("thanks for your time")
                break
            elif options == 5:
                print("enter the contact name")
                contact_to_be_edited = input()
                print("enter new number")
                number_to_be_edited = input()
                self.edit_contact(contact_to_be_edited, number_to_be_edited)

            print("are you done?")
            verify = input()

            if verify.lower() == "yes":
                break
            elif verify.lower() == "no":
                self.display_menu()


phonebook = Phonebook()
phonebook.main()






