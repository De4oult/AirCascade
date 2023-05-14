from tools.messages   import err_empty_commit, warn_no_file_in_dir, succ_files_succ_commited
from tools.validators import path_must_exist, path_exist, path_file_format
from tools.pathes     import call_dir, airline_dir

import shutil
import os

def copy_files(files: list[str], commit_path: str) -> None:
    if len(files) == 0: err_empty_commit()

    path_must_exist(commit_path)

    for filename in files:
        if not path_exist('%s/%s' % (call_dir, filename)): warn_no_file_in_dir(); continue

        file = path_file_format('%s/%s' % (call_dir, filename))
        
        if os.path.isdir(file):
            if file == '%s/' % airline_dir: continue

            shutil.copytree('%s' % file, '%s/%s' % (commit_path, filename)) 
            continue

        shutil.copyfile('%s' % file, '%s/%s' % (commit_path, filename))

    succ_files_succ_commited()
        