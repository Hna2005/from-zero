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
