from datetime import date, datetime
from flaskr import create_app
from flaskr.models.models import Categoria, CategoriaSchema, Estado, Tarea, TareaSchema, UsuarioSchema
from .models import db, Usuario
from flask_restful import Api
from .views import VistaUsuarios, VistaUsuario, VistaTareas, VistaTarea, VistaCategorias, VistaCategoria

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaUsuario, '/cancion/<int:id_usuario>')
api.add_resource(VistaTareas, '/tareas')
api.add_resource(VistaTarea, '/cancion/<int:id_tarea>')
api.add_resource(VistaCategorias, '/categorias')
api.add_resource(VistaCategoria, '/cancion/<int:id_categoria>')

# Prueba
with app.app_context():
    usuario_schema = UsuarioSchema()
    tarea_schema = TareaSchema()
    categoria_schema = CategoriaSchema()

    u = Usuario(nombre_usuario='Brenda', contrasenia='password')
    t = Tarea(texto='Texto de prueba', fecha_creacion=datetime.now().date(), fecha_tentativa_finalizacion=date(2025, 2, 11), estado=Estado.SIN_EMPEZAR)
    c = Categoria(nombre='Universidad', descripcion='Tareas de la universidad')

    u.tareas.append(t)
    c.tareas.append(t)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print("-------------------")
    print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])
    print([tarea_schema.dumps(tarea) for tarea in Tarea.query.all()])
    print([categoria_schema.dumps(categoria) for categoria in Categoria.query.all()])
    print([tarea_schema.dumps(tarea) for tarea in Usuario.query.all()[0].tareas])
    print([tarea_schema.dumps(tarea) for tarea in Categoria.query.all()[0].tareas])
    print("-------------------")

    db.session.delete(c)
    db.session.commit()
    print("-------------------")
    print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])
    print([tarea_schema.dumps(tarea) for tarea in Tarea.query.all()])
    print([categoria_schema.dumps(categoria) for categoria in Categoria.query.all()])
    print("-------------------")

    db.session.delete(u)
    db.session.commit()
    print("-------------------")
    print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])
    print([tarea_schema.dumps(tarea) for tarea in Tarea.query.all()])
    print([categoria_schema.dumps(categoria) for categoria in Categoria.query.all()])
    print("-------------------")