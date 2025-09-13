# Password Generator
This project is a starting point to improve my Python skills. It can generate stronger passwords with different options.
Inspired by a sample project on GitHub
## Installation
Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
## Usage:
Run the script:
```bash
python main.py
```
Or use the classes in your own project:
```python
from password_generator import PinPassword, RandomPassword

pin = PinPassword(length=12)
print("PIN:", pin.generate())

rand = RandomPassword(length=12, numbers=True, symbols=True)
print("Random password:", rand.generate())
```
