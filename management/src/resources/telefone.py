from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import fields
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.utils.funcoes_auxiliares import (
    retorno_nao_autorizado,
    # obter_portador_id,
    atualizar_objeto,
)
from src.models.telefone import TelefoneModel
from src.schemas.telefone import (
    TelefoneRequestGetSchema,
    TelefoneRequestPostSchema,
    TelefoneRequestPutSchema,
    TelefoneResponseSchema,
    TelefoneRequestGetNumeroSchema,
    telefone_schema,
)


@doc(description='Telefone Registro API', tags=['Telefones'])
class TelefoneRegisterResource(MethodResource, Resource):
    @marshal_with(TelefoneResponseSchema, code=201)
    @use_kwargs(TelefoneRequestPostSchema, location='json')
    @doc(description='Cadastrar novo telefone')
    def post(self, **kwargs):
        resposta = make_response(
            {
                'message': 'Não foi possível cadastrar um novo número de telefone.'
            },
            400,
        )

        if TelefoneModel.encontrar_por_numero(kwargs['numero']):
            resposta = make_response({'message': 'Número já cadastrado.'}, 400)
        else:
            telefone = TelefoneModel(**kwargs)

            if telefone.salvar():
                resposta = make_response(telefone_schema.dump(telefone), 201)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(TelefoneResponseSchema, code=201)
    @use_kwargs(TelefoneRequestGetSchema, location='query')
    @use_kwargs(TelefoneRequestPutSchema, location='json')
    @doc(description='Atualizar um número')
    @jwt_required()
    def put(self, **kwargs):
        resposta = make_response(
            {'message': 'Não foi possível atualizar telefone.'}, 400
        )

        telefone = TelefoneModel.encontrar_por_id(kwargs['id'])
        portador_id = telefone.obter_portador_id()

        if str(portador_id) == get_jwt_identity():
            telefone, resposta = atualizar_objeto(kwargs, telefone)

            if telefone.salvar():
                resposta = make_response(telefone_schema.dump(telefone), 201)

        else:
            resposta = retorno_nao_autorizado()

        return resposta

    @marshal_with(TelefoneResponseSchema, code=201)
    @use_kwargs(TelefoneRequestGetNumeroSchema, location='query')
    @doc(description='Obter informações de contato')
    def get(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao obter informações de contato.'}, 400
        )

        telefone = TelefoneModel.encontrar_por_numero(kwargs['numero'])

        if telefone:
            resposta = make_response(telefone_schema.dump(telefone), 201)

        else:
            resposta = make_response({'message': 'Telefone não encontrado.'})

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @use_kwargs(TelefoneRequestGetSchema, location='query')
    @doc(description='Excluir um número de telefone')
    @jwt_required()
    def delete(self, **kwargs):
        # TODO - Validação para exclusão ou edição para funcionário com permissões

        resposta = make_response({'message': 'Este telefone não existe.'}, 400)

        telefone = TelefoneModel.encontrar_por_id(kwargs['id'])
        portador_id = telefone.obter_portador_id()

        if str(portador_id) == get_jwt_identity():
            if telefone.excluir():
                resposta = make_response(
                    {'message': 'Telefone excluído com sucesso.'}, 201
                )

        else:
            resposta = retorno_nao_autorizado()

        return resposta
