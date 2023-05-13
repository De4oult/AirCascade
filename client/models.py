from datetime import datetime
from platform import node
from uuid     import uuid4

def repository(name: str, path: str) -> dict[str, any]:
    return {
        'name'   : name,
        'path'   : path,
        'author' : ''
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