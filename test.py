from client.declarator import create_declaration, validate_declaration
from tools.funcs       import convert_to_dict
from client.repo       import initialize

create_declaration()
declaration = validate_declaration('Declaration')

initialize()