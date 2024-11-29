from marshmallow import Schema, fields
from src.schemas.endereco import EnderecoResponseSchema
from src.schemas.telefone import TelefoneResponseSchema


class EmpresaSchema(Schema):
    id = fields.UUID()
    razao_social = fields.Str()
    cnpj = fields.Str()
    status = fields.Bool()


class FuncionarioInfoSchema(Schema):
    id = fields.UUID()
    nome = fields.Str()
    sobrenome = fields.Str()
    cpf = fields.Str()
    email = fields.Str()
    nome_usuario = fields.Str()
    ativo = fields.Bool()
    empresa = fields.Nested(EmpresaSchema)
    funcoes = fields.Dict()
    telefones = fields.List(fields.Nested(TelefoneResponseSchema))


class ClienteInfoSchema(Schema):
    id = fields.UUID()
    nome_usuario = fields.Str()
    nome = fields.Str()
    sobrenome = fields.Str()
    email = fields.Str()
    cpf = fields.Str()
    ativo = fields.Bool()
    telefones = fields.List(fields.Nested(TelefoneResponseSchema))
    enderecos = fields.List(fields.Nested(EnderecoResponseSchema))


funcionario_schema = FuncionarioInfoSchema()
cliente_shcema = ClienteInfoSchema()
empresa_schema = EmpresaSchema()
