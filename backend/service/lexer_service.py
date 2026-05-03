from service.afnd_service import get_all_afds
from model.automata_model import AfdModel

AFDS = get_all_afds()

# Simulacion del AFD para verificar si una cadena es aceptada o no por el AFD
def _run_afd(afd: AfdModel, symbols: list) -> bool:
    state = afd.initial
    for symbol in symbols:
        state = afd.transitions.get(state, {}).get(symbol) # Le pregunta a la tabla de transiciones del AFD a donde va desde el estado actual con el símbolo actual
        if state is None:
            return False
    return state in afd.accepting

# Recibe un lexema y lo vuelve tipo String y lo clasifica
def _clasificar_lexema(lexema: str) -> str:
    if _run_afd(AFDS['RESERVADA'], list(lexema)):
        return 'RESERVADA'
    if _run_afd(AFDS['IDENTIFICADORES'], list(lexema)):   
        return 'IDENTIFICADOR'
    if _run_afd(AFDS['DECIMALES'], list(lexema)):
        return 'DECIMAL'
    if _run_afd(AFDS['LOGICOS'], list(lexema)):
        return 'LOGICO'
    if _run_afd(AFDS['ARITMETICOS'], list(lexema)):
        return 'ARITMETICO'
    return 'INVALIDO'

# Recibe un código fuente y lo tokeniza, es decir, devuelve una lista de tokens con su tipo y valor
def tonkenizar(codigo: str) -> list:
    tokens = []
    i = 0
    n = len(codigo)
    
    while i < n:
        if codigo[i].isspace():
            tokens.append({
                'lexema': codigo[i],
                'tipo': 'ESPACIO',
                'valido': True,
                'inicio': i,
                'fin': i + 1
            })
            i += 1
            continue
        
        #Maxima munch, es decir se busca el lexema ma largo posible
        mejor = None
        for longitud in range(n - i, 0, -1):
            lexema = codigo[i:i + longitud]
            tipo = _clasificar_lexema(lexema)
            if tipo != 'INVALIDO':
                mejor = {
                    'lexema': lexema,
                    'tipo': tipo,
                    'valido': True,
                    'inicio': i,
                    'fin': i + longitud
                }
                break
            
        if mejor:
            tokens.append(mejor)
            i = mejor['fin']
        else:
            tokens.append({
                'lexema': codigo[i],
                'tipo': 'INVALIDO',
                'valido': False,
                'inicio': i,
                'fin': i + 1
            })
            i += 1
    return tokens
