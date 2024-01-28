from datetime import date, datetime
from flaskr import create_app
from flaskr.models.models import Categoria, Estado, Tarea
from .models import db, Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Prueba
with app.app_context():
    u = Usuario(nombre_usuario='Brenda', contrasenia='password')
    t = Tarea(texto='Texto de prueba', fecha_creacion=datetime.now().date(), fecha_tentativa_finalizacion=date(2025, 2, 11), estado=Estado.SIN_EMPEZAR)
    c = Categoria(nombre='Universidad', descripcion='Tareas de la universidad')

    u.tareas.append(t)
    c.tareas.append(t)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print("-------------------")
    print(Usuario.query.all())
    print(Tarea.query.all())
    print(Categoria.query.all())
    print(Usuario.query.all()[0].tareas)
    print(Categoria.query.all()[0].tareas)
    print("-------------------")

    db.session.delete(c)
    db.session.commit()
    print("-------------------")
    print(Usuario.query.all())
    print(Tarea.query.all())
    print(Categoria.query.all())
    print("-------------------")

    db.session.delete(u)
    db.session.commit()
    print("-------------------")
    print(Usuario.query.all())
    print(Tarea.query.all())
    print(Categoria.query.all())
    print("-------------------")