'''
Contains all color related functions
'''

def purple(msg: str):
    return "\033[95m"+msg+"\033[0m"

def cyan(msg: str): 
    return "\033[96m"+msg+"\033[0m"

def blue(msg: str): 
    return "\033[94m"+msg+"\033[0m"

def green(msg: str): 
    return "\033[92m"+msg+"\033[0m"

def yellow(msg: str): 
    return "\033[93m"+msg+"\033[0m"

def red(msg: str): 
    return "\033[91m"+msg+"\033[0m"

def bold(msg: str):
    return "\033[1m"+msg+"\033[0m"

def underline(msg: str):
    return "\033[4m"+msg+"\033[0m"
