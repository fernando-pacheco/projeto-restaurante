import json

from flask import make_response
from flask_apispec import doc, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from src.models.funcao_funcionario import FuncaoFuncionarioModel
from src.schemas.funcao_funcionario import (
    FuncaoFuncionarioResponseSchema,
    FuncaoFuncionarioResquestPostSchema,
    FuncaoFuncionarioResquestPutSchema,
    funcao_funcionario_schema,
)
from src.utils.decorators import error_decorators, marshal_with
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@doc(tags=['Função Funcionário'])
@marshal_with(FuncaoFuncionarioResponseSchema, code=201)
@error_decorators([400, 403])
class FuncaoFuncionariosResource(MethodResource, Resource):
    @use_kwargs(FuncaoFuncionarioResquestPostSchema, location='json')
    @doc(description='Registrar permissão para funcionário')
    @jwt_required()
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao definir função ao colaborador.'}, 400
        )

        funcao_funcionario = FuncaoFuncionarioModel(**kwargs)

        if funcao_funcionario.salvar():
            resposta = make_response(
                funcao_funcionario_schema.dump(funcao_funcionario), 200
            )

        return resposta


@doc(tags=['Função Funcionário'])
@marshal_with(FuncaoFuncionarioResponseSchema, code=201)
@error_decorators([400, 403, 404])
class FuncaoFuncionarioIDResource(MethodResource, Resource):
    @doc(description='Obter informações de permissão do funcionário')
    @jwt_required()
    def get(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao tentar obter informações do funcionário.'},
            400,
        )
        funcoes_retorno = []
        funcionario_id = kwargs['funcionario_id']
        funcoes_funcionario = (
            FuncaoFuncionarioModel.encontrar_por_funcionario_id(funcionario_id)
        )

        if funcoes_funcionario:
            for funcao_funcionario in funcoes_funcionario:
                funcoes_retorno.append(
                    funcao_funcionario_schema.dump(funcao_funcionario)
                )

            retorno = {
                'funcionario_id': str(funcionario_id),
                'funcoes': funcoes_retorno,
            }

            resposta = make_response(
                json.dumps(retorno, indent=4),
                200,
            )

        return resposta


@doc(tags=['Função Funcionário'])
@marshal_with(FuncaoFuncionarioResponseSchema, code=201)
@error_decorators([400, 403, 404])
class FuncaoFuncionarioResource(MethodResource, Resource):
    @use_kwargs(FuncaoFuncionarioResquestPutSchema, location='json')
    @doc(description='Atualizar permissões de um funcionário')
    @jwt_required()
    def put(self, **kwargs):
        funcao_funcionario_id = kwargs['id']
        funcao_funcionario = FuncaoFuncionarioModel.encontrar_por_id(
            funcao_funcionario_id
        )

        if str(funcao_funcionario.funcionario_id) == get_jwt_identity():
            funcao_funcionario, resposta = atualizar_objeto(
                kwargs, funcao_funcionario
            )

            if funcao_funcionario.salvar():
                resposta = make_response(
                    funcao_funcionario_schema.dump(funcao_funcionario), 201
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @doc(description='Excluir uma função de um funcionário')
    @jwt_required()
    def delete(self, **kwargs):
        resposta = make_response(
            {'messagem': 'Não foi possível encontrar a função.'}, 400
        )

        funcao_funcionario_id = FuncaoFuncionarioModel.encontrar_por_id(
            kwargs['id']
        )

        if funcao_funcionario_id.excluir():
            resposta = make_response(
                {'message': 'Função foi revogada com sucesso.'}, 200
            )

        return resposta
