#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: passgen.py                                                            #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import secrets
from pathlib import Path

import menus

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "words_alpha.txt"  # Dictionary to take words from


def generate_passphrase(numWords):
    with open(file_path) as f:
        words = [word.strip() for word in f]
        password = " ".join(secrets.choice(words) for i in range(numWords))
        
    return password


def generate_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = "".join(secrets.choice(characters) for i in range(int(length)))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            break
        
    return password


def password_generator(mode):
    if mode == 1:        
        print("\nChoose the number of words for your passphrase (4-8 inclusive)")
        
        numWords = menus.get_user_choice()            
        passphrase = generate_passphrase(numWords)  # Passphrase generator
        
        return passphrase
    elif mode == 2:
        print("\nChoose the number of characters for your password (8-32 inclusive)")
        
        length = menus.get_user_choice()            
        stringPass = generate_string(length)  # String generator
        
        return stringPass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
