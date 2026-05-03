from flask import Flask
from router.lexer_route import lexer_bp

app = Flask(__name__)

app.register_blueprint(lexer_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)