#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: passcheck.py                                                          #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import math

LOWERCASE = 26
UPPERCASE = 26
NUMERICAL = 10
SYMBOLS = 32
SPACE = 1

BCRYPT_COST = 12
GUESSES_PER_SEC = 1e5
SECONDS_PER_YEAR = 6.308 * (10**7)


def get_uppercase_count(password):
    upperCount = 0
    for i in password:
        if i.isupper():
            upperCount += 1
            
    return upperCount


def get_lowercase_count(password):
    lowerCount = 0
    for i in password:
        if i.islower():
            lowerCount += 1
            
    return lowerCount


def get_numeric_count(password):
    numericCount = 0
    for i in password:
        if i.isnumeric():
            numericCount += 1
            
    return numericCount


def get_symbols_count(password):
    symbols = list(string.punctuation)
    symbolsCount = 0
    for i in password:
        if i in symbols:
            symbolsCount += 1
            
    return symbolsCount


def get_space_count(password):
    spaceCount = 0
    for i in password:
        if i == " ":
            spaceCount += 1
            
    return spaceCount


def get_character_count(password):
    characters = 0
    if get_lowercase_count(password):
        characters += LOWERCASE

    if get_uppercase_count(password):
        characters += UPPERCASE

    if get_numeric_count(password):
        characters += NUMERICAL

    if get_symbols_count(password):
        characters += SYMBOLS

    if get_space_count(password):
        characters += SPACE

    return characters


def get_entropy(password):
    passwordLength = len(password)
    r = get_character_count(password)
    entropy = math.log2(r**passwordLength)

    return entropy


def sample_space_size(password):
    charactersAvailable = get_character_count(password)
    n = len(password)
    sampleSpaceSize = charactersAvailable**n
    
    return sampleSpaceSize


def get_strength_level(password):
    entropy = get_entropy(password)
    
    strengthLevels = [
        (28, "Very Weak 🟥"),
        (36, "Weak 🟧"),
        (60, "Medium 🟨"),
        (128, "Strong 🟩"),
        (float('inf'), "Very Strong 🟦")
    ]
    
    for threshold, label in strengthLevels:
        if entropy < threshold:
            return label


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
