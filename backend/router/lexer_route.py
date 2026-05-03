from flask import Blueprint, request, jsonify
from service.lexer_service import tonkenizar

lexer_bp = Blueprint('lexer', __name__)

# Recibe el código fuente y devuelve los tokens
@lexer_bp.route('/tokenizar', methods=['POST'])
def tokenizar():
    data = request.get_json()
    
    if not data or 'codigo' not in data:
        return jsonify({'error': 'No se recibió código fuente'}), 400
    
    codigo = data['codigo']
    tokens = tonkenizar(codigo)
    
    return jsonify({'tokens': tokens}), 200