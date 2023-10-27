from collections import UserDict
from exceptions import *
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
           raise PhoneValueError
        super().__init__(value)

    def is_valid(self, value):
        return value.isdigit() and len(value) == 10

class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            raise BirthdayValueError

class Record:
    def __init__(self, name, date_of_birth = None):
        self.name = Name(name)
        self.birthday = None if date_of_birth == None else Birthday(date_of_birth)
        self.phones = []
    
    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)

    def find_phone(self, number):
        phones = list(filter(lambda x: x.value == number, self.phones))
        if len(phones) == 0:
            raise KeyError
        return phones[0]

    def remove_phone(self, number):
        phone = self.find_phone(number)
        self.phones.remove(phone)
    
    def edit_phone(self, number, new_number):
        self.remove_phone(number)
        self.add_phone(new_number)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def record_exists(self, name):
        try:
            self.find(name)
            return True
        except:
            return False
    
    def find(self, name):          
        records = list(map(lambda x: self.data[x] , filter(lambda x: x == name, self.data)))
        if len(records) == 0:
            raise RecordDoesNotExistError
        return records[0]
    
    def delete(self, name):
        record = self.find(name)
        self.data.pop(record.name.value)

'''
#Example:
 # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

john_record.add_birthday("01.01.2000")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
'''
