import streamlit as st
from bank import Bank

st.set_page_config(page_title="🏦 Simple Bank", page_icon="💰", layout="centered")

st.title("🏦 Bank Management System")
menu = st.sidebar.radio(
    "Select an option",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
)

# --- CREATE ACCOUNT ---
if menu == "Create Account":
    st.header("📝 Create Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if not name or not email or not pin:
            st.error("Please fill all fields.")
        else:
            success, result = Bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success("Account created successfully!")
                st.json(result)
            else:
                st.error(result)

# --- DEPOSIT ---
if menu == "Deposit":
    st.header("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        success, msg = Bank.deposit(acc, int(pin), int(amount))
        st.success(msg) if success else st.error(msg)

# --- WITHDRAW ---
if menu == "Withdraw":
    st.header("🏧 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        success, msg = Bank.withdraw(acc, int(pin), int(amount))
        st.success(msg) if success else st.error(msg)

# --- SHOW DETAILS ---
if menu == "Show Details":
    st.header("📄 Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        success, result = Bank.get_details(acc, int(pin))
        if success:
            st.json(result)
        else:
            st.error(result)

# --- UPDATE DETAILS ---
if menu == "Update Details":
    st.header("✏️ Update Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New 4-digit PIN (optional)")

    if st.button("Update"):
        success, msg = Bank.update_details(
            acc,
            int(pin),
            new_name if new_name else None,
            new_email if new_email else None,
            int(new_pin) if new_pin else None
        )
        st.success(msg) if success else st.error(msg)

# --- DELETE ACCOUNT ---
if menu == "Delete Account":
    st.header("🗑️ Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = Bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
