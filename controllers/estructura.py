from controllers.conectores import conjuncion, disyuncion_inclusiva, disyuncion_exclusiva, condicion, bicondicion

BOOL = [True, False]
CONECTORES = ['(', ')', '¬', '∧', '⊕', '→', '↔']
PROPOSICIONES = ['p', 'q', 'r']

def crear(estructura):
    data = list(estructura)
    cant_prop = len(list(set(filter(lambda x: x in PROPOSICIONES, data))))
    
    rows = 2 ** cant_prop
    
    table = list()
    return rows
    