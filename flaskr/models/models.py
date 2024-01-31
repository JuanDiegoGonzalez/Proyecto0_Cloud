import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasenia = db.Column(db.String(128))
    tareas = db.relationship('Tarea', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "{}-{}".format(self.nombre_usuario, self.contrasenia)

class Estado(enum.Enum):
    SIN_EMPEZAR = 1
    EMPEZADA = 2
    FINALIZADA = 3

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(128))
    fecha_creacion = db.Column(db.Date)
    fecha_tentativa_finalizacion = db.Column(db.Date)
    estado = db.Column(db.Enum(Estado))
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    __table_args__ = (
        CheckConstraint('fecha_tentativa_finalizacion >= fecha_creacion', name='fecha_tentativa_finalizacion_despues_de_fecha_creacion'),
    )
    
    def __repr__(self):
        return "{}-{}-{}-{}-{}-{}".format(self.texto, self.fecha_creacion, self.fecha_tentativa_finalizacion, self.estado, self.usuario, self.categoria)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    descripcion = db.Column(db.String(128))
    tareas = db.relationship('Tarea')

    def __repr__(self):
        return "{}-{}".format(self.nombre, self.descripcion)
    
class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}

class TareaSchema(SQLAlchemyAutoSchema):
    estado = EnumADiccionario(attribute=('estado'))
    usuario = fields.Int()
    categoria = fields.Int()
    class Meta:
        model = Tarea
        include_relationships = True
        load_instance = True

class CategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships = True
        load_instance = True