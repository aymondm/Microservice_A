import string
import secrets

def create_password(length=18, numbers=1, special=1):
    password = ''
    all_chars = string.ascii_letters

    if numbers == 1:
        all_chars += string.digits
    if special == 1:
        all_chars += string.punctuation

    for i in range(length):
        password += secrets.choice(all_chars)
    return password
