from abc import ABC, abstractmethod
import string
import secrets

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinPassword(PasswordGenerator):
    def __init__(self, length=8):
        self.length = length

    def generate(self):
        return ''.join(secrets.choice(string.digits) for _ in range(self.length))
    

class RandomPassword(PasswordGenerator):
    def __init__(self, length=8, numbers=True, symbols=True):
        self.length = length
        self.characters = string.ascii_letters
        if numbers:
            self.characters += string.digits
        if symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join(secrets.choice(self.characters) for _ in range(self.length))
    
# ساختن آبجکت از کلاس‌ها
pin = PinPassword(length=6)               # پسورد فقط عددی، ۶ رقمی
rand1 = RandomPassword(length=12)         # پسورد شامل حروف+اعداد+سیمبل
rand2 = RandomPassword(length=10, numbers=False, symbols=False)  # فقط حروف

# تست خروجی‌ها
print("PIN Password:", pin.generate())
print("Random Password (default):", rand1.generate())
print("Random Password (letters only):", rand2.generate())
