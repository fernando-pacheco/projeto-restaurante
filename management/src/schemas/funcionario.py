from marshmallow import Schema, fields
from src.schema import ma


class FuncionarioResponseSchema(ma.Schema):
    id = fields.UUID()
    nome = fields.Str()
    sobrenome = fields.Str()
    cpf = fields.Str()
    email = fields.Str()
    nome_usuario = fields.Str()
    empresa_id = fields.Str()
    data_criacao = fields.DateTime()
    data_atualizacao = fields.DateTime()
    ativo = fields.Bool()

    class Meta:
        fields = (
            'id',
            'nome',
            'sobrenome',
            'cpf',
            'email',
            'nome_usuario',
            'empresa_id',
            'data_criacao',
            'data_atualizacao',
            'ativo',
        )

    _links = ma.Hyperlinks({'self': ma.URLFor('empresa')})


class FuncionarioRequestGetSchema(Schema):
    id = fields.UUID(required=True)


class FuncionarioRequestPostSchema(Schema):
    nome = fields.Str(required=True)
    sobrenome = fields.Str()
    cpf = fields.Str()
    email = fields.Str(required=True)
    nome_usuario = fields.Str(required=True)
    senha = fields.Str(required=True)
    empresa_id = fields.UUID(required=True)


class FuncionarioRequestPutSchema(Schema):
    nome = fields.Str()
    sobrenome = fields.Str()
    cpf = fields.Str()
    email = fields.Str()
    nome_usuario = fields.Str()
    ativo = fields.Bool()
    senha = fields.Str()


funcionario_schema = FuncionarioResponseSchema()
