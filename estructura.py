from controllers.conectores import conjuncion, disyuncion_inclusiva, disyuncion_exclusiva, condicion, bicondicion
from itertools import product


BOOL = [True, False]
CONECTORES = ['(', ')', '¬', '∧', '∨', '⊕', '→', '↔']
PROPOSICIONES = ['p', 'q', 'r']
PRECEDENCIA = {'¬': 4, '∧': 3, '∨': 3, '⊕': 3, '→': 2, '↔': 1}


def a_postfijo(tokens):
    salida = []
    pila = []
    for tok in tokens:
        if tok in PROPOSICIONES:
            salida.append(tok)
        elif tok == '¬':
            pila.append(tok)
        elif tok in PRECEDENCIA:
            while (pila and pila[-1] != '(' and
                   PRECEDENCIA.get(pila[-1], 0) >= PRECEDENCIA[tok]):
                salida.append(pila.pop())
            pila.append(tok)
        elif tok == '(':
            pila.append(tok)
        elif tok == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
    while pila:
        salida.append(pila.pop())
    return salida


def evaluar_postfijo(postfijo, valores):
    pila = []
    for tok in postfijo:
        if tok in PROPOSICIONES:
            pila.append(valores[tok])
        elif tok == '¬':
            a = pila.pop()
            pila.append(not a)
        else:
            b = pila.pop()
            a = pila.pop()
            if tok == '∧':
                pila.append(conjuncion(a, b))
            elif tok == '∨':
                pila.append(disyuncion_inclusiva(a, b))
            elif tok == '⊕':
                pila.append(disyuncion_exclusiva(a, b))
            elif tok == '→':
                pila.append(condicion(a, b))
            elif tok == '↔':
                pila.append(bicondicion(a, b))
    return pila[0]


def crear(estructura):
    valido, mensaje = validar_estructura(estructura)
    if not valido:
        raise ValueError(mensaje)

    tokens = list(estructura.replace(' ', ''))
    props_presentes = sorted(set(filter(lambda x: x in PROPOSICIONES, tokens)))
    cant_prop = len(props_presentes)
    rows = 2 ** cant_prop

    postfijo = a_postfijo(tokens)
    combinaciones = list(product(BOOL, repeat=cant_prop))

    table = []
    for combinacion in combinaciones:
        valores = dict(zip(props_presentes, combinacion))
        resultado = evaluar_postfijo(postfijo, valores)
        fila_vf = {clave: a_vf(val) for clave, val in valores.items()}
        fila_vf['resultado'] = a_vf(resultado)
        table.append(fila_vf)

    return table


def a_vf(valor):
    return 'V' if valor else 'F'


def validar_estructura(estructura):
    tokens = list(estructura.replace(' ', ''))

    if not tokens:
        return False, "La expresión está vacía"

    caracteres_validos = set(PROPOSICIONES) | set(CONECTORES)

    for tok in tokens:
        if tok not in caracteres_validos:
            return False, f"El símbolo '{tok}' no es válido"
 
    balance = 0
    for tok in tokens:
        if tok == '(':
            balance += 1
        elif tok == ')':
            balance -= 1
        if balance < 0:
            return False, "Hay un paréntesis de cierre ')' sin su apertura correspondiente"
   
    if balance != 0:
        return False, "Hay un paréntesis de apertura '(' sin cerrar"

    operadores_binarios = {'∧', '∨', '⊕', '→', '↔'}
    for i, tok in enumerate(tokens):
        if tok in operadores_binarios:
            anterior = tokens[i - 1] if i > 0 else None
            siguiente = tokens[i + 1] if i < len(tokens) - 1 else None
            if anterior is None or anterior in operadores_binarios or anterior == '(':
                return False, f"Falta un valor antes de '{tok}'"
            if siguiente is None or siguiente in operadores_binarios or siguiente == ')':
                return False, f"Falta un valor después de '{tok}'"

    return True, None