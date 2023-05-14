from tools.messages    import err_repo_alrd_inited, succ_repo_succ_inited, err_no_repo_inited, succ_repo_succ_deleted
from tools.pathes      import exec_dir, call_dir, database_dir, database_pathes, declaration_file, airline_dir
from tools.validators  import path_must_exist, repository_already_initialized
from tools.funcs       import get_from_declaration, commit_hash
from tools.database    import Database

from client.declarator import create_declaration, validate_declaration
from client.files      import copy_files
from client            import models

path_must_exist('%s/%s' % (exec_dir, database_dir))
path_must_exist('%s/%s' % (call_dir, airline_dir))

def declarate() -> None:
    create_declaration()

def initialize() -> None:
    database    = Database('%s/%s' % (exec_dir, database_pathes['repositories']))
    declaration = validate_declaration('%s/%s' % (call_dir, declaration_file))

    if repository_already_initialized(database, call_dir): err_repo_alrd_inited()

    database.push(
        models.repository(
            declaration,
            call_dir
        )
    )

    succ_repo_succ_inited()
    

def label(label: str) -> None:
    declaration = validate_declaration('%s/%s' % (call_dir, declaration_file))

    files = get_from_declaration(declaration, 'files')

    copy_files(files, '%s/%s/%s/' % (call_dir, airline_dir, commit_hash()))

    database = Database('%s/%s' % (exec_dir, database_pathes['repositories']))

    # add commit_model to db

def drop() -> None:
    database = Database('%s/%s' % (exec_dir, database_pathes['repositories']))

    if not repository_already_initialized(database, call_dir): err_no_repo_inited()

    database.delete(
        database.get(
            'path',
            call_dir,
            'id'
        )
    )

    succ_repo_succ_deleted()

    