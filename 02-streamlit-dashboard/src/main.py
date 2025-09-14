import streamlit as st
from generators import PinPassword, RandomPassword, MemorablePassword

st.title("Password Generator")

password_type = st.selectbox(
    "Select the type of password you want to generate:",
    ["Pin Password", "Random Password", "Memorable Password"]
)

if password_type == "Pin Password":
    length = st.slider("Length of password:", 4, 50)
    password_generator = PinPassword(length)

elif password_type == "Random Password":
    length = st.slider("Length of password:", 4, 50)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")
    password_generator = RandomPassword(length, include_numbers, include_symbols)

else:  # Memorable Password
    num_words = st.slider("Number of words:", 2, 10)
    separation = st.text_input("Enter your separator:", "-") or "-"
    capitalization = st.toggle("Capitalize words")
    password_generator = MemorablePassword(num_words, None, separation, capitalization)

st.write(password_generator.generate())
