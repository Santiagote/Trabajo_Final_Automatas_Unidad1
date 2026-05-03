from flask import Flask
from flask_cors import CORS
from router.lexer_route import lexer_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

app.register_blueprint(lexer_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)