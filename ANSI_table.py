from Tools import member_loader


def Check_CMD():
    from psutil import Process
    import os
    if 'exe' in Process(os.getpid()).parent().name():
        return True
    else:
        return False


def Clear_Screen(Run=[]):
    '''
    Uses kwarg list's global-like property to store state
    ..Not sure if that was a good idea, rather than using global variables
    '''
    import os

    if not Run:
        Run.append(Check_CMD())

    if Run[0]:
        os.system('cls')
    else:
        os.system('clear')


def Check_ANSI(output=True):
    if Check_CMD():

        if output:
            print("ANSI incompetible, Importing Colorama.init")

        from colorama import init
        init()

    else:
        if output:
            print("Running on ANSI compatable Terminal.")


class EscapeCode:
    BR_BLACK = '\033[90m'
    BR_RED = '\033[91m'
    BR_GREEN = '\033[92m'
    BR_YEL = '\033[93m'
    BR_BLUE = '\033[94m'
    BR_MAGENTA = '\033[95m'
    BR_CYAN = '\033[96m'
    BR_WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


def Colorize(txt, color):
    return getattr(EscapeCode, color) + str(txt) + getattr(EscapeCode, "RESET")
