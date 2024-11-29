from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


def config_swagger(app):
    spec = APISpec(
        title='Gerenciador de Usuários - Documentação API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0',
        securityDefinitions={
            'BearerAuth': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'Cabeçalho de autorização JWT usa o Bearer schema. Insira seu JWT token no formato "Bearer <token>"',
            }
        },
        security=[{'BearerAuth': []}],
        tags=[
            {'name': 'Auth', 'description': 'Operações de autenticação'},
            {'name': 'Usuários', 'description': 'Gestão de Usuários'},
            {'name': 'Empresas', 'description': 'Gestão de empresas'},
            {'name': 'Funções', 'description': 'Gestão de funções'},
            {
                'name': 'Função Funcionário',
                'description': 'Gestão de permissionamento',
            },
            {'name': 'Telefones', 'description': 'Gestão de telefones'},
            {
                'name': 'Health Checker',
                'description': 'Verificação de funcionamento do servidor',
            },
        ],
    )

    app.config.update(
        {
            'APISPEC_SPEC': spec,
            'APISPEC_SWAGGER_URL': '/doc/',
            'APISPEC_SWAGGER_UI_URL': '/api/',
        }
    )

    return FlaskApiSpec(app)
