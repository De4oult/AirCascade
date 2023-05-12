
import json

def declarate(path_to_declaration: str) -> dict[str, any]:
    with open(path_to_declaration, 'r') as file:
        return json.loads(''.join(file.readlines()))