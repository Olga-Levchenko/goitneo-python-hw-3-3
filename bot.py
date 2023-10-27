from address_book import *
from birthdays import get_birthdays_per_week

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError:
            return {
                "parse_input": "Invalid command.",
                "add_contact": "Give me name and phone please.",
                "change_contact": "Give me name and phone please.",
                "show_phone": "Give me name please.",
                "add_birthday": "Give me name and birthday please.",
                "show_birthday": "Give me name please."
            }[func.__name__]
        except (RecordAlreadyExistsError, RecordDoesNotExistError, PhoneValueError, BirthdayValueError) as e:
            return e.message
        except KeyError:
            return "Name not found."

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if contacts.record_exists(name):
        raise RecordAlreadyExistsError  
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contact = contacts.find(name)
    contact.add_phone(phone)
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) == 0:
        raise ValueError
    name = args[0]
    contact = contacts.find(name)
    return contact.__str__()

def show_all(contacts):
    return "\n".join(map(lambda x: contacts.find(x).__str__(), contacts))

@input_error
def add_birthday(args, contacts):
    name, date = args
    contact = contacts.find(name)
    contact.add_birthday(date)
    return "Birthday is added."

@input_error
def show_birthday(args, contacts):
    if len(args) == 0:
        raise ValueError
    name = args[0]
    contact = contacts.find(name)
    return contact.birthday

def show_birthdays_next_week(contacts):
    return get_birthdays_per_week(map(lambda x: { "name": x, "birthday": contacts.find(x).birthday.value}, contacts))

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        command, *args = parse_input(user_input)        

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(show_birthdays_next_week(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()