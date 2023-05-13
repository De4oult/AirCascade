from tools.funcs import get_from_declaration

from datetime import datetime
from platform import node
from uuid     import uuid4

def repository(declaration: dict[str, any], path: str) -> dict[str, any]:
    return {
        'name'       : get_from_declaration(declaration, 'name'),
        'author'     : get_from_declaration(declaration, 'author'),
        'language'   : get_from_declaration(declaration, 'language'),
        'identifier' : get_from_declaration(declaration, 'identifier'),
        'commits'    : [],
        'path'       : path
    }

def commit(label: str, hash: str) -> dict[str, any]:
    return {
        'label'  : label,
        'hash'   : hash,
        'author' : node(),
    }

def declaration() -> dict[str, any]:
    return {
        'name'    : '',
        'version' : 'v1.0',
        'main'    : '',
        'execute' : False,

        'author'  : node(),
        'email'   : '',


        'files'   : [
            'Declaration'
        ],
        'libs'    : [],
        'cmds'     : [
            'echo \'Successfully delivered!\''
        ],
        'notes'   : [
            'Succesfully delivered!'
        ],

        'server'  : {
            'address'  : '',
            'port'     : '',
            'username' : '',
            'password' : ''
        },
        
        'language'   : '',
        'identifier' : str(uuid4().int)[:18]
    }