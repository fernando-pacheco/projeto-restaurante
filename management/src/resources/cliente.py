from operator import ge

from flask import make_response
from flask_apispec import doc, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from src.models.cliente import ClienteModel
from src.schemas.cliente import (
    ClienteRequestPostSchema,
    ClienteRequestPutSchema,
    ClienteResponseSchema,
    cliente_schema,
)
from src.utils.decorators import error_decorators, marshal_with
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@doc(tags=['Usuários'])
@marshal_with(ClienteResponseSchema, code=201)
@error_decorators(status_codes=[400])
class ClientesResource(MethodResource, Resource):
    @use_kwargs(ClienteRequestPostSchema, location='json')
    @doc(description='Registrar novo usuário')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao registrar um novo usuário'}, 400
        )

        if ClienteModel.encontrar_por_nome_usuario(kwargs['nome_usuario']):
            resposta = make_response(
                {'message': 'Esse nome de usuário já existe'}, 400
            )

        if ClienteModel.encontrar_por_email(kwargs['email']):
            resposta = make_response(
                {'message': 'Esse email já está cadastrado'}, 400
            )

        if ClienteModel.encontrar_por_cpf(kwargs['cpf']):
            resposta = make_response(
                {'message': 'Esse cpf já está cadastrado.'}, 400
            )

        cliente = ClienteModel(**kwargs)

        if cliente.salvar():
            resposta = make_response(cliente_schema.dump(cliente), 201)

        return resposta


@error_decorators()
@doc(tags=['Usuários'])
@marshal_with(ClienteResponseSchema, code=201)
class ClienteResource(MethodResource, Resource):
    @doc(description='Obter usuário pelo ID')
    @jwt_required()
    def get(self, **kwargs):
        cliente_id = kwargs['id']
        cliente = ClienteModel.encontrar_por_id(cliente_id)
        resposta = make_response({'message': 'Usuário não encontrado'}, 404)

        if str(cliente_id) == get_jwt_identity():
            if cliente:
                resposta = make_response(cliente_schema.dump(cliente), 200)

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @use_kwargs(ClienteRequestPutSchema, location='json')
    @doc(description='Atualizar usuário salvo')
    @jwt_required()
    def put(self, **kwargs):
        cliente_id = kwargs['id']
        cliente = ClienteModel.encontrar_por_id(cliente_id)

        if str(cliente_id) == get_jwt_identity():
            if cliente:
                cliente, resposta = atualizar_objeto(kwargs, cliente)

                if cliente.salvar():
                    resposta = make_response(cliente_schema.dump(cliente), 200)

            else:
                resposta = make_response(
                    {'message': 'ID de usuário não existente'}, 400
                )
        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @doc(description='Excluir usuário por ID')
    @jwt_required()
    def delete(self, **kwargs):
        cliente_id = kwargs['id']
        cliente = ClienteModel.encontrar_por_id(cliente_id)
        resposta = make_response({'message': 'Usuário não encontrado'}, 404)

        if str(cliente_id) == get_jwt_identity():
            if cliente:
                cliente.ativo == False
                cliente.salvar()
                resposta = make_response(
                    {
                        'message': 'Funcionário desativado, será excluído após um período de 30 dias.'
                    },
                    200,
                )

            else:
                resposta = make_response(
                    {'message': 'Funcionário já está desativada'}, 400
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta
