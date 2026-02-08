##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Manager                                                                                                    #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator
from system import clear_screen
import getpass


def optionMenu():
    print("Choose an option to continue:")
    print("1. Generate a new password")
    print("2. Check password strength")
    print("3. Quit")
    option = int(input("Answer: "))
    clear_screen()
    if option == 1:
        passwordGeneratorMenu()
    elif option == 2:
        passwordCheckerMenu()


def getUserPassword():
    userPassword = getpass.getpass("Enter your password to continue: ")
    return userPassword


def passwordType():
    passwordType = int(input("Answer: "))
    print()
    return passwordType


def generateNewPassword(passwordType):
    generatedPassword = password_generator.generatePassword(passwordType)
    return generatedPassword


def displayPasswordStrength(generatedPassword=None):
    if generatedPassword is None:
        userPassword = getUserPassword()
        print("Entropy: {:.1f}".format(entropy.getEntropy(userPassword)))
        print(
            "Time to crack (in years): {:.1f}".format(
                entropy.getTimeToCrack(userPassword)
            )
        )
    else:
        print("Entropy: {:.1f}".format(entropy.getEntropy(generatedPassword)))
        print(
            "Time to crack (in years): {:.1f}".format(
                entropy.getTimeToCrack(generatedPassword)
            )
        )
    print()
    print("To find out more about entropy and time to crack, visit the link below:")
    print(
        "https://auth0.com/blog/defending-against-password-cracking-understanding-the-math/"
    )


def getGeneratedPassword(passwordType):
    generatedPassword = generateNewPassword(passwordType)
    return generatedPassword


def displayGeneratedPassword(passwordType):
    generatedPassword = getGeneratedPassword(passwordType)
    print("Your new password is: ", generatedPassword)
    displayPasswordStrength(generatedPassword)


def passwordCheckerMenu():
    print()
    print("=" * 18)
    print("Password Strength Checker")
    section("Description")
    print(
        "The Password Checker analyzes a password and estimates how secure \nit is against common attack methods."
    )
    print()
    print("It measures:")
    print(
        " 1. Password entropy – a way of quantifying how unpredictable a password \nis based on its length and the characters used."
    )
    print(
        " 2. Time to crack – an estimate of how long it would \ntake to brute-force the password assuming modern hardware and realistic attack speeds."
    )
    print()
    print(
        "Higher entropy generally means more possible combinations, which increases the \n"
        "time required to crack the password. The checker uses this \n"
        "information to give a practical sense of strength rather than \n"
        "a simple “weak/strong” label."
    )
    print()
    displayPasswordStrength()
    print()
    optionMenu()


def passwordGeneratorMenu():
    print("")
    print("=" * 18)
    print("Password Generator")
    section("Description")
    print(
        "The Password Generator creates new passwords for you using secure randomness."
    )
    print()
    print("You can choose between:")
    print(
        "1. Passphrase – a sequence of randomly selected words that balances security and memorability"
    )
    print("Example: swell posing gruffly slander onto")
    print()
    print(
        "2. Alphanumeric password – a fully random string of letters and numbers, with an optional \nsymbols setting for additional complexity."
    )
    print("Example: a9Fq7XrL2mP8ZKcE")
    print()
    displayGeneratedPassword(passwordType())
    print()
    optionMenu()


def section(title: str):
    print()
    print(f"[ {title} ]")


def splash():
    print()
    print(r"┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏┳┓┏━┓┏┓╻┏━┓┏━╸┏━╸┏━┓")
    print(r"┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┃┃┃┣━┫┃┗┫┣━┫┃╺┓┣╸ ┣┳┛")
    print(r"╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ╹ ╹╹ ╹╹ ╹╹ ╹┗━┛┗━╸╹┗╸")
    print()
    input("Press enter to continue...")
    clear_screen()


def mainMenu():
    section("Overview")
    print(
        "This project is a terminal-based password utility that helps\nyou both generate strong passwords and evaluate existing ones,\n"
        "it is designed to be simple to use, transparent in how it works,\nand focused on real-world security rather than gimmicks.\n"
    )
    print(
        "To get started, run the program in your terminal and\nchoose between generating a new password or checking the strength\n"
        "of an existing one. Each mode is interactive and guides\nyou through the available options."
    )
    print()
    optionMenu()


if __name__ == "__main__":
    splash()
    mainMenu()

# end main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
