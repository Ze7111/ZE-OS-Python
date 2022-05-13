from fileinput import close
from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("keys\\accountsdb.key", "wb") as key_file:
        key_file.write(key)
    close