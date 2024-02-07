from datetime import date, datetime
from flaskr import create_app
from flaskr.views.views import VistaCategoriasUsuario, VistaLogIn, VistaSignUp, VistaTareasUsuario
from .models import db, Usuario
from flask_restful import Api
from .views import VistaUsuarios, VistaUsuario, VistaTareas, VistaTarea, VistaCategorias, VistaCategoria
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaSignUp, '/signup/')
api.add_resource(VistaLogIn, '/login/')
api.add_resource(VistaUsuarios, '/usuarios/')
api.add_resource(VistaUsuario, '/usuarios/<int:id_usuario>/')
api.add_resource(VistaTareas, '/tareas/')
api.add_resource(VistaTarea, '/tareas/<int:id_tarea>/')
api.add_resource(VistaCategorias, '/categorias/')
api.add_resource(VistaCategoria, '/categorias/<int:id_categoria>/')
api.add_resource(VistaTareasUsuario, '/tareas/usuario/')

jwt = JWTManager(app)