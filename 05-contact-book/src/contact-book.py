import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contact(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding= "utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
                
        else:
            return []
        
    def save_contact(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file, indent= 4, ensure_ascii= False)

    def add_contact(self, name, phone, email, group):
        new_id = 1 if not self.contacts else self.add_contact[-1]["id"] + 1
        new_contact = {
            "id" : new_id,
            "name" : name,
            "phone" : phone,
            "email" : email,
            "group" : group
        }
        self.contacts.append(new_contact)
        self.save_contact()
        print("add contact seccesfully")
        