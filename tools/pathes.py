import json
import os

def __call_directory() -> str: # The directory where the program was called
    return str(os.getcwd())

def __work_directory() -> str: # The directory where the program was installed
    return str('/'.join(os.path.abspath(__file__).split('/')[0:-2]))

def __pathes(path: str) -> None:
    with open('%s' % path, 'r') as file:
        return json.loads(''.join(file.readlines()))

pathes = __pathes('%s/resources/configuration/pathes.json' % __work_directory())

# exports

configuration_pathes = pathes.get('configuration')
database_pathes      = pathes.get('databases')

database_dir         = pathes.get('database_dir')
projects_dir         = pathes.get('projects_dir')
airline_dir          = pathes.get('airline_dir')

declaration_file     = pathes.get('declaration')

archive_ext          = pathes.get('archive_ext')

exec_dir = __work_directory()
call_dir = __call_directory()