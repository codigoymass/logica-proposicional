def conjuncion(a, b):
    result = a and b
    return result

def disyuncion_inclusiva(a, b):
    result = a or b
    return result

def disyuncion_exclusiva(a, b):
    result = a != b
    return result

def condicion(a, b):
    result = a and (not b)
    return result

def bicondicion(a, b):
    result = a == b
    return result