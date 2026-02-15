##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Manager                                                                                                    #
# File Name: storage.py                                                                                                                      #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import json
from pathlib import Path


def save_master_credentials(username, salt, passwordHash):
    password_dir = Path.home() / ".password_manager"
    password_dir.mkdir(exist_ok=True)

    data = {"username": username, "salt": salt, "hash": passwordHash}

    master_file = password_dir / "master.json"
    with open(master_file, "w") as f:
        json.dump(data, f)

    master_file.chmod(0o600)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #