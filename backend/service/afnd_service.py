from model.automata_model import AfndModel, AfdModel
import string

LETRAS = list(string.ascii_letters) # Es la lista de las letras
DIGITOS = list(string.digits) # Es la lista de los dígitos

def _set_name(state_set: frozenset) -> str:
    return '_'.join(sorted(state_set))
#Conversion AFND a AFD

def afnd_to_afd(afnd: AfndModel) -> AfdModel:
    initial_set = frozenset([afnd.initial])
    queue = [initial_set]
    visited = {}
    afd_transitions = {}
    afd_accepting = []

    while queue:
        current_set = queue.pop(0)
        current_name = _set_name(current_set)
        
        if current_name in visited:
            continue
        
        visited[current_name] = current_set
        afd_transitions[current_name] = {}
        
        if any(state in afnd.accepting for state in current_set):
            afd_accepting.append(current_name)
            
        for symbol in afnd.alphabet:
            next_set = set()
            for state in current_set:
                targets = afnd.transitions.get(state, {}).get(symbol, []) #busca en la tabla AFND desde el estado donde estoy a donde voy
                next_set.update(targets) #agrega todos los destinos a donde puede ir
            
            if next_set:
                next_name = _set_name(frozenset(next_set))
                afd_transitions[current_name][symbol] = next_name
                if frozenset(next_set) not in visited.values():
                    queue.append(frozenset(next_set))
            else:
                afd_transitions[current_name][symbol] = None

    return AfdModel(
        states=list(visited.keys()),
        alphabet=afnd.alphabet,
        transitions=afd_transitions,
        initial=_set_name(initial_set),
        accepting=afd_accepting
    )

#Defincion de los AFND
def afnd_identificadores() -> AfndModel:
    alphabet = LETRAS + DIGITOS # El alfabeto es la combinación de letras y dígitos
    
    #No se se puede usar una lista como clave, por lo que ahora cada caracter es su propia clave
    transitions_q1 = {caracter: ['q1'] for caracter in alphabet}
    transitions_q0 = {caracter: ['q1'] for caracter in LETRAS}
    return AfndModel(
        states=['q0', 'q1'],
        alphabet=alphabet,  
        transitions={
            'q0': transitions_q0,
            'q1': transitions_q1
        },        
        initial='q0',
        accepting=['q1']
    )      
    
def afnd_decimales() -> AfndModel:
    alphabet = DIGITOS + ['.'] # El alfabeto es solo dígitos
    return AfndModel(
        states=['q0', 'q1', 'q2', 'q3'],
        alphabet=alphabet,   
        transitions={
            'q0': {caracter: ['q1'] for caracter in DIGITOS},
            'q1': {
                **{caracter: ['q1'] for caracter in DIGITOS}, #** es para fucionar los dos diccionarios, el primero es para los dígitos y el segundo es para el punto
                '.': ['q2']
            },
            'q2': {caracter: ['q3'] for caracter in DIGITOS},
            'q3': {caracter: ['q3'] for caracter in DIGITOS},
        },        
        initial='q0',
        accepting=['q1', 'q3']
    )
    
def afnd_logicos() -> AfndModel:
    return AfndModel(
        states=['q0', 'q1', 'q2', 'q3'],
        alphabet = ['&', '|'],
        transitions={
            'q0': {'&': ['q1'], '|': ['q2']},
            'q1': {'&': ['q3']},
            'q2': {'|': ['q3']}
        },
        initial='q0',
        accepting=['q3']
    )
    
def afnd_palabras_reservadas() -> AfndModel:
    return AfndModel(
        states=['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11'],
        alphabet=['i', 'f', 'e', 'l', 's', 'w', 'h'],
        transitions={
            'q0': {'i': ['q1'], 'e': ['q3'], 'w': ['q7']},
            'q1': {'f': ['q2']},
            'q2': {},
            'q3': {'l': ['q4']},
            'q4': {'s': ['q5']},
            'q5': {'e': ['q6']},
            'q6': {},
            'q7': {'h': ['q8']},
            'q8': {'i': ['q9']},
            'q9': {'l': ['q10']},
            'q10': {'e': ['q11']},
            'q11': {}
        },
        initial='q0',
        accepting=['q2', 'q6', 'q11']
    )
    
def afnd_aritmeticos() -> AfndModel:
    return AfndModel(
        states=['q0', 'q1'],
        alphabet=['+', '-', '*', '/'],
        transitions={
            'q0': {'+': ['q1'], '-': ['q1'], '*': ['q1'], '/': ['q1']}
        },
        initial='q0',
        accepting=['q1']
    )
    
#Obtener todos los AFD
def get_all_afds():
    return {
        'RESERVADA': afnd_to_afd(afnd_palabras_reservadas()),
        'IDENTIFICADORES': afnd_to_afd(afnd_identificadores()),
        'DECIMALES': afnd_to_afd(afnd_decimales()),
        'LOGICOS': afnd_to_afd(afnd_logicos()),
        'ARITMETICOS': afnd_to_afd(afnd_aritmeticos())
    }