from flask_restful import Api
from src.resources.empresa import EmpresaRegisterResource
from src.resources.funcao import FuncaoListResource, FuncaoResource
from src.resources.funcao_funcionario import FuncaoFuncionarioRegisterResource
from src.resources.funcionario import FuncionarioRegisterResource
from src.resources.health_checker import HealthCheckerResource
from src.resources.telefone import TelefoneRegisterResource
from src.resources.token import (
    TokenFuncionarioResource,
    TokenRefresherResource,
    TokenRevokeResource,
    TokenUsuarioResource,
)
from src.resources.cliente import (
    ClienteRegisterResource,
    ClienteResource,
)
from src.resources.usuario_info import UsuarioInfoResource


def config_app_routes(app, docs):
    api = Api(app)

    # Entidade
    __setting_route_doc(ClienteRegisterResource, '/cliente', api, docs)
    __setting_route_doc(ClienteResource, '/cliente/<string:id>', api, docs)
    __setting_route_doc(UsuarioInfoResource, '/usuario-info', api, docs)
    __setting_route_doc(FuncionarioRegisterResource, '/funcionario', api, docs)
    __setting_route_doc(EmpresaRegisterResource, '/empresa', api, docs)
    __setting_route_doc(TelefoneRegisterResource, '/telefone', api, docs)

    # Token
    __setting_route_doc(TokenUsuarioResource, '/token-usuario', api, docs)
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
        FuncaoFuncionarioRegisterResource, '/funcao-funcionario', api, docs
    )

    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
