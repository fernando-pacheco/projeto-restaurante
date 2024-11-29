from marshmallow import Schema, fields


class AccessRefreshTokenUidResponseSchema(Schema):
    token_acesso = fields.Str()
    refresh_token = fields.Str()
    usuario_id = fields.UUID()


class AccessTokenResponseSchema(Schema):
    token_acesso = fields.Str()


class AccessRefreshTokenRequestSchema(Schema):
    nome_usuario = fields.Str(
        required=True, example='user1', help='Invalid login or password'
    )
    senha = fields.Str(
        required=True, example='pwd1', help='Invalid login or password'
    )
