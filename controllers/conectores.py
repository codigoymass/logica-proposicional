def conjuncion(a, b):
    result = (a == True) and (b == True)
    return result

def disyuncion_inclusiva(a, b):
    result = (not a == False) and (not b == False)
    return result

def disyuncion_exclusiva(a, b):
    result = a != b
    return result

def condicion(a, b):
    result = (a == True) and (b == False)
    return result

def bicondicion(a, b):
    result = a == b
    return result