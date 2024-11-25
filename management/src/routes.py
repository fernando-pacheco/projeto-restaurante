from flask_restful import Api

from src.resources.funcionario import FuncionarioRegisterResource
from src.resources.empresa import EmpresaRegisterResource
from src.resources.health_checker import HealthCheckerResource
from src.resources.token import (
    TokenRefresherResource,
    TokenFuncionarioResource,
    TokenUsuarioResource,
)
from src.resources.usuario import UsuarioRegisterResource
from src.resources.funcao import FuncaoResource


def config_app_routes(app, docs):
    api = Api(app)

    # Entidade
    __setting_route_doc(UsuarioRegisterResource, '/usuario', api, docs)
    __setting_route_doc(FuncionarioRegisterResource, '/funcionario', api, docs)
    __setting_route_doc(EmpresaRegisterResource, '/empresa', api, docs)

    # Token
    __setting_route_doc(TokenUsuarioResource, '/token-usuario', api, docs)
    __setting_route_doc(
        TokenFuncionarioResource, '/token-funcionario', api, docs
    )
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)

    # Health Checker
    __setting_route_doc(HealthCheckerResource, '/health', api, docs)

    # Permissão
    __setting_route_doc(FuncaoResource, '/funcao', api, docs)

    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
