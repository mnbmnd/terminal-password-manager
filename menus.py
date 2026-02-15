import entropy
import system
import password_generator
import authentication

# Sections formatter
def section(title: str):
    print()
    print(f"[ {title} ]")
    
# Splash screen art (First screen that shows)
def splash():
    print()
    print("Password Manager")
    print()
    input("Press enter to continue...")
    system.clear_screen()

# The main menu, shows after splash screen
def overview():
    print("=" * 80)
    section("Overview")
    print(
        "This project is a terminal-based password utility that helps\nyou both generate strong passwords and evaluate existing ones,\n"
        "it is designed to be simple to use, transparent in how it works,\nand focused on real-world security rather than gimmicks.\n"
    )
    print()

# # Confirmation prompt to quit
# def quit_confirm(state):
#     print()
#     option = int(input("Enter 1 to confirm or 2 to go back: "))
#     if option == 1:
#         system.exit_program()
#         print("Thank you for using passman 👋")
#         exit(0) # Exit with success
#     elif option == 2:
#         if state == 1:
#             system.clear_screen()
#             overview()
#             credentials_menu()
#         elif state == 2:
#             system.clear_screen()
#             main_menu()

def setup_menu():
    print("=" * 80)
    section("Setup")
    print("To get started, set up your master password")
    masterCredentials = authentication.create_master_credentials()
    authentication.store_master_credentials(masterCredentials)

# The login menu
def login_menu():
    print("=" * 80)
    section("Login Menu")
    loginPassword = authentication.get_user_password()
    success = authentication.authenticate(loginPassword)
    if success:
        print("Login Successful")
        return True
    return False

# The second option menu presented
def main_menu():
    print("=" * 80)
    section("Main Menu")
    print()
    print("Choose an option below to continue:")
    print("1. Generate a new password")
    print("2. Check password strength")
    print("3. Quit")
    
    option = int(input("Answer: "))
    
    if option == 1:
        pass_generator_menu()
    elif option == 2:
        pass_checker_menu()
    # elif option == 3:
    #     quit_confirm(2)

# Gets user's option to generate either a passphrase or alphanumeric password
def password_type():
    passwordType = int(input("Answer: "))
    print()
    
    return passwordType

# Displays the password generator menu
def pass_generator_menu():
    print("")
    print("=" * 80)
    print("Password Generator")
    section("Description")
    print(
        "The Password Generator creates new passwords for you using secure randomness."
    )
    print()
    print("You can choose between:")
    # \033[1m\033[0m makes text bold
    print(
        "1.\033[1m Passphrase \033[0m– a sequence of randomly selected words that balances security and memorability"
    )
    print()
    print("Example:")
    print("\033[1mswell posing gruffly slander onto\033[0m")
    print()
    print()
    print(
        "2.\033[1m Alphanumeric password \033[0m– a fully random string of letters and numbers, with an optional \nsymbols setting for additional complexity."
    )
    print()
    print("Example:")
    print("\033[1ma9Fq7XrL2mP8ZKcE\033[0mi")
    print()
    display_generated_pass(password_type())
    print()

# Displays the password checker menu
def pass_checker_menu():
    print()
    print("=" * 80)
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
    display_pass_strength()
    print()
    main_menu()
    
# displays the password strength of an inputted password
def display_pass_strength(generatedPassword=None):
    if generatedPassword is None:
        userPassword = authentication.get_user_password()
        
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

# Gets the newly generated password
def get_generated_pass(passwordType):
    generatedPassword = password_generator.generatePassword(passwordType)
    
    return generatedPassword

# Displays the generated password back to the user
def display_generated_pass(passwordType):
    generatedPassword = get_generated_pass(passwordType)
    
    print("Your new password is: ", generatedPassword)
    display_pass_strength(generatedPassword)