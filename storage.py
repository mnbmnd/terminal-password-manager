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
