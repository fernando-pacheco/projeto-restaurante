import json
from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import fields
from flask_restful import Resource
from src.models.endereco import EnderecoModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.schemas.endereco import (
    EnderecoResponseSchema,
    EnderecoRequestGetSchema,
    EnderecoRequestPostSchema,
    EnderecoRequestPutSchema,
    endereco_schema,
)


@doc(description='Endereco Registro API', tags=['Endereços'])
class EnderecoRegisterResource(MethodResource, Resource):
    @marshal_with(EnderecoResponseSchema, code=201)
    @use_kwargs(EnderecoRequestPostSchema, location='json')
    @doc(description='Cadastrar novo endereço')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao cadastrar um novo endereço.'}, 400
        )

        endereco = EnderecoModel(**kwargs)

        if endereco.salvar():
            resposta = make_response(endereco_schema.dump(endereco), 201)

        return resposta

    def get():
        pass

    def put():
        pass

    def delete():
        pass


@doc(description='Funcao Listagem API', tags=['Endereços'])
class EnderecoListResource(MethodResource, Resource):
    @use_kwargs()
    @marshal_with(EnderecoResponseSchema, code=201)
    @doc(description='Obter lista de endereços por usuário')
    def get(self, **kwargs):
        resposta = make_response({'message': 'Funções não encontradas'}, 400)
        enderecos_retorno = []
        enderecos = EnderecoModel.listar_enderecos_por_entidade()

        if enderecos:
            for endereco in enderecos:
                enderecos_retorno.append(endereco_schema.dump(endereco))

            retorno = {'enderecos': enderecos_retorno}

            resposta = make_response(json.dumps(retorno, indent=4), 201)

        return resposta
