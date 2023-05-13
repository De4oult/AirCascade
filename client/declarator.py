from tools.messages   import err_no_repo_declaration, err_empty_declaration
from tools.funcs      import convert_to_json, convert_to_dict
from tools.validators import path_exist, declaration_filled
from tools.pathes     import call_dir
from client           import models

def create_declaration() -> None:
    if path_exist('%s/Declaration' % call_dir): return

    with open('%s/Declaration' % call_dir, 'w+') as file:
        file.write(
            convert_to_json(
                models.declaration()
            )
        )

def read_declaration(path: str) -> str:
    if not path_exist('%s/Declaration' % call_dir): err_no_repo_declaration(); exit()
    
    with open('%s/%s' % (call_dir, path)) as file:
        return convert_to_dict(''.join(file.readlines()))
    

def validate_declaration(declaration: dict[str, any]) -> None:
    if not declaration_filled(declaration): err_empty_declaration(); exit()

    