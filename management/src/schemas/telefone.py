from src.schema import ma
from marshmallow import Schema, fields


class TelefoneResponseSchema(ma.Schema):
    id = fields.Int()
    numero = fields.Str()
    principal = fields.Bool()

    class Meta:
        fields = ('id', 'numero', 'principal')

    _links = ma.Hyperlinks({'self': ma.URLFor('telefone')})


class TelefoneRequestGetSchema(Schema):
    id = fields.Int(required=True)


class TelefoneRequestGetNumeroSchema(Schema):
    numero = fields.Str(required=True)


class TelefoneRequestPostSchema(Schema):
    numero = fields.Str(required=True)
    principal = fields.Bool()
    empresa_id = fields.UUID()
    usuario_id = fields.UUID()
    funcionario_id = fields.UUID()


class TelefoneRequestPutSchema(Schema):
    numero = fields.Str()
    principal = fields.Bool()
    empresa_id = fields.UUID()
    usuario_id = fields.UUID()
    funcionario_id = fields.UUID()


telefone_schema = TelefoneResponseSchema()
