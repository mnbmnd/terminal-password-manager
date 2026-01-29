##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Generator                                                                                                  #
# File Name: password_generator.py                                                                                                           #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / 'words_alpha.txt'

def generatePassphrase(numWords):
    with open(file_path) as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(numWords))
    return password
    
def generateString(length):
    characters = string.ascii_letters + string.digits # + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(int(length)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def generatePassword(mode):
    print()
    if mode == 1:
        print("Choose the number of words for your passphrase (4-8 inclusive)")
        numWords = int(input("Answer: "))
        while (numWords < 4) | (numWords > 8):
            print("Enter a valid number!")
            print()
            numWords = int(input("Answer: "))
        passphrase = generatePassphrase(numWords) 
        return passphrase
    
    elif mode == 2:
        print("Choose the number of characters for your password (8-32 inclusive)") 
        length = int(input("Answer: "))
        while (length < 8) | (length > 32):
            print("Enter a valid number")
            print()
            length = int(input("Answer: "))
        stringPass = generateString(length)
        return stringPass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #