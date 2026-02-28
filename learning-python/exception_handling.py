# a = int(input("tell your number :-"))


# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an error as {err}")

# print("done")

age = int(input("tell your age"))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")
    

print("the club will start soon")
