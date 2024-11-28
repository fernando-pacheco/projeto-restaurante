from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow import fields
from src.models.funcionario import FuncionarioModel
from src.schemas.funcionario import (
    FuncionarioRequestGetSchema,
    FuncionarioRequestPostSchema,
    FuncionarioRequestPutSchema,
    FuncionarioResponseSchema,
    funcionario_schema,
)
from src.schemas.message import MessageSchema
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@doc(description='Funcionário Registro API', tags=['Funcionários'])
class FuncionarioRegisterResource(MethodResource, Resource):
    @marshal_with(FuncionarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(FuncionarioRequestPostSchema, location='json')
    @doc(description='Registrar novo funcionário')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao cadastrar um novo funcionário.'}, 400
        )

        # TODO - Verificação para pessoa que realizar registro
        # Só poderá cadastrar funcionário permissão de Aministrador ou Principal da funcionario

        if FuncionarioModel.encontrar_por_nome_usuario(kwargs['nome_usuario']):
            resposta = make_response(
                {
                    'message': 'Esse nome de usuário já existe para um funcionário.'
                },
                400,
            )

        if FuncionarioModel.encontrar_por_email(kwargs['email']):
            resposta = make_response(
                {'message': 'Esse email já está cadastrado.'}, 400
            )

        if FuncionarioModel.encontrar_por_cpf(kwargs['cpf']):
            resposta = make_response(
                {'message': 'Esse cpf já está cadastrado.'}, 400
            )

        funcionario = FuncionarioModel(**kwargs)

        if funcionario.salvar():
            resposta = make_response(funcionario_schema.dump(funcionario), 200)

        return resposta

    @use_kwargs(FuncionarioRequestGetSchema, location='query')
    @marshal_with(FuncionarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @doc(description='Obter informações de um funcionário')
    @jwt_required()
    def get(self, **kwargs):
        funcionario_id = kwargs['id']
        funcionario = FuncionarioModel.encontrar_por_id(funcionario_id)
        empresa_funcionario_requisitante = (
            FuncionarioModel.encontrar_empresa_id_por_funcionario_id(
                get_jwt_identity()
            )
        )

        if funcionario.empresa_id == empresa_funcionario_requisitante:
            if funcionario:
                resposta = make_response(
                    funcionario_schema.dump(funcionario), 200
                )

            else:
                resposta = make_response(
                    {'message': 'Funcionário não encontrado.'}, 404
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @use_kwargs(FuncionarioRequestGetSchema, location='query')
    @use_kwargs(FuncionarioRequestPutSchema, location='json')
    @marshal_with(FuncionarioResponseSchema, code=201)
    @doc(description='Atualizar funcionario existente salvo')
    @jwt_required()
    def put(self, **kwargs):
        funcionario_id = kwargs['id']
        funcionario = FuncionarioModel.encontrar_por_id(funcionario_id)

        if str(funcionario_id) == get_jwt_identity():
            funcionario, resposta = atualizar_objeto(kwargs, funcionario)

            if funcionario.salvar():
                resposta = make_response(
                    funcionario_schema.dump(funcionario), 201
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @marshal_with(FuncionarioResponseSchema, code=201)
    @marshal_with(MessageSchema, code=400)
    @use_kwargs(FuncionarioRequestGetSchema, location='query')
    @doc(description='Desativar cadastro de um funcionário')
    @jwt_required()
    def delete(self, **kwargs):
        resposta = make_response(
            {'message': 'Funcionário não encontrado.'}, 400
        )

        funcionario_id = kwargs['id']
        funcionario = FuncionarioModel.encontrar_por_id(funcionario_id)

        if funcionario.ativo:
            funcionario.ativo = False
            funcionario.salvar()
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

        return resposta
