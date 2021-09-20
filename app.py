from flask import Flask, Blueprint
from crud.api import api
from crud.api.view import api as villain_ns
from flask_cors import CORS


app = Flask(__name__)
blueprint = Blueprint('api', __name__)
# Pontos do Serviço
app.register_blueprint(blueprint)

api.init_app(app)
api.add_namespace(villain_ns, path='/villain')

# Recursos
cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000
    debug=True
    app.run(host, port, debug) 

