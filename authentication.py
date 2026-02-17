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


def authenticate(loginPassword):
    hashedLoginPass = hash_login_password(loginPassword)
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


def get_master_credentials():
    master_file = Path.home() / ".password_manager/master.json"
    with open(master_file, "r") as f:
        return json.load(f)


def set_master_credentials():
    username = getpass.getuser()
    password = getpass.getpass(prompt="Enter a master password\n")
    matching = False

    while not matching:
        passwordConfirm = getpass.getpass(prompt="Confirm password\n")

        if password == passwordConfirm:
            print("\033[1mSetup complete\033[0m")
            matching = True
        else:
            print("Your passwords do not match, try again!\n")

    salt = encrypt.generate_salt()
    passwordHash = encrypt.generate_hash(password, salt)

    return [
        username,
        salt.hex(),
        passwordHash,
    ]  # Convert the salt from bytes to hex string


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
