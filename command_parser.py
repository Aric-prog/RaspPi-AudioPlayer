import validators
from config.constants import COMM_LIST, DISCONNECT_MESSAGE

class command_parser():
    def separate(self,command):
        # Commands that doesn't need arguments
        COMM_NO_ARGS = ['skip', DISCONNECT_MESSAGE, 'q','queue']
        syntax = command.strip()
        arg = ""
        
        command = command.strip()
        syntax_len = 0
        for i in command:
            if(i == " "):
                syntax = command[:syntax_len]
                syntax = syntax.lower()
                arg = command[syntax_len:]
                arg = arg.strip()
                break
            syntax_len += 1
        
        if syntax in COMM_NO_ARGS:
            return syntax, arg
        elif syntax not in COMM_LIST:
            print("Unknown command")
            return False
        elif arg == "":
            print("Must have argument after command. (URL or keyword)")
            return False
        else:
            return syntax,arg

    def is_url(self,arg):
        return validators.url(arg)

