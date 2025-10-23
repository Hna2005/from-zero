import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
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
        new_id = 1 if not self.contacts else self.contacts[-1]["id"] + 1
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
        
    def view_contact(self):
        if not self.contacts:
            print("contact list is empty!")
            return
        else:
            print("\n Contact List:")
            print("-" * 80)
            print(f"{'ID':<5}{'Name':<20}{'Phone':<15}{'Email':<25}{'Group':<15}")
            for c in self.contacts:
                print(f"{c['id']:<5}{c['name']:<20}{c['phone']:<15}{c['email']:<25}{c['group']:<15}")
    
    def search_contact(self, keyword, field=None, exact=False):
        if not self.contacts:
            print("Contact list is empty!")
            return

        results = []

        for c in self.contacts:
            if field is None:
                if (
                    keyword.lower() in c["name"].lower()
                    or keyword.lower() in c["email"].lower()
                    or keyword in c["phone"]
                    or keyword.lower() in c["group"].lower()
                ):
                    results.append(c)

            else:
                value = str(c.get(field, "")).lower()
                key = keyword.lower()

                if exact:
                    if key == value:
                        results.append(c)
                else:
                    if key in value:
                        results.append(c)

        if not results:
            print(f"No results found for '{keyword}'.")
            return []

        print(f"\n🔍 Results for '{keyword}' ({field if field else 'all fields'}):")
        print("-" * 80)
        print(f"{'ID':<5}{'Name':<20}{'Phone':<15}{'Email':<25}{'Group':<15}")
        for c in results:
            print(f"{c['id']:<5}{c['name']:<20}{c['phone']:<15}{c['email']:<25}{c['group']:<15}")

        return results

    def update_contact(self, contact_id, name=None, phone=None, email=None, group=None):
        for c in self.contacts:
            if c["id"] == contact_id:
                if name:
                    c["name"] = name
                if phone:
                    c["phone"] = phone
                if email:
                    c["email"] = email
                if group:
                    c["group"] = group
                self.save_contact()
                print(f"Contact with ID {contact_id} updated successfully!")
                return
        
        print(f"No contact found with ID {contact_id}.")

    def delete_contact(self, contact_id):
        if not self.contacts:
            print("contact list is empty!")
            return
        
        for c in self.contacts:
            if c["id"] == contact_id:
                self.contacts.remove(c)
                self.save_contact()
                print(f"Contact with ID {contact_id} deleted successfully!")
                return
            
        print(f"No contact found with ID {contact_id}.")
