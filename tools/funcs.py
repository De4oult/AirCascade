from tools.validators  import declaration_contains
from tools.pathes import exec_dir
import json
import os

def get_from_configuration(path_to_config: str) -> str:
    with open('%s/%s' % (exec_dir, path_to_config), 'r') as file:
        return json.loads(''.join(file.readlines()))

def convert_to_json(model: dict[str, any]) -> json:
    return json.dumps(model, indent = 4)

def convert_to_dict(raw_json: json) -> dict[str, any]:
    return json.loads(raw_json)

def get_from_declaration(declaration: dict[str, any], field: str) -> any:
    return declaration.get(field) if declaration_contains(declaration, field) else ''
