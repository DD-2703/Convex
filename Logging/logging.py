'''
Contains all logging-related functions.
'''

_private_log_level: int = 0

def Log(variable):
    print("[DEBUG]      "+variable)

def PInfo(msg: str, level_matters:bool=False):
    if level_matters:
        if _private_log_level==0:
            print("[INFO]       "+msg)
            return
        else: return
    print("[INFO]       "+msg)

def PWarn(msg: str, level_matters:bool=False):
    if level_matters:
        if globals()['_private_log_level']<=1:
            print("[WARNING]    "+msg)
            globals()['_private_log_level'] = 1
            return
        else: return
    print("[WARNING]    "+msg)

def PException(msg: str, level_matters:bool=False):
    if level_matters:
        if globals()['_private_log_level']<=2:
            print("[EXCEPTION]  "+msg)
            globals()['_private_log_level'] = 2
            return
        else: return
    print("[EXCEPTION]  "+msg)

def PCritical(msg: str):
    print("[CRITICAL]   "+msg)
    exit(1)

def Info(msg: str, level_matters:bool=False):
    if level_matters:
        if _private_log_level==0:
            print("\033[92m[INFO]       "+msg+'\033[0m')
            return
        else: return
    print("\033[92m[INFO]       "+msg+'\033[0m')

def Warn(msg: str, level_matters:bool=False):
    if level_matters:
        if globals()['_private_log_level']<=1:
            print("\033[93m[WARNING]    "+msg+'\033[0m')
            globals()['_private_log_level'] = 1
            return
        else: return
    print("\033[93m[WARNING]    "+msg+'\033[0m')

def Exception(msg: str, level_matters:bool=False):
    if level_matters:
        if globals()['_private_log_level']<=2:
            print("\033[91m[EXCEPTION]  "+msg+'\033[0m')
            globals()['_private_log_level'] = 2
            return
        else: return
    print("\033[91m[EXCEPTION]  "+msg+'\033[0m')

def Critical(msg: str):
    print("\033[91m\033[1m[CRITICAL]   "+msg+'\033[0m\033[0m')
    exit(1)