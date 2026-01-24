import string
import math

"""
This file checks the strengths of a user's password.
Conditions are set against the time it takes for a hacker to brute force your password
"""

def getSize(userPassword):
    return len(userPassword)

def getUppercaseCount(userPassword):
    upperCount = 0
    for i in userPassword:
        if (i.isupper()):
            upperCount += 1
    return upperCount
            
def getLowercaseCount(userPassword):
    lowerCount = 0
    for i in userPassword:
        if (i.islower()):
            lowerCount += 1
    return lowerCount
    
def getNumericCount(userPassword):
    numericCount = 0
    for i in userPassword:
        if (i.isnumeric()):
            numericCount += 1
    return numericCount

def getSymbolsCount(userPassword):
    symbols = list(string.punctuation)
    symbolsCount = 0
    for i in userPassword:
        if i in symbols:
            symbolsCount += 1
    return symbolsCount

def getSpaceCount(userPassword):
    spaceCount = 0
    for i in userPassword:
        if i == " ":
            spaceCount += 1
    return spaceCount

#TODO: create a function that evaluates if it matches a name, character, product, or organization.