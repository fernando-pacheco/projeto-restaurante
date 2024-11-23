from marshmallow import Schema, fields

from src.schema import ma


class FuncaoResponseSchema(ma.Schema):
    id = fields.Int()
    funcao = fields.Str()
    nivel = fields.Int()

    class Meta:
        fields = ('id', 'funcao', 'nivel')
        ordered = True

    _links = ma.Hyperlinks({'self': ma.URLFor('funcao')})


class FuncaoRequestGetSchema(Schema):
    funcao = fields.Str(required=True, default='principal')


funcao_schema = FuncaoResponseSchema()
