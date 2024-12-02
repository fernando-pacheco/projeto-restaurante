from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from src.models.cliente import ClienteModel
from src.models.funcionario import FuncionarioModel
from src.models.telefone import TelefoneModel
from src.schemas.telefone import (
    TelefoneRequestPostSchema,
    TelefoneRequestPutSchema,
    TelefoneResponseSchema,
    telefone_schema,
)
from src.utils.decorators import error_decorators
from src.utils.funcoes_auxiliares import (
    atualizar_objeto,
    retorno_nao_autorizado,
)


@marshal_with(TelefoneResponseSchema, code=201)
@error_decorators([400, 401, 403])
@doc(tags=['Telefones'])
class TelefonesResource(MethodResource, Resource):
    @use_kwargs(TelefoneRequestPostSchema, location='json')
    @doc(description='Cadastrar novo telefone')
    @jwt_required()
    def post(self, **kwargs):
        #! TODO - Verificar a implementação do telefone
        resposta = make_response(
            {
                'message': 'Não foi possível cadastrar um novo número de telefone.'
            },
            400,
        )

        usuario_id = get_jwt_identity()
        cliente = ClienteModel.encontrar_por_id(usuario_id)

        if TelefoneModel.encontrar_por_numero(kwargs['numero']):
            resposta = make_response({'message': 'Número já cadastrado.'}, 400)
        else:
            if cliente:
                kwargs['cliente_id'] = usuario_id

            else:
                empresa_id = (
                    FuncionarioModel.encontrar_empresa_id_por_funcionario_id(
                        usuario_id
                    )
                )
                kwargs['empresa_id'] = empresa_id

            telefone = TelefoneModel(**kwargs)

            if telefone.salvar():
                resposta = make_response(telefone_schema.dump(telefone), 201)

        return resposta


@marshal_with(TelefoneResponseSchema, code=201)
@error_decorators([400, 404, 403])
@doc(tags=['Telefones'])
class TelefoneResource(MethodResource, Resource):
    @use_kwargs(TelefoneRequestPutSchema, location='json')
    @doc(description='Atualizar um número')
    @jwt_required()
    def put(self, **kwargs):
        resposta = make_response(
            {'message': 'Não foi possível atualizar telefone.'}, 400
        )

        telefone = TelefoneModel.encontrar_por_id(kwargs['id'])
        portador_id = telefone.obter_portador_id()

        if 'numero' in kwargs:
            if TelefoneModel.encontrar_por_numero(kwargs['numero']):
                resposta = make_response(
                    {'message': 'Número já cadastrado.'}, 400
                )
            else:
                if str(portador_id) == get_jwt_identity():
                    telefone, resposta = atualizar_objeto(kwargs, telefone)

                    if telefone.salvar():
                        resposta = make_response(
                            telefone_schema.dump(telefone), 201
                        )

                else:
                    resposta = retorno_nao_autorizado()

        return resposta

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
