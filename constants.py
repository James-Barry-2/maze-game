<<<<<<< HEAD
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def format_cell(cell, see_all):
    if cell == 'H':
        return f"{color.BLUE}{color.BOLD}H{color.END}"
    elif cell == 'M':
        if see_all:
            return f"{color.RED}M{color.END}"
        else:
            return '  '
    elif cell == '?':
        if see_all:
            return f"{color.YELLOW}?{color.END}"
        else:
            return '   '
    elif cell == 'E':
        return f"{color.PURPLE}E{color.END}"
    elif cell == 'X':
        return f"{color.GREEN}X{color.END}"
    elif cell == '':
        return '  '
    else:
        return str(cell)
    
def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)
=======
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def format_cell(cell, see_all):
    if cell == 'H':
        return f"{color.BLUE}{color.BOLD}H{color.END}"
    elif cell == 'M':
        if see_all:
            return f"{color.RED}M{color.END}"
        else:
            return '  '
    elif cell == '?':
        if see_all:
            return f"{color.YELLOW}?{color.END}"
        else:
            return '   '
    elif cell == 'E':
        return f"{color.PURPLE}E{color.END}"
    elif cell == 'X':
        return f"{color.GREEN}X{color.END}"
    elif cell == '':
        return '  '
    else:
        return str(cell)
    
def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)
>>>>>>> 2b0734f8ce33ed860adc69e4354616b534041f9d
