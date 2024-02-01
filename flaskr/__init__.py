from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_proyecto0.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secret-key'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app