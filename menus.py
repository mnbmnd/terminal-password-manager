#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: menus.py                                                              #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import getpass

import passcheck
import passgen
import system
import authentication


ATTEMPTS = 3

# Ascii art to welcome
def splash():
    print("Passman")
    overview()
    input("Press enter to continue to setup/login...")
    system.clear_screen()
    
# Adds titles to sections
def section(title: str):
    print("=" * 88)
    print(f"\n\033[1m[ {title} ]\033[0m")


def section_cutter():
    print("\n" + ("-" * 88))
    

def get_user_choice():
    userOption = int(input("\nAnswer: "))
    
    return userOption


def show_goodbye():
    print("Thank you for using Passman 👋")


# The overview section
def overview():
    section("Overview")
    print("\nWelcome to Passman 👋")
    print("└► A simple to use terminal-based password utility that securely "
          "manages your passwords")
    print("\nFeatures")
    print("- Secure password generation")
    print("- Accurate password strength check")
    section_cutter()


def show_setup_menu():
    section("Setup")
    print("\nTo get started, set up your master password which you will use "
          "to login to Passman\n")
    
    masterCredentials = authentication.set_master_credentials()
    authentication.store_master_credentials(masterCredentials)
    
    section_cutter()
    input("Press enter to continue to login screen...")
    system.clear_screen()


def show_login_menu():
    section("Login") 

    loginPassword = getpass.getpass("\nPassword: ")
    success = authentication.authenticate(loginPassword)
    
    attemptsRemaining = ATTEMPTS
    while (not success) and (attemptsRemaining > 0):
        print("\nPassword incorrect")
        print(f"You have \033[1m{attemptsRemaining}\033[0m attempts remaning!")

        loginPassword = getpass.getpass("\nPassword: ")
        success = authentication.authenticate(loginPassword)
        attemptsRemaining -= 1

    return success


def show_main_menu():
    section("Main Menu")

    print("\n1. Go to Passgen (Generator)")
    print("2. Go to Passcheck (Checker)")
    print("3. Quit")
    
    return get_user_choice()



def show_passgen_menu():
    section("Passgen")
    
    print("\nPassgen generates new passwords for you using secure randomness")
    print("\n1. Start Generator")
    print("2. Go back to main menu")
    
    passgenChoice = get_user_choice()
    
    if passgenChoice == 1:
        section_cutter()
        print("Generator Started")
        # \033[1m\033[0m makes text bold
        print("\nWhat would you like to generate?")
        print(
            "\n1. A\033[1m Passphrase \033[0m– a sequence of randomly selected words"
        )
        print("└► Example:  \033[1mswell posing gruffly slander onto\033[0m")

        print(
            "\n2. A\033[1m String \033[0m– a random string of letters, numbers, and symbols"
        )
        print("└► Example:  \033[1ma9Fq7XrL2mP8ZKcEi\033[0m")
        
        passwordType = get_user_choice()
        generatedPassword = passgen.password_generator(passwordType)
        
        print("Generated password:\033[1m", generatedPassword, "\033[0m")
        print("Entropy: {:.1f}".format(passcheck.get_entropy(generatedPassword)))
        print("Strength Level: ", passcheck.get_strength_level(generatedPassword))
        
        input("\nPress enter to go back to main menu...")
        
    system.clear_screen()


def show_passcheck_menu():
    section("Passcheck")
    
    print("\nPasscheck evaluates how long it would take to crack your password in years")
    print("\n1. Start Checker")
    print("2. Go back to main menu")
    
    passcheckChoice = get_user_choice()
    
    if passcheckChoice == 1:
        section_cutter()
        print("Checker Started\n")
        password = input("Enter your password: ")
        print("Entropy: {:.1f}".format(passcheck.get_entropy(password)))
        print("Strength Level: ", passcheck.get_strength_level(password))
        
        input("\nPress enter to go back to main menu...")
        
    system.clear_screen()
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
