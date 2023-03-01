'''
Contains all logging-related functions.
'''

__log_level: int = 0

def Log(variable):
    print("[DEBUG]      "+variable)

def Info(msg: str, level_matters=False):
    if level_matters:
        if __log_level==0:
            print("[INFO]       "+msg)
            return
        else: return
    print("[INFO]       "+msg)

def Warn(msg: str, level_matters=False):
    if level_matters:
        if __log_level<=1:
            print("[WARNING]    "+msg)
            __log_level = 1
            return
        else: return
    print("[WARNING]    "+msg)

def Exception(msg: str, level_matters=False):
    if level_matters:
        if __log_level<=2:
            print("[EXCEPTION]  "+msg)
            __log_level = 2
            return
        else: return
    print("[EXCEPTION]  "+msg)

def Critical(msg: str):
    print("[CRITICAL]   "+msg)
    exit(1)
