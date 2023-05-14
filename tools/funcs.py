from tools.validators import declaration_contains
from tools.pathes     import exec_dir

from datetime import datetime

import hashlib
import json

def get_from_configuration(path_to_config: str) -> str:
    with open('%s/%s' % (exec_dir, path_to_config), 'r') as file:
        return json.loads(''.join(file.readlines()))

def convert_to_json(model: dict[str, any]) -> json:
    return json.dumps(model, indent = 4)

def convert_to_dict(raw_json: json) -> dict[str, any]:
    return json.loads(raw_json)

def get_from_declaration(declaration: dict[str, any], field: str) -> any:
    return declaration.get(field) if declaration_contains(declaration, field) else ''

def commit_hash() -> str:
    return hashlib.sha256(datetime.strftime(datetime.now(), "%H:%M:%S:%f %d-%m-%Y").encode()).hexdigest()


        