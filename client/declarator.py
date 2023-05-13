from tools.messages   import err_no_repo_declaration, err_empty_declaration, err_empty_server
from tools.validators import path_exist, declaration_filled, server_filled
from tools.funcs      import convert_to_json, convert_to_dict
from tools.pathes     import call_dir, declaration_file
from client           import models

def create_declaration() -> None:
    if path_exist('%s/%s' % (call_dir, declaration_file)): return

    with open('%s/%s' % (call_dir, declaration_file), 'w+') as file:
        file.write(
            convert_to_json(
                models.declaration()
            )
        )
    
def validate_declaration(path: str) -> dict[str, any]:
    declaration = __read_declaration(path)
    if not declaration_filled(declaration): err_empty_declaration();
    if not server_filled(declaration):      err_empty_server();
    return declaration

def __read_declaration(path: str) -> dict[str, any]:
    if not path_exist('%s' % path): err_no_repo_declaration(); exit()
    
    with open('%s' % path) as file:
        return convert_to_dict(''.join(file.readlines()))