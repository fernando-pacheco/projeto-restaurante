from flask_restful import Api
from src.resources.cliente import ClienteResource, ClientesResource
from src.resources.empresa import EmpresaResource, EmpresasResource
from src.resources.funcao import FuncaoListResource, FuncaoResource
from src.resources.funcao_funcionario import (
    FuncaoFuncionarioIDResource,
    FuncaoFuncionarioResource,
    FuncaoFuncionariosResource,
)
from src.resources.funcionario import FuncionarioResource, FuncionariosResource
from src.resources.health_checker import HealthCheckerResource
from src.resources.telefone import TelefoneResource, TelefonesResource
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
    __setting_route_doc(FuncaoResource, '/funcao', api, docs)
    __setting_route_doc(FuncaoListResource, '/funcao/all', api, docs)
    __setting_route_doc(
        FuncaoFuncionariosResource, '/funcao-funcionario', api, docs
    )
    __setting_route_doc(
        FuncaoFuncionarioIDResource,
        '/funcao-funcionario/<string:funcionario_id>',
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
