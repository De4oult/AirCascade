from tools.pathes     import exec_dir, call_dir, projects_dir, database_pathes, declaration_file, airline_dir, archive_ext
from tools.validators import path_exist
from tools.database   import Database 

from server.customs   import declarate

import tarfile as tar
import os

def pack(commit_hash: str) -> str: # Send all commited files to archive
    archive_path: str = '%s/%s/%s%s' % (call_dir, airline_dir, commit_hash, archive_ext)

    with tar.open(archive_path, 'w:xz') as archive:
        os.chdir('%s/%s/' % (call_dir, airline_dir))

        for address, _, files in os.walk('%s' % commit_hash):
            for name in files:
                archive.add(os.path.join(address, name))
        
        os.chdir(call_dir)

        return archive_path



# def unpack(archive_path: str) -> str: # Exctract commit into projects folder
#     file = archive_path.split('/')[-1]
#     path = '%s/%s/%s' % (exec_dir, projects_dir, file)
#     hash = file[:-7]

#     database = Database('%s/%s' % (exec_dir, database_pathes['projects']))

#     if not path_exist('%s/%s/%s' % (exec_dir, projects_dir, hash)):
#         with tar.open(path, 'r') as archive:
#             archive.extractall('%s/%s' % (exec_dir, projects_dir))

#     os.remove(path)

#     identifier = declarate('%s/%s/%s/%s' % (exec_dir, projects_dir, hash, declaration_file))

#     if not database_contains(database, 'identifier', identifier):
#         database.push({'identifier' : identifier})

#     return identifier, hash, '%s/%s/%s' % (exec_dir, projects_dir, hash)