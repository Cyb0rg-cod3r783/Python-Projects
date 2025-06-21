# Contact-Book using dictionary

# build a CLI based contact book where user can:

# 1. Add new contacts
# 2. View all contacts 
# 3. Search by name 
# 4. Delete contacts

import argparse 
import json 
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        if os.path.getsize(CONTACTS_FILE) == 0:
            return {}
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts to a file
def save_contacts(contacts):
    if os.path.exists(CONTACTS_FILE):
        with open("contacts.json", "w") as file:
            json.dump(contacts,file)


print("For adding a contact write 'python script_name add contact_name contact_number' in the terminal\n")
print("For removing a contact write 'python script_name remove contact_name contact_number' in the terminal\n")
print("For veiwing all contacts write 'python script_name view' in the terminal\n")
print("For searching a contact write 'python script_name search contact_name' in the terminal\n")

parser = argparse.ArgumentParser(description= "Contact Book")

parser.add_argument("action", choices = ["add", "remove", "view", "search"], help = "Enter what you want to do")
parser.add_argument("--contactName", type = str, help = "Enter the contact name")
parser.add_argument("--contactNumber", type = int, help = "Enter the contact number")

args = parser.parse_args()

contacts = load_contacts()

if (args.action == "add"):
    if args.contactName and args.contactNumber:
        contacts[args.contactName] = args.contactNumber
        save_contacts(contacts)
        print("Contact Added Successfully!!")
    else:
        print("Both --contactName and --contactNumber are required for adding.")

elif(args.action == "remove"):
    if args.contactName in contacts:
        del contacts[args.contactName]
        save_contacts(contacts)
        print("Contact Removed Successfully!")
    else:
        print("Contact Not Found")

elif(args.action == "view"):
    if contacts:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"{name} : {number}")
    else:
        print("No contacts found")

elif(args.action == "search"):
    if args.conatactName in contacts:
        print(f"{args.contactName} : {contacts[args.contactName]}")
        json.loads(contacts)
    else:
        print("No Such Contact Found!")

else:
    print("Invalid action entered")


# json.dump(obj, file)	Saves JSON data to a file
# json.dumps(obj)	Converts to JSON string in memory
# json.load(file)	Loads JSON from a file
# json.loads(string)	Parses JSON string from memory