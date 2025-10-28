import functools

def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Обробляє KeyError, ValueError, IndexError.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт.
    Викликає ValueError, якщо аргументів не 2.
    """
    name, phone = args  # Викличе ValueError, якщо args < 2
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Змінює існуючий контакт.
    Викликає ValueError, якщо аргументів не 2.
    Викликає KeyError, якщо ім'я не знайдено.
    """
    name, new_phone = args  # Викличе ValueError, якщо args < 2
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError  # Явно викликаємо KeyError, щоб декоратор його зловив

@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону для контакту.
    Викликає IndexError, якщо ім'я не надано.
    Викликає KeyError, якщо ім'я не знайдено.
    """
    name = args[0]  # Викличе IndexError, якщо args порожній
    return contacts[name]  # Викличе KeyError, якщо name не в contacts

def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts found."
    
    # Форматуємо вивід: кожен контакт з нового рядка
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main():
    """
    Головна функція бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            # Це спрацює, якщо користувач введе лише пробіли
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

