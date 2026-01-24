import math
import string
import entropy
import password_generator

if __name__ == "__main__":
    print("PASSWORD STRENGTH CHECKER")
    userPassword = input("Please enter your password: ")
    print("Password length: " + str(entropy.getSize(userPassword)))
    print("Upper count: " + str(entropy.getUppercaseCount(userPassword)))
    print("Lower count: " + str(entropy.getLowercaseCount(userPassword)))
    print("Numeric count: " + str(entropy.getNumericCount(userPassword)))
    print("Symbols count: " + str(entropy.getSymbolsCount(userPassword)))
    print("Space count: " + str(entropy.getSpaceCount(userPassword)))
# end main