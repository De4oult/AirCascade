import shutil
import os

# Path validators

def path_must_not_exist(path: str) -> None: # If the folder exists, it will be removed
    if os.path.exists('%s' % path):
        shutil.rmtree('%s' % path)

def path_must_exist(path: str) -> None:      # If the folder doesn't exist, it will be created
    if not os.path.exists('%s' % path):
        os.mkdir('%s' % path)

def path_exist(path: str) -> bool:
    return os.path.exists('%s' % path)

# Hash validators

def hash_already_exist(hash: str, hashes: list[str]) -> bool: # Return True if hash in hashes list 
    if not hash in hashes: return True
    return False

# Declaration validators 

def declaration_contains(declaration: dict[str, any], parameter: str) -> bool: # Return True if Declaration has a parameter
    if declaration.get(parameter) and declaration.get(parameter) != []: return True
    return False

# Database 
def database_contains(database, key: str, value: str) -> bool:
    return database.contains(key, value) 