##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Generator                                                                                                  #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def optionMenu():
    print("Choose an option to continue:")
    print("1. Generate a new password")
    print("2. Check password strength")
    print("3. Quit")
    option = int(input("Answer: "))
    clear()
    if option == 1:
        passwordGeneratorMenu()
    elif option == 2:
        passwordCheckerMenu()

def getUserPassword():
    userPassword = input("Please enter your password: ")
    return userPassword

def passwordType():
    passwordType = int(input("Answer: "))
    return passwordType

def generateNewPassword(passwordType):
    generatedPassword = password_generator.generatePassword(passwordType)
    return generatedPassword

def displayPasswordEntropy(generatedPassword = None):
    if generatedPassword == None:
        print("Entropy: {:.1f}".format(entropy.getEntropy(getUserPassword())))
    else:
        print("Entropy: {:.1f}".format(entropy.getEntropy(generatedPassword)))
    
def displayTimeToCrack(generatedPassword = None):
    if generatedPassword == None:
        print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(getUserPassword())))
    else:
        print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(generatedPassword)))

def getGeneratedPassword(passwordType):
    generatedPassword = generateNewPassword(passwordType)
    return generatedPassword
    
def displayGeneratedPassword(passwordType):
    generatedPassword = getGeneratedPassword(passwordType)
    print("Your new password is: " + generatedPassword)
    displayTimeToCrack(generatedPassword)
    displayPasswordEntropy(generatedPassword)
    
def passwordCheckerMenu():
    print()
    print("=" * 18)
    print("Password Strength Checker")
    print("Details...")
    print()
    print()
    displayTimeToCrack()
    displayPasswordEntropy()

def passwordGeneratorMenu():
    print("")
    print("=" * 18)
    print("Password Generator")
    section("Overview")
    print()
    print("Choose your password type")
    print()
    print("1. Passphrase (Easier to remember)")
    print("Example: swell posing gruffly slander onto")
    print()
    print("2. Random String (Alphanumeric)")
    print("Example: a9Fq7XrL2mP8ZKcE")
    print()
    # TODO: Add a 3rd option as 3. Random String (Alphanumeric + Symbols)
    displayGeneratedPassword(passwordType())
    print()
    optionMenu()

def section(title: str):
    print()
    print(f"[ {title} ]")

def splash():
    print()
    print(r"┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏━╸┏━╸┏┓╻┏━╸┏━┓┏━┓╺┳╸┏━┓┏━┓")
    print(r"┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┃╺┓┣╸ ┃┗┫┣╸ ┣┳┛┣━┫ ┃ ┃ ┃┣┳┛")
    print(r"╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ┗━┛┗━╸╹ ╹┗━╸╹┗╸╹ ╹ ╹ ┗━┛╹┗╸")
    print()
    input("Press enter to continue...")
    clear()
    
def mainMenu():
    section("Overview")
    print(
        "This project is a terminal-based password utility that helps \n"
    "you both generate strong passwords and evaluate existing ones, \n"
    "it is designed to be simple to use, transparent in how it works, \n"
    "and focused on real-world security rather than gimmicks. \n"
        )
    print("To get started, run the program in your terminal and \n"
          "choose between generating a new password or checking the strength \n"
          "of an existing one. Each mode is interactive and guides \n"
          "you through the available options."
          )
    print()
    optionMenu()

if __name__ == "__main__":
    splash()
    mainMenu()
        
# end main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #