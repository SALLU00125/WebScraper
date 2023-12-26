a="123"

def customMethod(a,method,parm=None):
    if parm is None:
        Method = getattr(a, method, None)