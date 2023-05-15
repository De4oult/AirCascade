from tools.pathes import call_dir
from ftplib       import FTP

import os

def send_to_server(declaration: dict[str, any], archive_path: str, commit_hash: str) -> None:
    server_configuration: dict[str, any] = declaration.get('server')
    
    with FTP(server_configuration.get('address')) as client:
        client.login(
            server_configuration.get('username'), 
            server_configuration.get('password')
        )
        client.storbinary('STOR %s.tar.xz' % (declaration.get('identifier')), open(archive_path, 'rb'))
    
    os.remove('%s' % archive_path)