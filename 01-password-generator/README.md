# 01-password-generator
A Python CLI tool to generate secure passwords in three styles:
1. **PIN** → numeric only (like a bank PIN)  
2. **Random** → mix of letters, numbers, and symbols  
3. **Memorable** → word-based passwords that are easier to remember 
Built with object-oriented programming to practice class design in Python
Inspired by a sample project on GitHub. 

## Requirements
- Python 3.9+
- Dependencies listed in `requirements.txt`

## Installation
Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
### Requirements
- Python 3.10 or higher  
- Dependencies (install using pip):
```bash
  pip install -r requirements.txt
```
Download the NLTK words corpus:
```bash
python prepare_data.py
```
## Usage
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
**Options:**
- --words → number of words (default: 4)
- --separator → string to join words (default: "-")
- --no-capitalize → disables capitalization of words
## General help
You can always see all available commands and options with:
```bash
python main.py --help
```

## Project structure
```graphql
01-password-generator/
│
├── src/
│   ├── __init__.py        # package init
│   ├── generators.py      # password generator classes
│   └── main.py            # CLI entry point
│
├── prepare_data.py        # downloads NLTK words corpus
└── requirements.txt       # dependencies


```
## Notes
- Longer passwords are always more secure.

- The memorable mode can create long but still easy-to-remember passphrases.

- You can customize it by swapping in your own word list instead of NLTK.
## What I learned
Even though this project could have been written in a functional style, I chose to build it with object-oriented programming. this help me with:

- Practice designing classes for different use cases

- Build a foundation for experimenting with dashboards, which I explored in the next

It also gave me the background to experiment with dashboards — which I explored in my next project:
[02-streamlit-dashboard](https://github.com/Hna2005/from-zero/tree/main/02-streamlit-dashboard)