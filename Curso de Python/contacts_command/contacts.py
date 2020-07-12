# -*- coding: utf-8 -*- 

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBoook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                 self._print_contact(contact)
                 break
        else:
            self._not_found(contact)

    def _not_found(self, contact):
        print('-----------------------------')
        print('The contact doesnt exist')
        print('-----------------------------')

    def _print_contact(self, contact):
        print('-----------------------------')
        print('Name {} '.format(contact.name))
        print('Phone {} '.format(contact.phone))
        print('Email {} '.format(contact.email))
        print('-----------------------------')

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


def main():

    contact_book = ContactBoook()

    with open('contacts.csv', "rt", encoding="utf8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if row == []:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''Type a command to continue:  
        
            [a] Add Contact
            [u] Update Contact
            [s] Search Contact
            [d] Delete Contact
            [L] List Contact
            [e] Exit
        '''))

        if command == 'a':
            print('Add Contact')
            name = str(input('Type a contact name  '))                
            phone = str(input('Type a phone number  '))
            email = str(input('Type a email contact  '))

            contact_book.add(name,phone,email)

        elif command == 'u':
            print('Update Contact')

        elif command == 's':
            print('Search Contact')
            name = str(input('Type a contact name  '))
            contact_book.search(name)

        elif command == 'd':
            print('Delete Contact')  
            name = str(input('Type a contact name  '))
            contact_book.delete(name)     

        elif command == 'l':
            print('List Contact')
            contact_book.show_all()

        elif command == 'e':
            print('Exit')
            break
        
        else:
            print('Comand not found   ')


if __name__ == '__main__':
    main()
    