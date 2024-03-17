def main():
    """
    The function is controlling the cycle of command processing.
    """
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        #Getting the input from the user, firest word is a command, other words are arguments
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        #If there is a word "close" or "exit" in the command, the cycle is interrupted
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        #If the command is "hello", the bot greets the user
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(get_phone(args, contacts))
            
        elif command == "all":
            print(print_all_contacts(contacts))
            
            
        else:
            print("Invalid command.")
    
    
def parse_input(user_input) -> tuple:
    """Function is finding a command in the input and returns it"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts) -> str:
    """Function is adding a contact to the contacts dictionary. Returns a message about the result.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts) -> str:
    """Function is changing the phone number for the contact in the contacts dictionary. Returns a message about the result.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."
    
def get_phone(args, contacts) -> str:
    """Function is getting the phone number for the contact from the contacts dictionary. Returns a message about the result.
    """
    name = args[0]
    if name in contacts:
        return f"The {name} phone number is: {contacts[name]}"
    else:
        return "Contact not found."

def print_all_contacts(contacts) -> str:
    """Function is printing all contacts from the contacts dictionary. Returns a message about the result.
    """
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
            
        return "All contacts printed"
    else:
        return "No contacts found."
    
    


if __name__ == "__main__":
    main()