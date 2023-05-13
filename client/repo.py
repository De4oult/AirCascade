from tools.pathes      import exec_dir, call_dir, database_dir, database_pathes, declaration_file 
from tools.validators  import path_must_exist, repository_already_initialized
from tools.messages    import err_repo_alrd_inited, succ_repo_succ_inited
from tools.database    import Database

from client.declarator import create_declaration, validate_declaration
from client            import models

def declarate() -> None:
    create_declaration()

def initialize() -> None:
    path_must_exist('%s/%s' % (exec_dir, database_dir))

    database = Database('%s/%s' % (exec_dir, database_pathes['repositories']))
    declaration = validate_declaration('%s/%s' % (call_dir, declaration_file))

    if repository_already_initialized(database, call_dir): err_repo_alrd_inited()

    database.push(
        models.repository(
            declaration,
            call_dir
        )
    )

    succ_repo_succ_inited()

