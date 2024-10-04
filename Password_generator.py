# The import streamlit as st statement brings in the Streamlit library for building web applications, using st as a convenient alias.The random module is imported to generate random numbers and selections,while the string module provides predefined character sets like letters, digits, and punctuation for easy access.

import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars, use_uppercase):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    
    if score == 4:
        return 'Strong'
    elif score == 3:
        return 'Medium'
    else:
        return 'Weak'

# Only one header
st.title('Secure Password Generator')
st.sidebar.header('Password Options')

# Sidebar input options

length = st.sidebar.slider('Password Length', min_value=6, max_value=20, value=12, step=1)
use_digits = st.sidebar.checkbox('Include Digits', value=True)
use_special_chars = st.sidebar.checkbox('Include Special Characters', value=True)
use_uppercase = st.sidebar.checkbox('Include Uppercase Letters', value=True)

if st.button('Generate Password'):
    if length < 6:
        st.error('Password length should be at least 6 characters.')
    else:
        generated_password = generate_password(length, use_digits, use_special_chars, use_uppercase)
        st.success('Generated Password:')
        st.code(generated_password)
        
        # Calculate and show password strength

        strength = password_strength(generated_password)
        st.write(f'Password Strength: {strength}')
