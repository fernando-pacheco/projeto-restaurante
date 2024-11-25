from flask_restful import Api

from src.resources.empresa import EmpresaRegisterResource
from src.resources.health_checker import HealthCheckerResource
from src.resources.token import TokenRefresherResource, TokenResource
from src.resources.usuario import UsuarioRegisterResource
from src.resources.funcao import FuncaoResource


def config_app_routes(app, docs):
    api = Api(app)
    __setting_route_doc(UsuarioRegisterResource, '/user', api, docs)
    __setting_route_doc(TokenResource, '/token', api, docs)
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)
    __setting_route_doc(HealthCheckerResource, '/health', api, docs)
    __setting_route_doc(FuncaoResource, '/funcao', api, docs)
    __setting_route_doc(EmpresaRegisterResource, '/empresa', api, docs)
    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
