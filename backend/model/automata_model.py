#Definicion del modelo AFND 
class AfndModel:
    def __init__(self, states, alphabet, initial, accepting, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial
        self.accepting = accepting
        self.transitions = transitions
        
    def to_dict(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'initial': self.initial,
            'accepting': self.accepting,
            'transitions': self.transitions 
        }
#Definicion del modelo AFD       
class AfdModel:
    def __init__(self, states, alphabet, initial, accepting, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial
        self.accepting = accepting
        self.transitions = transitions
        
    def to_dict(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'initial': self.initial,
            'accepting': self.accepting,
            'transitions': self.transitions
        }