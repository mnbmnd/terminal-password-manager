##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Manager                                                                                                    #
# File Name: authentication.py                                                                                                               #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import getpass
import encrypt
import system
import json
import getpass
import storage
from pathlib import Path


# Gets the user's inputted password
def get_user_password():
    userPassword = getpass.getpass("Enter your password to continue: ")
    
    return userPassword

# Sets the master password
def create_master_credentials():
    masterCredentials = set_master_credentials()
    
    return masterCredentials

# Stores the master's username, password salt, and password hash
def store_master_credentials(masterCredentials):
    storage.save_master_credentials(masterCredentials[0], masterCredentials[1], masterCredentials[2])

def has_master_credentials():
    try:
        masterCredentials = get_master_credentials()
        if 'hash' in masterCredentials and 'salt' in masterCredentials:
            return True
    except:
        return False
    
def authenticate(loginPassword):
    hashedLoginPass = hash_login_password(loginPassword)
    masterCredentials = get_master_credentials()
    if hashedLoginPass == masterCredentials['hash']:
        return True
    else:
        return False

def hash_login_password(loginPassword):
    masterCredentials = get_master_credentials()
    salt = bytes.fromhex(masterCredentials['salt']) # Convert the hex string back to bytes
    return encrypt.generate_hash(loginPassword, salt)


def get_master_credentials():
    master_file = Path.home() / ".password_manager/master.json"
    with open(master_file, "r") as f:
        return json.load(f)


def set_master_credentials():
    username = getpass.getuser()
    password = getpass.getpass(prompt="Enter a master password\n")
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
            print("Setup successfully completed!")
            matching = True
        else:
            print("Your passwords do not match!")
            attemptsRemaining -= 1
    
    if attemptsRemaining == 0:
        print()
        print("You are out of attempts")
        print()
        print("What would you like to do?")
    
    input("Press enter to continue to the main menu")
    system.clear_screen()
    
    salt = encrypt.generate_salt()
    passwordHash = encrypt.generate_hash(password, salt)
    
    return [username, salt.hex(), passwordHash] # Convert the salt from bytes to hex string

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #