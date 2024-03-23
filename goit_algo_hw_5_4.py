
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        
    return inner

@input_error 
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error   
def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error 
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise ValueError
    contacts[name] = new_phone
    return f"Phone number for {name} changed."   
    
    
@input_error 
def show_phone(args, contacts):
    if len(args) < 1:
        return "Please provide a contact name."
    key = args[0]
    if key in contacts:
        value = contacts.get(key)
        return value
    else:
        return "Contact not found."

@input_error     
def show_all(contacts):
    for key, value in contacts.items():
        print(key, value)

def main():
    contacts = {}
    
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
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()