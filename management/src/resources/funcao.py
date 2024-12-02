import json

from flask import make_response
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from flask_restful import Resource
from src.utils.decorators import error_decorators
from src.models.funcao import FuncaoModel
from src.schemas.funcao import (
    FuncaoResponseSchema,
    funcao_schema,
)


@doc(tags=['Funções'])
@marshal_with(FuncaoResponseSchema, code=200)
@error_decorators([404])
class FuncaoResource(MethodResource, Resource):
    @doc(description='Obter função')
    def get(self, **kwargs):
        resposta = make_response({'message': 'Função não encontrada.'}, 404)

        funcao = FuncaoModel.encontrar_por_funcao(kwargs['funcao'])

        if funcao:
            resposta = make_response(funcao_schema.dump(funcao), 200)

        return resposta


@doc(tags=['Funções'])
@marshal_with(FuncaoResponseSchema, code=200)
class FuncoesResource(MethodResource, Resource):
    @marshal_with(FuncaoResponseSchema, code=201)
    @doc(description='Obter lista de funções')
    def get(self):
        resposta = make_response({'message': 'Funções não encontradas.'}, 404)
        funcoes_retorno = []
        funcoes = FuncaoModel.listar_funcoes()

        if funcoes:
            for funcao in funcoes:
                funcoes_retorno.append(funcao_schema.dump(funcao))

            retorno = {'funcoes': funcoes_retorno}

            resposta = make_response(json.dumps(retorno, indent=4), 200)

        return resposta
