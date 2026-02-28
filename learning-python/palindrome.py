def palindrome(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]

    if rev == st:
        print(f"{st} is palindrome")
    else:
        print(f"{st} is not a palindrome")


palindrome("madam")