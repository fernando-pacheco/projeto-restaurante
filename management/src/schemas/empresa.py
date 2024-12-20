from marshmallow import Schema, fields
from src.schema import ma


class EmpresaResponseSchema(ma.Schema):
    id = fields.UUID()
    nome = fields.Str()
    razao_social = fields.Str()
    cnpj = fields.Str()
    status = fields.Bool()
    data_criacao = fields.DateTime()
    data_atualizacao = fields.DateTime()

    class Meta:
        fields = (
            'id',
            'nome',
            'razao_social',
            'cnpj',
            'status',
            'data_criacao',
            'data_atualizacao',
        )

    _links = ma.Hyperlinks({'self': ma.URLFor('empresa')})


class EmpresaRequestGetSchema(Schema):
    id = fields.UUID(required=True)


class EmpresaRequestPostSchema(Schema):
    nome = fields.Str()
    razao_social = fields.Str(required=True)
    cnpj = fields.Str(required=True)


class EmpresaRequestPutSchema(Schema):
    nome = fields.Str()
    razao_social = fields.Str()
    cnpj = fields.Str()
    status = fields.Bool()


empresa_schema = EmpresaResponseSchema()
