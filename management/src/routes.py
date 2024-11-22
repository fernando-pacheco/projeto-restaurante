from flask_restful import Api

# from src.resources.health_checker import HealthCheckerResource
# from src.resources.token import TokenRefresherResource, TokenResource
# from src.resources.user import UserRegisterResource


def config_app_routes(app, docs):
    api = Api(app)
    # __setting_route_doc(UserRegisterResource, '/user', api, docs)
    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
