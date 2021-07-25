import random

chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[]\;',./!@#$%^&*():"

while True:
    password_len = int(input("How long would you like your password to be?\n"))
    password_count = int(input("How many password would you like to have?\n"))
    for x in range(password_count):
        password = []
        for y in range(password_len):
            password.append(random.choice(chars))
        password = "".join(password)
        print("Here's your password(s):")
        print(password)
    answer = input("Do you want to continue?(q/else) ")
    if answer == "q":
        quit()
    
                    