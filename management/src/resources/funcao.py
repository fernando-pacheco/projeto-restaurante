from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource

from src.models.funcao import FuncaoModel
from src.schemas.funcao import (
    FuncaoRequestGetSchema,
    FuncaoResponseSchema,
    funcao_schema,
)


@doc(description='Funcao API', tags=['Função'])
class FuncaoResource(MethodResource, Resource):
    @marshal_with(FuncaoResponseSchema, code=201)
    @use_kwargs(FuncaoRequestGetSchema, location='query')
    @doc(description='Obter função')
    def get(self, **kwargs):
        resposta = make_response({'message': 'Função não encontrada'}, 400)

        funcao = FuncaoModel.encontrar_por_funcao(kwargs['funcao'])

        if funcao:
            resposta = make_response(funcao_schema.dump(funcao), 201)

        return resposta
