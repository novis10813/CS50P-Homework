from curses.ascii import isupper



words = input("Please enter something: \n")

for i in words:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")