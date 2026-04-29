import json
import pandas as pd 

class Contact:
  def __init__(self, name, phone, email):  
    self.name = name
    self.phone = phone
    self.email = email
    

  def to_dict(self):
     return{"name":self.name, "phone":self.phone, "email":self.email}
 
contacts = []

def save_contacts():
 with open("contacts.json", "w") as f:
   json.dump([c. to_dict() for c in contacts], f)


def load_contacts():
   global contacts  
   try:
      with open("contacts.json", "r") as f:
            contacts = [Contact(c["name"], c["phone"],  c["email"]) for c in json.load(f)]
   except FileNotFoundError:
         pass

def add_contact():
   name = input("Enter name:")
   phone = input("Enter phone:")
   email = input("Enter email:")
   contacts.append(Contact(name, phone, email))
   save_contacts()
   print("Contact added successfully!")

def view_contacts():
   if not contacts:
      print("No contacts found.")
   else:   
       df = pd.DataFrame([c. to_dict() for c in contacts])
       print(df)

def search_contact():
   name = input("Enter name to serach:")
   for contact in contacts:
       if contacts.name == name:
          print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
       return
   print("Contact not found.")

def delete_contact():
   name = input("Enter name to delete:")
   for contact in contacts:
      if contact.name == name:
        contacts.remove(contact)
        save_contacts()
        print(f"Contact {name} deleted successfully!")
        return
   print("Contact not found.")

def show_menu():
      print("1. Add contact")
      print("2. View contact")
      print("3. Search contact")
      print("4. Delete contact")
      print("5. Quit")

load_contacts()

while True:
   show_menu()
   choice = input("Enter your choice:")
   if choice == "1":
      add_contact()
   elif choice == "2":
      view_contacts()
   elif choice == "3":
      search_contact()
   elif choice == "4":
      delete_contact()
   elif choice == "5":
      print("Goodbye!")
      break
   else:
      print("Invalid choice.Please try again")




       
   

