"""
    User Interface Modul
"""

import address_book
import notes
import files

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"

def help():
    print(f' List of comand:\n'
            f'{YELLOW} add {BLUE} - add contact to phone book\n'
            f'{YELLOW} all {BLUE} - show all records\n'
            f'{YELLOW} add tel {BLUE} - add phone number to record with Name\n'
            f'{YELLOW} delete {BLUE} - delete record from list\n'
            f'{YELLOW} find {BLUE} - search for records by part of a name or phone number\n'
            f'{YELLOW} help {BLUE} - help\n'
            f'{YELLOW} exit  {BLUE} - exit from program\n{RESET}')

def start_bot():
    print(f'{YELLOW}Hello! I`m your personal assistant! To finish working please enter "exit". To view all commands please enter "Help"{RESET}')

    filename = "files\\save_contacts.bin"
    try:
        book = address_book.read_from_file(filename)
    except Exception:
        book = address_book.AddressBook()

    while True:
        data = input(">").lower()
        if data == "exit":
            book.save_to_file(filename)
            break
        elif data == "help":
            help()
        elif data == "add":
            name = input("Enter name :")
            if (name):
              record = address_book.Record(name)
              phone = input('Enter phone number (or press "Enter" to continue):')
              if phone:
                  record.add_phone(phone)
              birthday = input('Enter date of birth [DD-MM-YYYY](or press "Enter" to continue):')
              if birthday:
                  record.add_birthday(birthday)
              book.add_record(record)
        elif data == "add tel":
            name = input("Enter name :")
            if (name):
                rec = book.find(name)
                if rec:
                   phone = input("Enter phone number:")
                   rec.add_phone(phone)
                else:
                  print(f"The name {name} was not found in the address book")

        elif data=="delete":
            name = input("Enter name :")
            if (name ):
              nam=book.delete(name)
              if nam:
                 print(f"{nam} deleted from address book")
              else:
                 print(f"The name {name} was not found in the address book")
        elif data == "find":
             f=input("Enter text for searching (part of name or phone number):")
             book.get_find(f)

        elif data == "all":
            n=-1
            if len(book.data.items())>10:
                n=10
            book.get_all(n)
        else:
            print(f'The command "{data}" not defined')


#start_bot()