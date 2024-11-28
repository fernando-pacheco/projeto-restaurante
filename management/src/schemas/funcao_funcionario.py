from marshmallow import Schema, fields
from src.schema import ma


class FuncaoFuncionarioResponseSchema(ma.Schema):
    id = fields.Int()
    funcionario_id = fields.UUID()
    funcao_id = fields.Int()

    class Meta:
        fields = ('id', 'funcionario_id', 'funcao_id')

    _links = ma.Hyperlinks({'self': ma.URLFor('funcao-funcionario')})


class FuncaoFuncionarioResquestGetSchema(Schema):
    id = fields.Int(required=True)


class FuncaoFuncionarioResquestGetByFuncionarioIDSchema(Schema):
    funcionario_id = fields.UUID(required=True)


class FuncaoFuncionarioResquestPostSchema(Schema):
    funcionario_id = fields.UUID(required=True)
    funcao_id = fields.Int(required=True)


class FuncaoFuncionarioResquestPutSchema(Schema):
    funcionario_id = fields.UUID()
    funcao_id = fields.Int()


funcao_funcionario_schema = FuncaoFuncionarioResponseSchema()
