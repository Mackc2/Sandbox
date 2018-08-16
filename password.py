"""Jack Camp"""
MINIMUM_PASSWORD_LENGTH = 4
password = str(input("Please enter a password "))
password_length = len(password)
while password_length <= MINIMUM_PASSWORD_LENGTH:
    password = str(input("please enter a password "))
    password_length = len(password)
print("*"*password_length)
