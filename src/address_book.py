"""
    Address Book Modul
"""
from collections import UserDict
from datetime import datetime
import pickle

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"

def read_from_file(file):
    with open(file, 'rb') as fh:
        return pickle.load(fh)

class Field:
    def __init__(self, value):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super.__init__(self,value)



class Phone(Field):
    def __init__(self, value):
        if int(value) and len(value)==10:
            self.value = value
        else:
            raise ValueError


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = value
            d = value.split("-")
            self.date=datetime(int(d[2]),int(d[1]),int(d[0]))
        except Exception as e: 
            raise ValueError


class Name(Field):
    def __init__(self, value):
        self.value = value


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
        if birthday:
            try:
                self.date = Birthday(birthday)
            except  ValueError:
                print('Please enter date of birth in string format "DD-MM-YYYY"')

    def add_birthday(self, birthday_s):
        try:
            self.value = birthday_s
            self.birthday = Birthday(birthday_s)
        except  ValueError:
            print(f'{birthday_s} Please enter date of birth in string format "DD-MM-YYYY"')

    def days_to_birthday(self):
        if self.birthday:
            current_datetime = datetime.now()
            dbirt = datetime(current_datetime.year, self.birthday.date.month, self.birthday.date.day)
            if current_datetime>dbirt:
                dbirt = datetime(current_datetime.year+1, self.birthday.date.month, self.birthday.date.day)

            days = dbirt - current_datetime
            print(f"{days.days} days before birthday of {self.name}")
        else:
            print(f"birthday of {self.name} is unknown")

    def add_phone(self, phone_s):
        try:
            self.phones.append(Phone(phone_s))
        except ValueError as e:
            if len(str(e))>0:
                print(f'{RED}{e}{YELLOW} - Phone number must consist of numbers only{RESET}')
            else:
                print(f'{RED}{phone_s}{YELLOW} - Phone number must consist of 10 numbers{RESET}')

    def edit_phone(self, old_phone, new_phone):
        n=0
        f=True
        for phone in self.phones:
            if phone.value == old_phone:
                f = False
                self.phones.pop(n)
                self.phones.insert(n,Phone(new_phone))
            n+=1
        if f:
            raise ValueError

    def remove_phone(self, phone):
        n = 0
        f = True
        try:
            for phon in self.phones:
                if phon.value == phone:
                    f = False
                    self.phones.pop(n)
                n += 1
            if f:
                raise ValueError
        except ValueError:
            print(f'{RED}{phone} {YELLOW} - not found{RESET}')

    def find_phone(self, num_phone):
        for phone in self.phones:
            if phone.value == num_phone:
                return phone

    def __str__(self):
        sp = f"{BLUE} phones:{YELLOW} {'; '.join(p.value for p in self.phones)}" if self.phones else ""
        sb = f",{BLUE} birthday: {YELLOW} {self.birthday}{RESET}" if self.birthday else ""
        return (f"{BLUE}Contact name:{YELLOW} {self.name.value} {sp} {sb}")


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value]=record

    def get_all_in_page(self, n=0):

        list_rec = []
        for name, record in self.data.items():
            list_rec.append(record)
        if n<=0:
            n=len(list_rec)

        def list_generator(n, x=0):
            y = n + x
            for l in list_rec[x:y]:
                print(l)
            if y >= len(list_rec):
                return
            
            if input("Press Enter to continue") == "":
                if (x + n) <= len(list_rec):
                    x = x + n
                    list_generator(n, x)

        list_generator(n)

    def get_find(self, found=""):
        for name, record in self.data.items():
            find_tel = 0
            for num in record.phones:
                if str(num).find(found)>=0:
                    find_tel = 1
            if (name.find(found) >= 0 or find_tel == 1):
                print(record)


    def get_some(self, x, y):
        i=0
        for name, record in self.data.items():
            if (x <= i and i <= y):
                print(record)
            i += 1

    def get_all(self, count = -1):
        if count == -1 or count > len(self.data.items()):
            a = len(self.data.items())
        else:
            a = count-1

        y = a
        self.get_some(0, y)
        while y < len(self.data.items()):
            if input("Press Enter to continue") == "":
                print("%" * 50)
                x=y+1
                y+=a+1
                self.get_some(x, y)

    def find(self, name):
        for nam, rec in self.data.items():
            if rec.name.value == name:
                return rec

    def delete(self, name):
        for nam, rec in self.data.items():
            if nam == name:
                del self[nam]
                return nam
        return None

    def save_to_file(self, filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self,fh)