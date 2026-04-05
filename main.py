
import streamlit as st
from frontend import run_frontend

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

def login():
    st.title("🔐 Login System")
    menu = ["Login", "Register", "Forgot Password"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if user in st.session_state.users and st.session_state.users[user] == pwd:
                st.session_state.logged_in = True
                st.success("Login Successful ✅")
                st.rerun()
            else:
                st.error("Invalid Credentials ❌")
        if st.button("Continue with Google"):
            st.session_state.logged_in = True
            st.success("Logged in with Google (Demo) ✅")
            st.rerun()

    elif choice == "Register":
        new_user = st.text_input("New Username")
        new_pwd = st.text_input("New Password", type="password")
        if st.button("Register"):
            st.session_state.users[new_user] = new_pwd
            st.success("Account Created 🎉")

    elif choice == "Forgot Password":
        user = st.text_input("Username")
        if st.button("Reset Password"):
            if user in st.session_state.users:
                new_pwd = st.text_input("Enter New Password", type="password")
                if st.button("Update"):
                    st.session_state.users[user] = new_pwd
                    st.success("Password Updated ✅")
            else:
                st.error("User not found ❌")

if not st.session_state.logged_in:
    login()
else:
    run_frontend()