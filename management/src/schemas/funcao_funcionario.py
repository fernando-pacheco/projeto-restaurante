from marshmallow import Schema, fields
from src.schema import ma


class FuncaoFuncionarioResponseSchema(ma.Schema):
    id = fields.Int()
    funcao_id = fields.Int()
    nome_funcao = fields.Method('obter_nome_funcao')

    def obter_nome_funcao(self, obj):
        return getattr(obj.nome_funcao, 'funcao', None)

    class Meta:
        fields = ('id', 'funcao_id', 'nome_funcao')

    _links = ma.Hyperlinks({'self': ma.URLFor('funcao-funcionario')})


class FuncaoFuncionarioResquestPostSchema(Schema):
    funcionario_id = fields.UUID(required=True)
    funcao_id = fields.Int(required=True)


class FuncaoFuncionarioResquestPutSchema(Schema):
    funcionario_id = fields.UUID()
    funcao_id = fields.Int()


funcao_funcionario_schema = FuncaoFuncionarioResponseSchema()
