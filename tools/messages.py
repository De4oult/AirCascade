from tools.funcs  import get_from_configuration
from tools.pathes import configuration_pathes 

from colorama import Fore, Style

class __Message:
    def __init__(self, text: str = '', type: str = '') -> None:
        self.text = text
        self.type = type

    def __str__(self) -> str:
        return '%s: %s' % (self.type, self.text)
    
    def __call__(self) -> None:
        match self.type.lower():
            case 'information':
                print(Fore.BLUE    + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
            case 'success':
                print(Fore.GREEN   + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
            case 'warning':
                print(Fore.YELLOW  + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
            case 'error':
                print(Fore.RED     + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
                exit()
            case 'comment':
                print(Fore.MAGENTA + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
            case 'text':
                print(Fore.CYAN    + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)


__messages: dict[str, dict[str, str]] = get_from_configuration(configuration_pathes['messages']) 



### INFOS

info_server_configurated = __Message(__messages['info']['server_configurated'], 'information')

### SUCCS

succ_repo_succ_inited    = __Message(__messages['success']['repo_succ_inited'],    'success')
succ_files_succ_commited = __Message(__messages['success']['files_succ_commited'], 'success')
succ_file_succ_commited  = __Message(__messages['success']['file_succ_commited'],  'success')
succ_commit_succ_inited  = __Message(__messages['success']['commit_succ_inited'],  'success')
succ_commit_succ_sended  = __Message(__messages['success']['commit_succ_sended'],  'success')

### WARNS

warn_file_in_ignore      = __Message(__messages['warnings']['file_in_ignore'], 'warning')

### ERRORS

err_repo_alrd_inited    = __Message(__messages['errors']['repo_alrd_inited'],    'error')
err_file_alrd_commited  = __Message(__messages['errors']['file_alrd_commited'],  'error')
err_empty_commit        = __Message(__messages['errors']['empty_commit'],        'error')
err_empty_server_config = __Message(__messages['errors']['empty_server_config'], 'error')
err_no_repo_declaration = __Message(__messages['errors']['no_repo_declaration'], 'error')
err_empty_declaration   = __Message(__messages['errors']['empty_declaration'],   'error')
err_empty_server        = __Message(__messages['errors']['empty_server'],        'error')

### TESTS

if __name__ == '__main__':
    info_server_configurated()
    succ_repo_succ_inited()
    succ_files_succ_commited()
    succ_file_succ_commited()
    succ_commit_succ_inited()
    succ_commit_succ_sended()
    warn_file_in_ignore()
    err_repo_alrd_inited()
    err_file_alrd_commited()
    err_empty_commit()
    err_empty_server_config()
    err_no_repo_declaration()
    err_empty_declaration()