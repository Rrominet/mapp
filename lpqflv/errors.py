class type(Exception) :
    def __init__(self, var, expected, funcName) :
        msg = "[" + funcName + "] : bad Type !\nGot " + str(type(var)) + " but was expected : " + expected + ".\n Variable : " + str(var)
        super().__init__(msg)

class empty(Exception) :
    def __init__(self, varName, funcName) :
        msg = "[" + funcName + "] : " + varName + " is empty."
        super().__init__(msg)

class bad_length(Exception) :
    def __init__(self, listName, expectedLength, ls, funcName) :
        msg = "[" + funcName + "] : " + listName + " is of bad length.\nGot : " + str(len(ls)) + " but expected : " + str(expectedLength)
        super().__init__(msg)

class not_found(Exception) :
    def __init__(self, msg, funcName) :
        msg = "[" + funcName + "] : " + msg
        super().__init__(msg)

def checkType(var, type, funcName) : 
    if not isinstance(var, type) : 
        raise type(var, str(type), funcName)
