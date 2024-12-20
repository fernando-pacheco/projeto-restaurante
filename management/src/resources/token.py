import re
from datetime import datetime, timezone

from flask import make_response
from flask_apispec import doc, use_kwargs
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
from src.models.cliente import ClienteModel
from src.models.funcionario import FuncionarioModel
from src.models.token import TokenBlocklistModel
from src.schemas.message import MessageTokenRevoked
from src.schemas.token import (
    AccessRefreshTokenRequestSchema,
    AccessRefreshTokenUidResponseSchema,
)
from src.utils.decorators import error_decorators, marshal_with


@doc(tags=['Auth'])
@error_decorators()
@marshal_with(AccessRefreshTokenUidResponseSchema, code=200)
class TokenUsuarioResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(description='Login e gerador de novo acesso de cliente')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro na autenticação, credenciais inválidas.'},
            401,
        )
        credencial = kwargs['credencial']
        senha = kwargs['senha']

        if re.match(r'[^@]+@[^@]+\.[^@]+', credencial):
            cliente = ClienteModel.encontrar_por_email(credencial)
        else:
            cliente = ClienteModel.encontrar_por_nome_usuario(credencial)

        if cliente and cliente.verificar_senha(senha):
            login_user(cliente)
            token_acesso = create_access_token(identity=cliente.id)
            refresh_token = create_refresh_token(cliente.id)
            resposta = make_response(
                {
                    'access_token': token_acesso,
                    'refresh_token': refresh_token,
                    'usuario_id': cliente.id,
                },
                201,
            )

        return resposta


@doc(tags=['Auth'])
@marshal_with(AccessRefreshTokenUidResponseSchema, code=201)
@error_decorators()
class TokenFuncionarioResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(description='Login e gerador de novo acesso de funcionário')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro na autenticação, credenciais inválidas.'},
            401,
        )

        credencial = kwargs['credencial']
        senha = kwargs['senha']

        if re.match(r'[^@]+@[^@]+\.[^@]+', credencial):
            funcionario = FuncionarioModel.encontrar_por_email(credencial)
        else:
            funcionario = FuncionarioModel.encontrar_por_nome_usuario(
                credencial
            )

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
@use_kwargs(AccessRefreshTokenRequestSchema, location='json')
class TokenRefresherResource(MethodResource, Resource):
    @doc(
        description='Atualiza um token de acesso usando o token de atualização'
    )
    @jwt_required()
    def post(self):
        jwt_usuario_atual = get_jwt_identity()
        novo_token = create_access_token(
            identity=jwt_usuario_atual, fresh=False
        )
        return make_response({'token_acesso': novo_token}, 201)


@doc(tags=['Auth'])
@error_decorators(status_codes=[400])
@marshal_with(MessageTokenRevoked, code=200)
class TokenRevokeResource(MethodResource, Resource):
    @jwt_required()
    @doc(description='Revogar token de acesso atual')
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
