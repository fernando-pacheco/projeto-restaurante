from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow import fields

from management.src.schemas.funcionario import FuncionarioRequestPostSchema, FuncionarioResponseSchema
from src.utils.funcoes_auxiliares import (
    retorno_nao_autorizado,
    atualizar_objeto,
)
from schemas.funcao_funcionario import (
    FuncaoFuncionarioResponseSchema,
    FuncaoFuncionarioResquestGetSchema,
    FuncaoFuncionarioResquestPostSchema,
    FuncaoFuncionarioResquestPutSchema,
    funcao_funcionario_schema,
)


@doc(
    description='Função Funcionário Registro API', tags=['Função Funcionário']
)
class FuncaoFuncionarioRegisterResource(MethodResource, Resource):
    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(FuncionarioResponseSchema, code=201)
    @use_kwargs(FuncionarioRequestPostSchema, location='json')
    @doc(description='Registrar permissão para funcionário')
    @jwt_required()
    def post(self, **kwargs):
        pass
    
    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @use_kwargs(FuncaoFuncionarioResquestGetSchema, location='query')
    @marshal_with(FuncionarioResponseSchema, code=201)
    @doc(description='Obter informações de permissão do funcionário')
    @jwt_required()
    def get(self, **kwargs):
        pass
    
    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @use_kwargs(FuncaoFuncionarioResquestGetSchema, location='query')
    @use_kwargs(FuncaoFuncionarioResquestPutSchema, location='json')
    @marshal_with(FuncaoFuncionarioResponseSchema, code=201)
    @doc(description='Atualizar permissões de um funcionário')
    @jwt_required()
    def put(self, **kwargs):
        pass
    
    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @use_kwargs(FuncaoFuncionarioResquestGetSchema, location='query')
    @marshal_with(FuncaoFuncionarioResponseSchema, code=201)
    @doc(description='Excluir uma função de um funcionário')
    @jwt_required()
    def delete(self, **kwargs):
        pass