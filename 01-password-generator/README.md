# Password Generator
This project is a starting point to improve my Python skills. It can generate stronger passwords with different options.
Inspired by a sample project on GitHub. It generates secure passwords in three different styles:  

1. **PIN** → numeric only (like a bank PIN)  
2. **Random** → mix of letters, numbers, and symbols  
3. **Memorable** → word-based passwords that are easier to remember  


## Installation
Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
## How to use
Go inside the `src/` folder and run the main script.

### 1. Generate a PIN
```bash
python main.py pin --length 6
```
Example output: `493028`

### 2. Generate a random password
```bash
python main.py random --length 12
```
Example output: `aB7#r!pLq9Zx`

Exclude numbers or symbols if you like:

```bash
python main.py random --length 12 --no-numbers
python main.py random --length 12 --no-symbols
```
### 3. Generate a memorable password
``` bash
python main.py memorable --words 4 --separator "-" --no-capitalize
```
Example output: `river-dream-light-sound`

## Project structure
```graphql
01-password-generator/
│
├── src/
│   ├── generators.py   # password generator classes
│   └── main.py         # CLI entry point
│
├── prepare_data.py     # downloads NLTK words corpus
└── requirements.txt    # dependencies
```
## Notes
Longer passwords are always more secure.

The memorable mode can create long but still easy-to-remember passphrases.

You can customize it by swapping in your own word list instead of NLTK.
## What I learned
Even though this project could have been written in a functional style, I chose to build it with object-oriented programming.
This helped me strengthen my OOP skills in Python and practice designing classes for different use cases.

It also gave me the background to experiment with dashboards — which I explored in my next project:
[02-streamlit-dashboard](https://github.com/Hna2005/from-zero/tree/main/02-streamlit-dashboard)