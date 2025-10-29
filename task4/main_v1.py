# -- Version 1 of code --
# These version is based on the messages from previous task in hm3
# The main difference (from v2) is in "def inner" block
import functools
# Without functools.wraps, decorated functions will lose their original identity.

def input_error(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # The reason: message for ValueError for add_contact and change_contact is different
        except ValueError as e:
            return str(e) 
        except KeyError as e:
            return str(e)
        except IndexError as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):   
    if len(args) != 2: # ValueError if args < 2
        raise ValueError("Invalid arguments. Usage: add [name] [phone]")
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2: # ValueError if args < 2
        raise ValueError("Invalid arguments. Usage: change [name] [new_phone]")

    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError(f"Contact '{name}' not found.")    # KeyError if name not found

@input_error
def show_phone(args, contacts):
    if len(args) != 1:  # IndexError if name not entered (args empty)
        raise IndexError("Invalid arguments. Usage: phone [name]")
        
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError(f"Contact '{name}' not found.")    # KeyError if name not found 

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("Invalid command. Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

