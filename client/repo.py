from tools.messages    import err_repo_alrd_inited, succ_repo_succ_inited, err_no_repo_inited, succ_repo_succ_deleted, succ_commit_succ_inited, err_smthing_went_wrong
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
    declaration: dict[str, any] = validate_declaration('%s/%s' % (call_dir, declaration_file))
    files      : any            = get_from_declaration(declaration, 'files')
    hash       : str            = commit_hash()

    copy_files(files, '%s/%s/%s/' % (call_dir, airline_dir, hash))

    database = Database('%s/%s' % (exec_dir, database_pathes['repositories']))

    repository: dict[str, any] = database.get_instance('path', '%s' % call_dir)
    commits   : list[str]      = repository.get('commits')

    commits .append(models.commit(label, hash))
    database.update(repository.get('id'), 'commits', commits)

    succ_commit_succ_inited()

def deliver() -> None:
    declaration: dict[str, any] = validate_declaration('%s/%s' % (call_dir, declaration_file))
    
    database = Database('%s/%s' % (exec_dir, database_pathes['repositories']))

    try:
        commits: list[str] = database.get_instance('path', '%s' % call_dir).get('commit')

        # archive and send
    
    except:
        err_smthing_went_wrong()

def fast_delivery(label: str) -> None:
    pass

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

    