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

def path_file_format(path: str) -> str:
    if     os.path.isdir('%s' % path) and path[-1] != '/': return '%s/' % path
    if not os.path.isdir('%s' % path) and path[-1] == '/': return '%s'  % path[:-1]
    return path 

# Hash validators

def hash_already_exist(hash: str, hashes: list[str]) -> bool: # Return True if hash in hashes list 
    return True if not hash in hashes else False


# Declaration validators 

def declaration_contains(declaration: dict[str, any], field: str) -> bool: # Return True if Declaration has a parameter
    return True if (
        (declaration.get(field)) and 
        (declaration.get(field) != [])
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

def repository_already_initialized(database, path: str) -> bool:
    return database.contains('path', path)

# Server

def server_config(config: dict[str, any]) -> None:
    return True if (
        (config.get('server_address') != '') and
        (config.get('server_port')    != '') and
        (config.get('username')       != '') and
        (config.get('password')       != '') 
    ) else False