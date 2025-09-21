import secrets
import string
from abc import ABC, abstractmethod
from typing import Optional, List

import nltk


class PasswordGenerator(ABC):
    """Base class for generate passwords."""
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate passwords.
        """
        pass


class PinPassword(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    def __init__(self, length: int = 8):
        self.length = length

    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return ''.join(secrets.choice(string.digits) for _ in range(self.length))
    

class RandomPassword(PasswordGenerator):
    """
    Class to generate a random password.
    """
    def __init__(self, length: int = 8, numbers: bool = True, symbols: bool = True):
        self.length = length
        self.characters: str = string.ascii_letters
        if numbers:
            self.characters += string.digits
        if symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """
        Generate a password from specified characters.
        """
        return ''.join(secrets.choice(self.characters) for _ in range(self.length))


class MemorablePassword(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
        self,
        word_count: int = 8,
        vocabulary: Optional[List[str]] = None,
        separator: str = '-',
        capitalization: bool = True
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()   # edit this to any vocabulary list you want
        
        self.word_count: int = word_count
        self.vocabulary: List[str] = [w for w in vocabulary if w.isalpha() and len(w) > 3]
        self.separator: str = separator
        self.capitalization: bool = capitalization
    
    def generate(self):
        """
        Generate a password from a list of vocabulary words.
        """
        if not self.vocabulary:
            raise ValueError("Vocabulary list is empty. Please provide a valid word list.")

        password_words = [secrets.choice(self.vocabulary) for _ in range(self.word_count)]
        if self.capitalization:
            password_words = [word.capitalize() for word in password_words]
        return self.separator.join(password_words)
