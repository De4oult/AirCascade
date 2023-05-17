from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers    import FTPHandler
from pyftpdlib.servers     import FTPServer

from tools.messages        import err_empty_server_config, info_server_was_runned
from tools.validators      import server_config
from tools.funcs           import get_from_configuration
from tools.pathes          import configuration_pathes, exec_dir, projects_dir

import os

def server() -> None:
    config: dict[str, any] = get_from_configuration(configuration_pathes.get('server'))
    if not server_config(config): err_empty_server_config()

    authorizer = DummyAuthorizer()
    handler    = CascadeHandler

    authorizer.add_user(config.get('username'), config.get('password'), '%s/%s' % (exec_dir, projects_dir), perm = 'elradfmwMT')
    
    handler.authorizer = authorizer

    server = FTPServer((config.get('server_address'), config.get('server_port')), handler)
    
    info_server_was_runned()
    
    server.serve_forever()


class CascadeHandler(FTPHandler):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_login(self, username):
        pass

    def on_logout(self, username):
        pass

    def on_file_sent(self, file):
        pass

    def on_file_received(self, file):
        pass

    def on_incomplete_file_sent(self, file):
        pass

    def on_incomplete_file_received(self, file):
        os.remove(file)