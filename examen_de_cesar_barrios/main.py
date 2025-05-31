from flask import Flask
from cliente import cliente
app = Flask(__name__)

# Registrar el blueprint de cliente
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Examen de César sobre cliente'

if __name__ == "__main__":
    app.run(host='localhost', port=5003, debug=True)
    app.run(debug=True)