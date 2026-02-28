import json
import random
import string
from pathlib import Path

class Bank:
    database = Path("data.json")
    data = []

    # Load existing data
    if database.exists():
        try:
            with open(database, "r") as fs:
                data = json.load(fs)
        except json.JSONDecodeError:
            data = []
    else:
        database.touch()
        data = []

    @staticmethod
    def __update():
        with open(Bank.database, "w") as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __generateAccountNo(cls):
        alpha = random.choices(string.ascii_uppercase, k=4)
        num = random.choices(string.digits, k=4)
        acc = alpha + num
        random.shuffle(acc)
        return "".join(acc)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "You must be at least 18 and pin must be 4 digits."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": cls.__generateAccountNo(),
            "balance": 0
        }

        cls.data.append(account)
        cls.__update()
        return True, account

    @classmethod
    def authenticate(cls, accountNo, pin):
        return next((user for user in cls.data if user["accountNo"] == accountNo and user["pin"] == pin), None)

    @classmethod
    def deposit(cls, accountNo, pin, amount):
        user = cls.authenticate(accountNo, pin)
        if not user:
            return False, "Invalid account number or pin."
        if amount <= 0 or amount > 10000:
            return False, "Deposit must be between 1 and 10,000."

        user["balance"] += amount
        cls.__update()
        return True, f"Successfully deposited ₹{amount}"

    @classmethod
    def withdraw(cls, accountNo, pin, amount):
        user = cls.authenticate(accountNo, pin)
        if not user:
            return False, "Invalid account number or pin."
        if amount <= 0:
            return False, "Amount must be positive."
        if user["balance"] < amount:
            return False, "Insufficient balance."

        user["balance"] -= amount
        cls.__update()
        return True, f"Successfully withdrew ₹{amount}"

    @classmethod
    def get_details(cls, accountNo, pin):
        user = cls.authenticate(accountNo, pin)
        if not user:
            return False, "Invalid credentials."
        return True, user

    @classmethod
    def update_details(cls, accountNo, pin, new_name=None, new_email=None, new_pin=None):
        user = cls.authenticate(accountNo, pin)
        if not user:
            return False, "Invalid credentials."

        if new_name:
            user["name"] = new_name
        if new_email:
            user["email"] = new_email
        if new_pin and len(str(new_pin)) == 4:
            user["pin"] = new_pin

        cls.__update()
        return True, "Details updated successfully."

    @classmethod
    def delete_account(cls, accountNo, pin):
        user = cls.authenticate(accountNo, pin)
        if not user:
            return False, "Invalid credentials."
        cls.data.remove(user)
        cls.__update()
        return True, "Account deleted successfully."

