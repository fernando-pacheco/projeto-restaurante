from marshmallow import Schema, fields
from src.schema import ma


class EnderecoResponseSchema(ma.Schema):
    id = fields.Str()
    logradouro = fields.Str()
    numero = fields.Int()
    bairro = fields.Str()
    cidade = fields.Str()
    estado = fields.Str()
    cep = fields.Str()
    complemento = fields.Str()
    principal = fields.Bool()

    class Meta:
        fields = (
            'id',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'complemento',
            'principal',
        )

    _links = ma.Hyperlinks({'self': ma.URLFor('endereco')})


class EnderecoRequestGetSchema(Schema):
    id = fields.Str(required=True)


class EnderecoRequestPostSchema(Schema):
    logradouro = fields.Str()
    numero = fields.Int()
    bairro = fields.Str()
    cidade = fields.Str()
    estado = fields.Str()
    cep = fields.Str()
    complemento = fields.Str()
    principal = fields.Bool()


class EnderecoRequestPutSchema(Schema):
    logradouro = fields.Str(required=True)
    numero = fields.Int(required=True)
    bairro = fields.Str(required=True)
    cidade = fields.Str(required=True)
    estado = fields.Str(required=True)
    cep = fields.Str(required=True)
    complemento = fields.Str()
    principal = fields.Bool()


endereco_schema = EnderecoResponseSchema()
