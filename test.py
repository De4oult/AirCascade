from client.declarator import create_declaration, read_declaration, validate_declaration
from tools.funcs       import convert_to_dict

create_declaration()

declaration = read_declaration('Declaration')

validate_declaration(declaration)