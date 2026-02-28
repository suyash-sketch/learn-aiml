# p = open(r'dictionary.py')

# print(p.read())

# file = open("superman.txt", 'w')

# file.write("hello i am suyash and i am writing inside this file ")
# file.close()

# file = open("superman.txt",'a')
# file.write("and now i am appending some content ")

#CRUD Operations
from pathlib import Path
import os
def read_file_and_folder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f'{i+1} : {item}')


def createfile():
    read_file_and_folder()
    try:
        name = input("please tell name of your file: ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("what you want to write: ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exists")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        read_file_and_folder()
        name = input("which file do you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully")
        else:
            print("File does not exists")
    except Exception as err:
        print(f"An error ocurred as {err}")

def updatefile():
    try:
        read_file_and_folder()
        name = input("which file do you want to access: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file")
            print("press 2 for overwriting the file")
            print("press 3 for appending content to the file")

            res = int(input("tell your response: "))
            if res == 1:
                name2 = input("tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to overwrite: ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append to the file: ")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error ocurred as {err}")

def deletefile():
    try:
        read_file_and_folder()
        name = input("which file do you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
        
            print("File removed successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error ocurred as {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("please tell your response: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()


