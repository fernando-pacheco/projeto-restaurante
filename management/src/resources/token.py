from datetime import datetime, timezone

from flask import Response, make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_login import login_user, logout_user
from flask_restful import Resource
from marshmallow import fields
from src.models.funcionario import FuncionarioModel
from src.models.token import TokenBlocklistModel
from src.models.usuario import UsuarioModel
from src.schemas.message import (
    MessageErro400,
    MessageErro401,
    MessageErro403,
    MessageErro404,
    MessageTokenRevoked,
)
from src.schemas.token import (
    AccessRefreshTokenRequestSchema,
    AccessRefreshTokenUidResponseSchema,
    AccessTokenResponseSchema,
)


@doc(tags=['Auth'])
@marshal_with(MessageErro400, code=400)
@marshal_with(MessageErro401, code=401)
@marshal_with(MessageErro403, code=403)
@marshal_with(MessageErro404, code=404)
@marshal_with(AccessRefreshTokenUidResponseSchema, code=200)
class TokenUsuarioResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(description='Login e gerador de novo acesso de cliente')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro na autenticação, credenciais inválidas.'},
            401,
        )
        nome_usuario = kwargs['nome_usuario']
        senha = kwargs['senha']
        usuario = UsuarioModel.encontrar_por_nome_usuario(nome_usuario)
        if usuario and usuario.verificar_senha(senha):
            login_user(usuario)
            token_acesso = create_access_token(identity=usuario.id)
            refresh_token = create_refresh_token(usuario.id)
            resposta = make_response(
                {
                    'access_token': token_acesso,
                    'refresh_token': refresh_token,
                    'usuario_id': usuario.id,
                },
                201,
            )

        return resposta


@doc(tags=['Auth'])
@marshal_with(AccessRefreshTokenUidResponseSchema, code=201)
@marshal_with(MessageErro400, code=400)
@marshal_with(MessageErro401, code=401)
@marshal_with(MessageErro403, code=403)
@marshal_with(MessageErro404, code=404)
class TokenFuncionarioResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(description='Login e gerador de novo acesso de funcionário')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro na autenticação, credenciais inválidas.'},
            401,
        )

        nome_usuario = kwargs['nome_usuario']
        senha = kwargs['senha']
        funcionario = FuncionarioModel.encontrar_por_nome_usuario(nome_usuario)

        if funcionario and funcionario.verificar_senha(senha):
            login_user(funcionario)
            token_acesso = create_access_token(identity=funcionario.id)
            refresh_token = create_refresh_token(funcionario.id)
            resposta = make_response(
                {
                    'access_token': token_acesso,
                    'refresh_token': refresh_token,
                    'funcionario_id': funcionario.id,
                },
                201,
            )

        return resposta


@doc(tags=['Auth'])
@marshal_with(AccessRefreshTokenUidResponseSchema, code=200)
class TokenRefresherResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(
        description='Atualiza um token de acesso usando o token de atualização'
    )
    @jwt_required(refresh=True)
    def post(self):
        jwt_usuario_atual = get_jwt_identity()
        novo_token = create_access_token(
            identity=jwt_usuario_atual, fresh=False
        )
        return make_response({'token_acesso': novo_token}, 201)


@doc(tags=['Auth'])
@marshal_with(MessageErro400, code=400)
@marshal_with(MessageTokenRevoked, code=200)
class TokenRevokeResource(MethodResource, Resource):
    @doc(description='Revogar token de acesso atual')
    @jwt_required()
    def delete(self):
        resposta = make_response({'message': 'Erro ao excluir o token.'}, 400)

        jti = get_jwt()['jti']
        logout_user()
        agora = datetime.now(timezone.utc)

        if TokenBlocklistModel(jti=jti, data_criacao=agora).salvar():
            resposta = make_response(
                {'message': 'Token de acesso revogado ou expirado'}, 200
            )

        return resposta
