from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow import fields
from src.models.usuario import UsuarioModel
from src.schemas.message import MessageSchema
from src.schemas.usuario import (
    UsuarioRequestGetSchema,
    UsuarioRequestPostSchema,
    UsuarioRequestPutSchema,
    UsuarioResponseSchema,
    usuario_schema,
)
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@doc(description='Usuário Registro API', tags=['Usuários'])
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

        if UsuarioModel.encontrar_por_cpf(kwargs['cpf']):
            resposta = make_response(
                {'message': 'Esse cpf já está cadastrado.'}, 400
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

        if str(usuario_id) == get_jwt_identity():
            if usuario:
                usuario, resposta = atualizar_objeto(kwargs, usuario)

                if usuario.salvar():
                    resposta = make_response(usuario_schema.dump(usuario), 200)

            else:
                resposta = make_response(
                    {'message': 'ID de usuário não existente'}, 400
                )
        else:
            resposta = retorno_nao_autorizado()

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
    @marshal_with(MessageSchema, code=404)
    @use_kwargs(UsuarioRequestGetSchema, location='query')
    @doc(description='Obter usuário pelo ID')
    @jwt_required()
    def get(self, **kwargs):
        usuario_id = kwargs['usuario_id']
        usuario = UsuarioModel.encontrar_por_id(usuario_id)
        resposta = make_response({'message': 'Usuário não encontrado'}, 404)

        if str(usuario_id) == get_jwt_identity():
            if usuario:
                resposta = make_response(usuario_schema.dump(usuario), 200)

        else:
            resposta = retorno_nao_autorizado()

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

        if str(usuario_id) == get_jwt_identity():
            if usuario:
                usuario.ativo == False
                usuario.salvar()
                resposta = make_response(
                    {
                        'message': 'Funcionário desativado, será excluído após um período de 30 dias.'
                    },
                    200,
                )

            else:
                resposta = make_response(
                    {'message': 'Funcionário já está desativada'}, 400
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta
