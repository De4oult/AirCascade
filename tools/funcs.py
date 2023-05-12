import json
import os

def get_from_configuration(path_to_config: str) -> str:
    with open(path_to_config, 'r') as file:
        return json.loads(''.join(file.readlines()))
