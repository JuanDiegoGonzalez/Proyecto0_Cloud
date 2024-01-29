from datetime import datetime
from flask_restful import Resource

from flaskr.models.models import Categoria, CategoriaSchema, Tarea, TareaSchema, Usuario, UsuarioSchema
from ..models import db
from flask import request

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()
categoria_schema = CategoriaSchema()

class VistaUsuarios(Resource):
    def get(self):
        return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
    
    def post(self):
        nuevo_usuario = Usuario(nombre_usuario=request.json['nombre_usuario'],
                                contrasenia=request.json['contrasenia'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario)
    
class VistaUsuario(Resource):
    def get(self, id_usuario):
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))
    
    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.nombre_usuario = request.json.get('nombre_usuario', usuario.nombre_usuario)
        usuario.contrasenia = request.json.get('contrasenia', usuario.contrasenia)
        db.session.commit()
        return usuario_schema.dump(usuario)
    
    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Operacion exitosa', 204
    
class VistaTareas(Resource):
    def get(self):
        return [tarea_schema.dump(tarea) for tarea in Tarea.query.all()]
    
    def post(self):
        nueva_tarea = Tarea(texto=request.json['texto'],
                            fecha_creacion=datetime.strptime(request.json['fecha_creacion'], "%Y-%m-%d").date(),
                            fecha_tentativa_finalizacion=datetime.strptime(request.json['fecha_tentativa_finalizacion'], "%Y-%m-%d").date(),
                            estado=request.json['estado'],
                            usuario=request.json['usuario'],
                            categoria=request.json['categoria'])
        db.session.add(nueva_tarea)
        db.session.commit()
        return tarea_schema.dump(nueva_tarea)
    
class VistaTarea(Resource):
    def get(self, id_tarea):
        return tarea_schema.dump(Tarea.query.get_or_404(id_tarea))
    
    def put(self, id_tarea):
        tarea = Tarea.query.get_or_404(id_tarea)
        tarea.texto = request.json.get('texto', tarea.texto)
        fecha_creacion = request.json.get('fecha_creacion')
        if fecha_creacion:
            tarea.fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d").date()
        fecha_tentativa_finalizacion = request.json.get('fecha_tentativa_finalizacion')
        if fecha_tentativa_finalizacion:
            tarea.fecha_tentativa_finalizacion = datetime.strptime(fecha_tentativa_finalizacion, "%Y-%m-%d").date()
        tarea.estado = request.json.get('estado', tarea.estado)
        tarea.usuario = request.json.get('usuario', tarea.usuario)
        tarea.categoria = request.json.get('categoria', tarea.categoria)
        db.session.commit()
        return tarea_schema.dump(tarea)
    
    def delete(self, id_tarea):
        tarea = Tarea.query.get_or_404(id_tarea)
        db.session.delete(tarea)
        db.session.commit()
        return 'Operacion exitosa', 204
    
class VistaCategorias(Resource):
    def get(self):
        return [categoria_schema.dump(categoria) for categoria in Categoria.query.all()]
    
    def post(self):
        nueva_categoria = Categoria(nombre=request.json['nombre'],
                                    descripcion=request.json['descripcion'])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schema.dump(nueva_categoria)
    
class VistaCategoria(Resource):
    def get(self, id_categoria):
        return categoria_schema.dump(Categoria.query.get_or_404(id_categoria))
    
    def put(self, id_categoria):
        categoria = Categoria.query.get_or_404(id_categoria)
        categoria.nombre = request.json.get('nombre', categoria.nombre)
        categoria.descripcion = request.json.get('descripcion', categoria.descripcion)
        db.session.commit()
        return categoria_schema.dump(categoria)
    
    def delete(self, id_categoria):
        categoria = Categoria.query.get_or_404(id_categoria)
        db.session.delete(categoria)
        db.session.commit()
        return 'Operacion exitosa', 204