from funcs  import get_from_configuration
from pathes import configuration_pathes 

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
            case 'comment':
                print(Fore.MAGENTA + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)
            case 'text':
                print(Fore.CYAN    + '[%s] -> %s' % (self.type.upper(), self.text) + Style.RESET_ALL)


__messages: dict[str, dict[str, str]] = get_from_configuration(configuration_pathes['messages']) 
print(__messages)

err1 = __Message('Runtime Exception', 'Information')

err1()