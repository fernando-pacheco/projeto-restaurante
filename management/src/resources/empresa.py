from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import fields
from src.models.empresa import EmpresaModel
from src.models.funcao_funcionario import FuncaoFuncionarioModel
from src.schemas.empresa import (
    EmpresaRequestGetSchema,
    EmpresaRequestPostSchema,
    EmpresaResponseSchema,
    EmpresaRequestPutSchema,
    empresa_schema,
)


@doc(description='Empresa Registro API', tags=['Empresa'])
class EmpresaRegisterResource(MethodResource, Resource):
    @marshal_with(EmpresaResponseSchema, code=201)
    @use_kwargs(EmpresaRequestPostSchema, location='json')
    @doc(description='Registrar nova empresa')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao registrar uma nova empresa.'}, 400
        )

        if EmpresaModel.encontrar_por_cnpj(kwargs['cnpj']):
            resposta = make_response({'message': 'Essa empresa já cadastrada.'}, 400)

        empresa = EmpresaModel(**kwargs)

        if empresa.salvar():
            resposta = make_response(empresa_schema.dump(empresa), 201)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(EmpresaResponseSchema, code=201)
    @use_kwargs(EmpresaRequestGetSchema, location='query')
    @use_kwargs(EmpresaRequestPutSchema, location='json')
    @doc(description='Atualizar empresa existente salvo')
    @jwt_required()
    def put(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro ao atualizar empresa.'}, 400
        )

        empresa = EmpresaModel.encontrar_por_id(kwargs['id'])

        # TODO - implementar verificação por função do colaborador <sc[401]>
        # Apenas funções de administrador e principal podem atualizar dados da empresa

        # usuario = UsuarioModel.encontrar_por_id(kwargs['usuario_id'])
        # Deve ser um usuário da empresa e ter funções de edição dos dados da empresa

        for campo, valor in kwargs.items():
            if (
                campo not in ['usuario_id', 'Authorization']
                and valor is not None
            ):
                if hasattr(empresa, campo):
                    if isinstance(getattr(empresa, campo), bool):
                        valor = str(valor).lower() == 'true'

                    setattr(empresa, campo, valor)

                else:
                    resposta = make_response(
                        {'message': f'O campo {campo} não é válido.'}, 400
                    )

        if empresa.salvar():
            resposta = make_response(empresa_schema.dump(empresa), 201)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(EmpresaResponseSchema, code=201)
    @use_kwargs(EmpresaRequestGetSchema, location='query')
    @doc(description='Obter informações da empresa.')
    @jwt_required()
    def get(self, **kwargs):
        resposta = make_response({'message': 'Empresa não encontrada.'}, 400)

        # TODO - Implementar verificação para colaborador
        # Apenas colaboradores podem acessar informações da empresa

        empresa = EmpresaModel.encontrar_por_id(kwargs['id'])

        if empresa:
            resposta = make_response(empresa_schema.dump(empresa), 200)

        return resposta

    @use_kwargs(
        {
            'Authorization': fields.Str(
                required=True, description='Bearer [access_token]'
            )
        },
        location='headers',
    )
    @marshal_with(EmpresaResponseSchema, code=201)
    @use_kwargs(EmpresaRequestGetSchema, location='query')
    @doc(description='Desativar uma empresa')
    @jwt_required()
    def delete(self, **kwargs):
        resposta = make_response({'message': 'Empresa não encontrada.'}, 400)

        empresa = EmpresaModel.encontrar_por_id(kwargs['id'])

        if empresa.status:
            print(empresa.status)
            empresa.status = False
            print(empresa.status)
            empresa.salvar()
            resposta = make_response(
                {
                    'message': 'Empresa desativada, será excluída após um período de 30 dias.'
                },
                200,
            )
        else:
            resposta = make_response(
                {'message': 'Empresa já está desativada.'}, 400
            )

        return resposta
