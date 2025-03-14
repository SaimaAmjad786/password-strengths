
import re
import random
import string
import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="🔐 Password Strength & Generator", 
                   page_icon="🔑", layout="wide")

# Custom CSS for Hover Effects & Styling
st.markdown("""
    <style>
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        
        .animated-text {
            animation: fadeIn 1.5s ease-in-out;
        }

        .hover-effect:hover {
            color: blue !important;
            font-weight: bold !important;
            background-color: white !important;
            transition: 0.3s ease-in-out;
            border-radius: 5px;
            padding: 5px;
        }
        
        .password-box {
            background: #f8f9fa;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            color: #155724;
            animation: fadeIn 1s;
        }
        
        .stButton button {
            width: 100%;
            background: linear-gradient(to right, #007BFF, #00C9FF);
            color: white;
            font-size: 18px;
            border-radius: 8px;
            transition: 0.3s;
        }

        .stButton button:hover {
            background: linear-gradient(to right, white, white);
            transform: scale(1.05);
        }

        .success-alert {
            color: white;
            background: #28a745;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }

        .warning-alert {
            color: white;
            background: #ffc107;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }

        .error-alert {
            color: white;
            background: #dc3545;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title & Description
st.title("🔐 Password Strength Checker & Generator")
st.write("Ensure your passwords are **secure** using this tool! Generate strong passwords & check security levels in real-time. 🚀")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('<span class="hover-effect">❌ Password should be **at least 8 characters long**.</span>')

    # Check uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append('<span class="hover-effect">❌ Include **both uppercase (A-Z) and lowercase (a-z) letters**.</span>')

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append('<span class="hover-effect">❌ Add **at least one number (0-9)**.</span>')

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append('<span class="hover-effect">❌ Use **at least one special character (!@#$%^&*)**.</span>')

    # Animated password strength display
    time.sleep(0.5)  # Simulate loading animation
    if score == 4:
        st.markdown('<div class="success-alert">✔️ **Strong Password** - Your password is secure! 🔒</div>', unsafe_allow_html=True)
    elif score == 3:
        st.markdown('<div class="warning-alert">⚠️ **Moderate Password** - Improve security by adding complexity.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="error-alert">❌ **Weak Password** - Follow the suggestions below to strengthen it.</div>', unsafe_allow_html=True)

    # Display feedback with hover effect
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.markdown(item, unsafe_allow_html=True)

# Function to generate a strong password
def generate_password(length):
    if length < 8:
        return "❌ Password length should be at least 8 characters."
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Sidebar with options
st.sidebar.header("🔧 Options")
password_length = st.sidebar.slider("Select password length:", min_value=8, max_value=32, value=12)

if st.sidebar.button("🔄 Generate Strong Password"):
    strong_password = generate_password(password_length)
    st.sidebar.markdown(f'<div class="password-box">{strong_password}</div>', unsafe_allow_html=True)

# User input for password checking
st.subheader("🔍 Check Your Password Strength")
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

# Button to check password strength with animation
if st.button("🚀 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
