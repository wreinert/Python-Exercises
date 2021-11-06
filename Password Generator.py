#Write a password generator in Python.
#Be creative with how you generate passwords -
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
#Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


#Generate a ten-character alphanumeric password with at least one lowercase character,
#at least one uppercase character, and at least three digits:
import random
import string
import secrets

def strongPsswd():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c in string.punctuation for c in password)
                and any(c.isupper() for c in password)
                and any(c.islower() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    print(password)

def averagePsswd():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        break
    print(password)

def weakPsswd():
    alphalower = string.ascii_lowercase
    alphaupper = string.ascii_uppercase
    numbers = string.digits
    options = [alphalower, alphaupper, numbers]
    alphabet = random.choice(options)
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        break
    print(password)

userchoice = input('Please pick a password strength (Weak, Average, Strong): ')

if userchoice.lower() == 'weak':
    weakPsswd()
elif userchoice.lower() == 'average':
    averagePsswd()
else:
    strongPsswd()
