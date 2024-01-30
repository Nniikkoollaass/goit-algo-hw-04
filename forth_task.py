contacts={}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts: {}):
    try:
        name, phone = args
    except ValueError:
        print("Not enough values to unpack. Please, enter again your command to add contact correctly")
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: {}):
    try:
        name, phone = args
    except ValueError:
        print("Not enough values to unpack. Please, enter again your command to add contact correctly")
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts: {}):
    if len(contacts)==0:
        return "Your contacts database is empty!"
    else:
        try:
            name = args[0]
            if contacts.get(name) is None:
                return "Error: there is no such contact yet. Please, add it."
            else:
                return f"Phone number for user {name} is -> {contacts[name]}"
        except ValueError:
            print("Not enough values to unpack. Please, enter again your command to add contact correctly")

def show_all(contacts: {}):
    all_contacts=""
    if len(contacts)>0:
        count_number=1
        for name, number in contacts.items():
            all_contacts+=str(count_number)+" - "+name+" "+str(number)+"\n"
            count_number+=1
        return all_contacts
    else:
        return "Your contacts database is empty!"

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter your command: ")
        if user_input is not None:
            if  user_input in ["close", "exit"]:
                print("Good bye!")
                break
            elif user_input=="hello":
                print("How can I help you?")
            elif len(user_input)==0:
                print("You entered empty command! Please, try again.")
                continue
            else:
                entered_command, *args = parse_input(user_input)
                if entered_command=="add" \
                    and len(args)==2:
                    print(add_contact(args, contacts))
                elif entered_command=="change" \
                    and len(args)==2:
                    print(change_contact(args, contacts))
                elif entered_command=="phone" \
                    and len(args)==1:
                    print(show_phone(args, contacts))
                elif entered_command=="all" \
                    and len(args)==0:
                    print(show_all(contacts))
                else:
                    print("Invalid command.")

if __name__ == "__main__":
    main()              
