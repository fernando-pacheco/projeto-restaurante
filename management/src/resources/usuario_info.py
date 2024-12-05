from flask import make_response
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from src.models.cliente import ClienteModel
from src.models.empresa import EmpresaModel
from src.models.endereco import EnderecoModel
from src.models.funcao_funcionario import FuncaoFuncionarioModel
from src.models.funcionario import FuncionarioModel
from src.models.telefone import TelefoneModel
from src.schemas.endereco import endereco_schema
from src.schemas.funcao_funcionario import funcao_funcionario_schema
from src.schemas.usuario import (
    FuncionarioInfoSchema,
    cliente_schema,
    empresa_schema,
    funcionario_schema,
    telefone_schema,
)


@doc(tags=['Usuários'])
@marshal_with(FuncionarioInfoSchema, 200)
class UsuarioInfoResource(MethodResource, Resource):
    @jwt_required()
    def get(self):
        usuario_id = get_jwt_identity()
        cliente = ClienteModel.encontrar_por_id(usuario_id)

        if cliente:
            cliente_data = cliente_schema.dump(cliente)
            cliente_data['telefones'] = self.listar_objetos_model_por_schema(
                TelefoneModel.listar_telefones_por_entidade(
                    usuario_id, 'cliente'
                ),
                telefone_schema,
            )
            cliente_data['enderecos'] = self.listar_objetos_model_por_schema(
                EnderecoModel.listar_enderecos_por_entidade(
                    usuario_id, 'cliente'
                ),
                endereco_schema,
            )

            return make_response(cliente_data, 200)

        else:
            funcionario = FuncionarioModel.encontrar_por_id(usuario_id)
            funcionario_data = funcionario_schema.dump(funcionario)
            funcionario_data[
                'telefones'
            ] = self.listar_objetos_model_por_schema(
                TelefoneModel.listar_telefones_por_entidade(
                    usuario_id, 'funcionario'
                ),
                telefone_schema,
            )
            funcao_funcionario = (
                FuncaoFuncionarioModel.encontrar_por_funcionario_id(usuario_id)
            )
            funcionario_data['funcoes'] = self.listar_objetos_model_por_schema(
                funcao_funcionario,
                funcao_funcionario_schema,
            )
            funcionario_data['empresa'] = empresa_schema.dump(
                EmpresaModel.encontrar_por_id(funcionario.empresa_id)
            )

            return make_response(funcionario_data, 200)

    def listar_objetos_model_por_schema(self, lista_model, schema):
        return [schema.dump(objeto) for objeto in lista_model]
