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
    return True if not hash in hashes else False


# Declaration validators 

def declaration_contains(declaration: dict[str, any], parameter: str) -> bool: # Return True if Declaration has a parameter
    return True if (
        (declaration.get(parameter)) and 
        (declaration.get(parameter) != [])
    ) else False

def declaration_filled(declaration: dict[str, any]) -> bool:
    return True if (
        (declaration.get('name')       != '') and 
        (declaration.get('author')     != '') and
        (declaration.get('files')      != []) and
        (declaration.get('language')   != '') and
        (declaration.get('identifier') != '')
    ) else False

def server_filled(declaration: dict[str, any]) -> bool:
    server = declaration.get('server')
    return True if (
        (server.get('address')  != '') and
        (server.get('port')     != '') and
        (server.get('username') != '') and
        (server.get('password') != '')
    ) else False


# Database 

def database_contains(database, key: str, value: str) -> bool:
    return database.contains(key, value) 