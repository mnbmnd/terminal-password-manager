##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Manager                                                                                                    #
# File Name: authentication.py                                                                                                               #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import getpass
import system


def get_master_credentials():
    pass


def set_master_credentials():
    username = getpass.getuser()
    password = getpass.getpass(prompt="Enter a master password\n")

    masterCredentials = [username, password]
    matching = False
    attemptsRemaining = 3
    
    while (not matching) and (attemptsRemaining != 0):
        if attemptsRemaining == 1:
            print(f"You have {attemptsRemaining} attempt remaning!")
            print()
        else:
            print(f"You have {attemptsRemaining} attempts remaining")
            print()
        passwordConfirm = getpass.getpass(prompt="Confirm password\n")
        if password == passwordConfirm:
            print("Setup complete")
            matching = True
        else:
            print("Passwords do not match")
            # passwordConfirm = getpass.getpass(prompt="Try again!\n")
            attemptsRemaining -= 1

    if attemptsRemaining == 0:
        print("You are out of attempts")
        masterCredentials[1] = ""

    return masterCredentials
