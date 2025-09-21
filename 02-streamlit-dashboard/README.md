# 02-streamlit-dashboard
A Python web app built with Streamlit to generate secure passwords in three styles:
- PIN → numeric only (like a bank PIN)
- Random → mix of letters, numbers, and symbols
- Memorable → word-based passwords that are easier to remember
This project is a continuation of [01-password-generator](https://github.com/Hna2005/from-zero/tree/main/01-password-generator)
It reuses the same password generator classes but provides an interactive dashboard instead of a CLI.

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

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
Download the NLTK words corpus:
```bash
python prepare_data.py
```
# Usage
```bash
streamlit run src/main.py
```
Then open the provided local URL in your browser (usually [`http://localhost:8501/`](http://localhost:8501/)).
You’ll see three password generator modes available in the sidebar:
### 1. Generate a PIN
Choose Pin Password and adjust the slider to set the length (default: `4`).
Example output: 493028
### 2. Generate a random password
Choose Random Password and select options:
- Length (slider)
- Include numbers (toggle)
- Include symbols (toggle)
Example output: `aB7#r!pLq9Zx`
### 3. Generate a memorable password
Choose Memorable Password and set:
- Number of words (slider)
- Separator string (text input, default: `-`)
- Capitalization (toggle)
Example output: `River-Dream-Light-Sound`

## Project structure
```graphql
02-streamlit-dashboard/
│
├── src/
│   ├── __init__.py        # package init
│   ├── generators.py      # password generator classes
│   └── main.py            # Streamlit dashboard entry point
│
├── prepare_data.py        # downloads NLTK words corpus
└── requirements.txt       # dependencies
```
## Notes
- PIN passwords are easy to type but less secure.  
- Random passwords are strongest if you include symbols.  
- Memorable passwords are long but easier to remember.  
