from datetime import datetime, timezone

from flask import make_response
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
from src.models.token import TokenBlocklistModel
from src.models.usuario import UsuarioModel
from src.schemas.token import (
    AccessRefreshTokenRequestSchema,
    AccessRefreshTokenUidResponseSchema,
    AccessTokenResponseSchema,
    MessageSchema,
)


@doc(description='Token API', tags=['Token'])
class TokenResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @marshal_with(AccessRefreshTokenUidResponseSchema, code=201)
    @marshal_with(MessageSchema, code=401)
    @doc(description='Login e gerador de novo acesso')
    def post(self, **kwargs):
        nome_usuario = kwargs['nome_usuario']
        senha = kwargs['senha']
        usuario = UsuarioModel.query.filter_by(
            nome_usuario=nome_usuario
        ).first()
        if not usuario or not usuario.verificar_senha(senha):
            return make_response(
                {'message': 'Nome de usuário ou senha inválido'}, 401
            )

        login_user(usuario)
        token_acesso = create_access_token(identity=usuario.id)
        refresh_token = create_refresh_token(usuario.id)
        return make_response(
            {
                'access_token': token_acesso,
                'refresh_token': refresh_token,
                'uid': usuario.id,
            },
            201,
        )

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(MessageSchema, code=201)
    @doc(description='Revogar token de acesso atual')
    @jwt_required()
    def delete(self, **kwargs):
        jti = get_jwt()['jti']
        logout_user()
        agora = datetime.now(timezone.utc)
        TokenBlocklistModel(jti=jti, data_criacao=agora).salvar()
        return make_response(
            {'message': 'Token de acesso revogado ou expirado'}, 201
        )


@doc(description='Token refresher API', tags=['Token'])
class TokenRefresherResource(MethodResource, Resource):
    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [refresh_token]'
            )
        },
        location='headers',
    )
    @marshal_with(AccessTokenResponseSchema, code=201)
    @doc(description='Refresh current access token')
    @jwt_required(refresh=True)
    def post(self, **kwargs):
        jwt_usuario_atual = get_jwt_identity()
        novo_token = create_access_token(
            identity=jwt_usuario_atual, fresh=False
        )
        return make_response({'access_token': novo_token}, 201)
