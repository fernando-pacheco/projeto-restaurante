import json

from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from src.models.cliente import ClienteModel
from src.models.endereco import EnderecoModel
from src.models.funcionario import FuncionarioModel
from src.schemas.endereco import (
    EnderecoRequestPostSchema,
    EnderecoRequestPutSchema,
    EnderecoResponseSchema,
    endereco_schema,
)
from src.utils.decorators import error_decorators
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@doc(tags=['Endereços'])
@marshal_with(EnderecoResponseSchema, code=201)
@error_decorators([400])
class EnderecosResource(MethodResource, Resource):
    @use_kwargs(EnderecoRequestPostSchema, location='json')
    @doc(description='Cadastrar novo endereço')
    @jwt_required()
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao cadastrar um novo endereço.'}, 400
        )
        usuario_id = get_jwt_identity()
        cliente = ClienteModel.encontrar_por_id(usuario_id)

        if cliente:
            kwargs['cliente_id'] = usuario_id

        else:
            empresa_id = (
                FuncionarioModel.encontrar_empresa_id_por_funcionario_id(
                    usuario_id
                )
            )
            kwargs['empresa_id'] = empresa_id

        endereco = EnderecoModel(**kwargs)

        if endereco.salvar():
            resposta = make_response(endereco_schema.dump(endereco), 201)

        return resposta


@doc(tags=['Endereços'])
@error_decorators([400, 403, 404])
@marshal_with(EnderecoResponseSchema, code=200)
class EnderecoResource(MethodResource, Resource):
    @doc(description='Obter informações de endereço')
    def get(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao encontrar endereço.'}, 404
        )
        endereco = EnderecoModel.encontrar_por_id(kwargs['id'])

        if endereco:
            resposta = make_response(endereco_schema.dump(endereco), 200)

        return resposta

    @jwt_required()
    @doc(description='Atualizar um endereço')
    @use_kwargs(EnderecoRequestPutSchema, location='json')
    def put(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao atualizar um endereço.'}, 400
        )
        endereco = EnderecoModel.encontrar_por_id(kwargs['id'])
        portador_id = endereco.obter_portador_id()

        if str(portador_id) == get_jwt_identity():
            endereco, resposta = atualizar_objeto(kwargs, endereco)

            if endereco.salvar():
                resposta = make_response(endereco_schema.dump(endereco), 201)

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @jwt_required()
    @doc(description='Excluir um endereço')
    def delete(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao excluir um endereço.'}, 400
        )
        endereco = EnderecoModel.encontrar_por_id(kwargs['id'])
        portador_id = endereco.obter_portador_id()

        if str(portador_id) == get_jwt_identity():
            if endereco.excluir():
                resposta = make_response(
                    {'message': 'Endereço excluído com sucesso.'}, 200
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta


@doc(tags=['Endereços'])
@marshal_with(EnderecoResponseSchema, code=200)
class EnderecosClienteResource(MethodResource, Resource):
    @doc(description='Obter lista de endereços por cliente')
    def get(self, **kwargs):
        resposta = make_response(
            {'message': 'Endereços não encontrados.'}, 404
        )
        enderecos_retorno = []
        enderecos = EnderecoModel.listar_enderecos_por_entidade(
            kwargs['id'], 'cliente'
        )

        if enderecos:
            for endereco in enderecos:
                enderecos_retorno.append(endereco_schema.dump(endereco))

            retorno = {'enderecos': enderecos_retorno}

            resposta = make_response(json.dumps(retorno, indent=4), 200)

        return resposta


@doc(tags=['Endereços'])
@marshal_with(EnderecoResponseSchema, code=200)
class EnderecosEmpresaResource(MethodResource, Resource):
    @doc(description='Obter lista de endereços por empresa')
    def get(self, **kwargs):
        resposta = make_response({'message': 'Endereços não encontrados'}, 404)
        enderecos_retorno = []
        enderecos = EnderecoModel.listar_enderecos_por_entidade(
            kwargs['id'], 'empresa'
        )

        if enderecos:
            for endereco in enderecos:
                enderecos_retorno.append(endereco_schema.dump(endereco))

            retorno = {'enderecos': enderecos_retorno}

            resposta = make_response(json.dumps(retorno, indent=4), 201)

        return resposta
