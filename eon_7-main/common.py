#common.py - 공통적으로 사용할 만한 기능 
def input_int(msg=''): 
    try: 
        ns = input(msg) 
        return int(ns) 
    except: 
            return 0 
def tryinput_int(msg=''): 
    try: 
        ns = input(msg) 
        return int(ns),True 
    except: 
        return 0,False
