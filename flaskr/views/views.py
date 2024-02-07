from datetime import datetime
from flask_restful import Resource
from flaskr.models.models import Categoria, CategoriaSchema, Tarea, TareaSchema, Usuario, UsuarioSchema
from ..models import db
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()
categoria_schema = CategoriaSchema()

class VistaSignUp(Resource):
    def post(self):
        yaExisteElUsuario = Usuario.query.filter(Usuario.nombre_usuario == request.json["nombre_usuario"]).first()
        if yaExisteElUsuario:
            return {'error': 'Ya existe el usuario'}
        else:
            nuevo_usuario = Usuario(nombre_usuario=request.json['nombre_usuario'],
                                    contrasenia=request.json['contrasenia'])
            token_de_acceso = create_access_token(identity=request.json['nombre_usuario'])
            db.session.add(nuevo_usuario)
            db.session.commit()
            return {'mensaje': 'Usuario creado exitosamente',
                    'token_de_acceso': token_de_acceso,
                    'usuario': usuario_schema.dump(nuevo_usuario)}

class VistaLogIn(Resource):
    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre_usuario == request.json["nombre_usuario"], Usuario.contrasenia == request.json["contrasenia"]).first()
        db.session.commit()
        if usuario is None:
            return {"error":"El usuario no existe"}, 404
        else:
            token_de_acceso = create_access_token(identity = usuario.nombre_usuario)
            return {"mensaje":"Acceso concedido", "usuario": usuario_schema.dump(usuario), "token_de_acceso": token_de_acceso}

class VistaUsuarios(Resource):
    @jwt_required()
    def get(self):
        return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
    
class VistaUsuario(Resource):
    @jwt_required()
    def get(self, id_usuario):
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))
    
    @jwt_required()
    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.nombre_usuario = request.json.get('nombre_usuario', usuario.nombre_usuario)
        usuario.contrasenia = request.json.get('contrasenia', usuario.contrasenia)
        db.session.commit()
        return usuario_schema.dump(usuario)
    
    @jwt_required()
    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Operacion exitosa', 204
    
class VistaTareas(Resource):
    @jwt_required()
    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre_usuario == get_jwt_identity()).first()
        print(request.json['fecha_creacion'])
        nueva_tarea = Tarea(texto=request.json['texto'],
                            fecha_creacion=datetime.strptime(request.json['fecha_creacion'].split("T")[0], "%Y-%m-%d").date(),
                            fecha_tentativa_finalizacion=datetime.strptime(request.json['fecha_tentativa_finalizacion'], "%Y-%m-%d").date(),
                            estado=request.json['estado'],
                            usuario=usuario.id,
                            categoria=request.json['categoria'])
        print(nueva_tarea)
        db.session.add(nueva_tarea)
        usuario = Usuario.query.get_or_404(nueva_tarea.usuario)
        categoria = Categoria.query.get_or_404(nueva_tarea.categoria)
        usuario.tareas.append(nueva_tarea)
        categoria.tareas.append(nueva_tarea)
        db.session.commit()
        return tarea_schema.dump(nueva_tarea)

    @jwt_required()
    def get(self):
        return [tarea_schema.dump(tarea) for tarea in Tarea.query.all()]
    
class VistaTarea(Resource):
    @jwt_required()
    def get(self, id_tarea):
        return tarea_schema.dump(Tarea.query.get_or_404(id_tarea))
    
    @jwt_required()
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

    @jwt_required()
    def delete(self, id_tarea):
        tarea = Tarea.query.get_or_404(id_tarea)
        db.session.delete(tarea)
        db.session.commit()
        return 'Operacion exitosa', 204
    
class VistaCategorias(Resource):
    @jwt_required()
    def post(self):
        nueva_categoria = Categoria(nombre=request.json['nombre'],
                                    descripcion=request.json['descripcion'])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schema.dump(nueva_categoria)
    
    @jwt_required()
    def get(self):
        return [categoria_schema.dump(categoria) for categoria in Categoria.query.all()]
    
class VistaCategoria(Resource):
    @jwt_required()
    def get(self, id_categoria):
        return categoria_schema.dump(Categoria.query.get_or_404(id_categoria))

    @jwt_required()
    def put(self, id_categoria):
        categoria = Categoria.query.get_or_404(id_categoria)
        categoria.nombre = request.json.get('nombre', categoria.nombre)
        categoria.descripcion = request.json.get('descripcion', categoria.descripcion)
        db.session.commit()
        return categoria_schema.dump(categoria)
    
    @jwt_required()
    def delete(self, id_categoria):
        categoria = Categoria.query.get_or_404(id_categoria)
        db.session.delete(categoria)
        db.session.commit()
        return 'Operacion exitosa', 204
    
class VistaTareasUsuario(Resource):
    @jwt_required()
    def get(self):
        usuario = Usuario.query.filter(Usuario.nombre_usuario == get_jwt_identity()).first()
        return [tarea_schema.dump(tarea) for tarea in Tarea.query.filter(Tarea.usuario == usuario.id)]

class VistaCategoriasUsuario(Resource):
    @jwt_required()
    def get(self):
        usuario = Usuario.query.filter(Usuario.nombre_usuario == get_jwt_identity()).first()
        return [categoria_schema.dump(categoria) for categoria in Categoria.query.filter(Categoria.usuario == usuario.id)]