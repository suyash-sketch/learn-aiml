import json
import random
import string

from pathlib import Path
class Bank:
    database = 'bank management/data.json'
    data = []

    try:
        if Path(database).exists():

            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")

    except Exception as err:
        print(f"an exception occurred as {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generateaccountno(cls):
        alpha = random.choices(string.ascii_letters, k = 4)
        num = random.choices(string.digits,k = 4)

        id = alpha + num
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "name" : input("tell your name : "),
            "age" : int(input("tell your age : ")),
            "email": input("tell your email address : "),
            "pin" : int(input("create a 4 digit pin number : ")),
            "accountNo" : Bank.__generateaccountno(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositMoney(self):
        accNumber = input("please tell your account no : ")
        pin = int(input("enter your Pin number : "))

        userData = [i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]

        if userData == False:
            print("sorry no data found")
        else:
            amount = int(input("how do you want to deposit : "))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much, please deposit below 10,000")
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")

    def withdrawMoney(self):
        accNumber = input("please tell your account no : ")
        pin = int(input("enter your Pin number : "))

        userData = [i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]

        if userData == False:
            print("sorry no data found")
        else:
            amount = int(input("how do you want to withdraw : "))
            if userData[0]['balance'] < amount:
                print("sorry you do not have sufficient balance")

            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully")


    def showDetails(self):
        accNumber = input("please tell your account no : ")
        pin = int(input("enter your Pin number : "))

        userData = [i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]
        print("your details are:\n")
        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")


    def updateDetails(self):
        accNumber = input("please tell your account no : ")
        pin = int(input("enter your Pin number : "))

        userData = [i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin ]

        if userData == False:
            print("no such user found ")

        else:
            print("you cannot change age, account number and balance ")
            print("fill the details for change or leave it empty if no change: ")

            newData = {
                "name" : input("tell your name or press enter to skip : "),
                "email" : input("tell you email address or press enter to skip : "),
                "pin" : int(input("update your pin number"))
            }

            if newData['name'] == "":
                newData['name'] = userData[0]['name']

            if newData['email'] == "":
                newData['email'] = userData[0]['email']

            if newData['pin'] == "":
                newData['pin'] = userData[0]['pin']

            newData['age'] = userData[0]['age']

            newData['accountNo'] = userData[0]['accountNo']

            newData['balance'] = userData[0]['balance']

            if type(newData["pin"]) == str:
                newData["pin"] = int(newData["pin"])

            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]

            Bank.__update()
            print("Details updated successfully")


    def deleteDetails(self):
        accNumber = input("please tell your account no : ")
        pin = int(input("enter your Pin number : "))

        userData = [i for i in Bank.data if i['accountNo'] == accNumber and i['pin'] == pin]

        if userData == False:
            print("No such user exists")
        else:
            check = input("press y if you actually want to delete your account or press n")

            if check == "n" or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userData[0])

                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()


user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating details")
print("press 6 for deleting the account")

check = int(input("tell your response :- "))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.deleteDetails()
