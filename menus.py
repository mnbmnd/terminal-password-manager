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


def splash():
    print("Passman")
    overview()
    input("Press enter to continue to setup/login...")
    system.clear_screen()
    

def section(title: str):
    print("=" * 88)
    print(f"\n\033[1m[ {title} ]\033[0m")


def section_cutter():
    print("\n" + ("-" * 88))


def overview():
    section("Overview")
    print("\nWelcome to Passman 👋")
    print("└► A simple to use terminal-based password utility that securely "
          "manages your passwords\n")
    print("Features")
    print("- Secure password generation")
    print("- Accurate password entropy indicator")
    section_cutter()


def setup_menu():
    section("Setup")
    print("\nTo get started, set up your master password which you will use "
          "to login to Passman\n")
    
    masterCredentials = authentication.set_master_credentials()
    authentication.store_master_credentials(masterCredentials)
    
    section_cutter()
    input("Press enter to continue to login screen...")
    system.clear_screen()


def login_menu():
    section("Login") 

    loginPassword = getpass.getpass("\nPassword: ")
    success = authentication.authenticate(loginPassword)
    
    attemptsRemaining = 3
    while (not success) and (attemptsRemaining > 0):
        print("\nPassword incorrect")
        print(f"You have \033[1m{attemptsRemaining}\033[0m attempts remaning!\n")

        loginPassword = getpass.getpass("Password: ")
        success = authentication.authenticate(loginPassword)
        attemptsRemaining -= 1

    return success


def main_menu():
    section("Main Menu")

    print("\n1. Go to Passgen (Generator)")
    print("2. Go to Passcheck (Checker)")
    print("3. Quit\n")


    option = int(input("Ans: "))

    if option == 1:
        system.clear_screen()
        passgen_menu()
    elif option == 2:
        system.clear_screen()
        passcheck_menu()
    elif option == 3:
        system.clear_screen()
        print("Are you sure you would like to exit?")
        print("└► Enter 0 to go back to main menu")
        print("└► Enter 1 to confirm\n")
        confirmed = int(input("Ans: "))
        if confirmed:
            system.exit()
        else:
            system.clear_screen()
            main_menu()


def passgen_menu():
    section("Passgen")
    
    print("\nPassgen generates new passwords for you using secure randomness\n")
   
    print("1. Start Generator")
    print("2. Go back to main menu\n")
    
    passgenChoice = int(input("Ans: "))
    
    if passgenChoice == 1:
        section_cutter()
        print("Generator Started\n")
        # \033[1m\033[0m makes text bold
        print("What would you like to generate?\n")
        print(
            "1. A\033[1m Passphrase \033[0m– a sequence of randomly selected words"
        )
        print("└► Example:  \033[1mswell posing gruffly slander onto\033[0m")
        print("")
        print(
            "2. A\033[1m String \033[0m– a random string of letters, numbers, and symbols"
        )
        print("└► Example:  \033[1ma9Fq7XrL2mP8ZKcEi\033[0m\n")
        
        passwordType = int(input("Ans: "))
        generatedPassword = passgen.generatePassword(passwordType)
        
        print("Generated password:\033[1m", generatedPassword, "\033[0m")
        print("Entropy: {:.1f}".format(passcheck.get_entropy(generatedPassword)))
        print("Strength Level: ", passcheck.get_strength_level(generatedPassword), "\n")
        
        input("Press enter to go back to main menu...")
        
    system.clear_screen()
    main_menu()


def passcheck_menu():
    section("Passcheck")
    
    print("\nPasscheck evaluates how long it would take to crack your password in years\n")
    
    print("1. Start Checker")
    print("2. Go back to main menu\n")
    
    passcheckChoice = int(input("Ans: "))
    
    if passcheckChoice == 1:
        section_cutter()
        print("Checker Started\n")
        password = input("Enter your password: ")
        print("Entropy: {:.1f}".format(passcheck.get_entropy(password)))
        print("Strength Level: ", passcheck.get_strength_level(password), "\n")
        
        input("Press enter to go back to main menu...")
    system.clear_screen()
    main_menu()
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
