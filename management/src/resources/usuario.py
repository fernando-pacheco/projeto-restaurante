from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields

from src.models.usuario import UsuarioModel
from src.schemas.token import MessageSchema
from src.schemas.usuario import (
    UsuarioRequestGetSchema,
    UsuarioRequestPostSchema,
    UsuarioRequestPutSchema,
    UsuarioResponseSchema,
    usuario_schema,
)


@doc(description='Usuário Registro API', tags=['Usuário'])
class UsuarioRegisterResource(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(UsuarioRequestPostSchema, location='json')
    @doc(description='Registrar novo usuário')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao registrar um novo usuário'}, 400
        )

        if UsuarioModel.encontrar_por_nome_usuario(kwargs['nome_usuario']):
            resposta = make_response(
                {'message': 'Esse nome de usuário já existe'}, 400
            )
            
        if UsuarioModel.encontrar_por_email(kwargs['email']):
            resposta = make_response(
                {'message': 'Esse email já está cadastrado'}, 400
            )

        usuario = UsuarioModel(**kwargs)

        if usuario.salvar():
            resposta = make_response(usuario_schema.dump(usuario), 201)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(UsuarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(UsuarioRequestGetSchema, location='query')
    @use_kwargs(UsuarioRequestPutSchema, location='json')
    @doc(description='Atualizar usuário salvo')
    @jwt_required()
    def put(self, **kwargs):
        usuario_id = kwargs['usuario_id']
        usuario = UsuarioModel.encontrar_por_id(usuario_id)

        if not usuario:
            return make_response(
                {'message': 'ID de usuário não existente'}, 400
            )

        for campo, valor in kwargs.items():
            if (
                campo not in ['usuario_id', 'Authorization']
                and valor is not None
            ):

                if campo == 'senha':
                    usuario.definir_senha(valor)

                elif hasattr(usuario, campo):
                    if isinstance(getattr(usuario, campo), bool):
                        valor = str(valor).lower() == 'true'

                    setattr(usuario, campo, valor)

                else:
                    return make_response(
                        {'message': f'O campo {campo} não é válido.'}, 400
                    )

        usuario.salvar()

        return make_response(usuario_schema.dump(usuario), 201)

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(UsuarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(UsuarioRequestGetSchema, location='query')
    @doc(description='Obter usuário pelo ID')
    @jwt_required()
    def get(self, **kwargs):
        usuario_id = kwargs['usuario_id']
        usuario = UsuarioModel.encontrar_por_id(usuario_id)
        resposta = make_response({'message': 'Usuário não encontrado'}, 404)

        if usuario:
            resposta = make_response(usuario_schema.dump(usuario), 200)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(MessageSchema, code=201)
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(UsuarioRequestGetSchema, location='query')
    @doc(description='Excluir usuário por ID')
    @jwt_required()
    def delete(self, **kwargs):
        usuario_id = kwargs['usuario_id']
        usuario = UsuarioModel.encontrar_por_id(usuario_id)
        resposta = make_response({'message': 'Usuário não encontrado'}, 404)

        if usuario:
            usuario.excluir()
            resposta = make_response(
                {'message': 'Usuário excluído com sucesso'}, 201
            )

        return resposta
