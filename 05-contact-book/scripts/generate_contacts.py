from faker import Faker
import random
import json
import argparse
import os

fake = Faker()
group = ["family", "friend", "work", "other"]

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=100, help="Number of contacts to generate")
args = parser.parse_args()

contacts = []

for i in range(1, args.n + 1):
    contact = {
        "id" : i,
        "name" : fake.name(),
        "phone" : fake.phone_number(),
        "email" : fake.email(),
        "group" : random.choice(group)
    }
    contacts.append(contact)

base_dir = os.path.dirname(__file__)

file_path = os.path.join(base_dir, "../data/contacts.json")

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=4, ensure_ascii=False)

print("contact.json create succesfully")