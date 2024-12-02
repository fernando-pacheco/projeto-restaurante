from flask_restful import Api
from src.resources.cliente import ClienteResource, ClientesResource
from src.resources.empresa import EmpresaResource, EmpresasResource
from src.resources.endereco import (
    EnderecoResource,
    EnderecosClienteResource,
    EnderecosEmpresaResource,
    EnderecosResource,
)
from src.resources.funcao import FuncaoResource, FuncoesResource
from src.resources.funcao_funcionario import (
    FuncaoFuncionarioIDResource,
    FuncaoFuncionarioResource,
    FuncaoFuncionariosResource,
)
from src.resources.funcionario import FuncionarioResource, FuncionariosResource
from src.resources.health_checker import HealthCheckerResource
from src.resources.telefone import (
    TelefoneResource,
    TelefonesClienteResource,
    TelefonesEmpresaResource,
    TelefonesFuncionarioResource,
    TelefonesResource,
)
from src.resources.token import (
    TokenFuncionarioResource,
    TokenRefresherResource,
    TokenRevokeResource,
    TokenUsuarioResource,
)
from src.resources.usuario_info import UsuarioInfoResource


def config_app_routes(app, docs):
    api = Api(app)

    # Entidade
    ## Usuários
    __setting_route_doc(ClientesResource, '/cliente', api, docs)
    __setting_route_doc(ClienteResource, '/cliente/<string:id>', api, docs)
    ## Funcionários
    __setting_route_doc(FuncionariosResource, '/funcionario', api, docs)
    __setting_route_doc(
        FuncionarioResource, '/funcionario/<string:id>', api, docs
    )
    ## Usuário Info
    __setting_route_doc(UsuarioInfoResource, '/usuario-info', api, docs)
    ## Empresas
    __setting_route_doc(EmpresasResource, '/empresa', api, docs)
    __setting_route_doc(EmpresaResource, '/empresa/<string:id>', api, docs)
    ## Telefones
    __setting_route_doc(TelefonesResource, '/telefone', api, docs)
    __setting_route_doc(TelefoneResource, '/telefone/<int:id>', api, docs)
    __setting_route_doc(
        TelefonesClienteResource, '/cliente/<string:id>/telefones', api, docs
    )
    __setting_route_doc(
        TelefonesEmpresaResource, '/empresa/<string:id>/telefones', api, docs
    )
    __setting_route_doc(
        TelefonesFuncionarioResource, '/funcionario/<string:id>/telefones', api, docs
    )
    ## Endereços
    __setting_route_doc(EnderecosResource, '/endereco', api, docs)
    __setting_route_doc(EnderecoResource, '/endereco/<string:id>', api, docs)
    __setting_route_doc(
        EnderecosEmpresaResource, '/empresa/<string:id>/enderecos', api, docs
    )
    __setting_route_doc(
        EnderecosClienteResource, '/cliente/<string:id>/enderecos', api, docs
    )

    # Token
    __setting_route_doc(TokenUsuarioResource, '/token-cliente', api, docs)
    __setting_route_doc(
        TokenFuncionarioResource, '/token-funcionario', api, docs
    )
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)
    __setting_route_doc(TokenRevokeResource, '/token', api, docs)

    # Health Checker
    __setting_route_doc(HealthCheckerResource, '/health', api, docs)

    # Permissão
    __setting_route_doc(FuncaoResource, '/funcao/<string:funcao>', api, docs)
    __setting_route_doc(FuncoesResource, '/funcao', api, docs)
    __setting_route_doc(
        FuncaoFuncionariosResource, '/funcao-funcionario', api, docs
    )
    __setting_route_doc(
        FuncaoFuncionarioIDResource,
        '/funcionario/<string:id>/funcoes',
        api,
        docs,
    )
    __setting_route_doc(
        FuncaoFuncionarioResource, '/funcao-funcionario/<int:id>', api, docs
    )

    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
