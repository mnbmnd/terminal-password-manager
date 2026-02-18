#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: authentication.py                                                     #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import getpass
import json
from pathlib import Path

import encrypt
import storage


# If the user does not have master credentials they will be taken to the setup screen
def has_master_credentials():
    try:
        masterCredentials = get_master_credentials()
        if "hash" in masterCredentials and "salt" in masterCredentials:
            return True
    except:
        return False


# Stores the master's username, password salt, and password hash
def store_master_credentials(masterCredentials):
    storage.save_master_credentials(
        masterCredentials[0], masterCredentials[1], masterCredentials[2]
    )


# Password matching at the login
def authenticate(loginPassword):
    hashedLoginPass = hash_login_password(loginPassword)  # Hashes inputted pass
    masterCredentials = get_master_credentials()
    if hashedLoginPass == masterCredentials["hash"]:
        return True
    else:
        return False


def hash_login_password(loginPassword):
    masterCredentials = get_master_credentials()
    salt = bytes.fromhex(
        masterCredentials["salt"]
    )  # Convert the hex string back to bytes
    return encrypt.generate_hash(loginPassword, salt)


# Retrieves master credentials from the saved json file
def get_master_credentials():
    master_file = Path.home() / ".passman/master.json"
    with open(master_file, "r") as f:
        return json.load(f)


# Creates the master credentials via the setup screen, and saves them to json
def set_master_credentials():
    username = getpass.getuser()
    password = getpass.getpass(prompt="\nEnter a master password")
    matching = False

    while not matching:
        passwordConfirm = getpass.getpass(prompt="\nConfirm password")

        if password == passwordConfirm:
            print("\033[1mSetup complete\033[0m")
            matching = True
        else:
            print("\nYour passwords do not match, try again!")

    salt = encrypt.generate_salt()
    passwordHash = encrypt.generate_hash(password, salt)

    return [
        username,
        salt.hex(),
        passwordHash,
    ]  # Convert the salt from bytes to hex string for reading


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
