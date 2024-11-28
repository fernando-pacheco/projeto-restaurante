from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


def config_swagger(app):
    spec = APISpec(
        title='Gerenciador de Usuários - Documentação API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='3.0.2',
        components={
            'securitySchemes': {
                'BearerAuth': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'JWT',
                    'description': 'Cabeçalho de autorização JWT usando o esquema Bearer. Insira seu token JWT no formato "Bearer <token>"',
                }
            },
            'requestBodies': {
                'DefaultRequestBody': {
                    'content': {
                        'application/json': {'schema': {'type': 'object'}}
                    }
                }
            },
        },
        security=[{'BearerAuth': []}],
        tags=[
            {'name': 'Auth', 'description': 'Operações de autenticação'},
            {'name': 'Usuários', 'description': 'Gestão de usuários'},
            {'name': 'Empresas', 'description': 'Gestão de empresas'},
            {'name': 'Funcionários', 'description': 'Gestão de funcionários'},
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
        servers=[
            {
                'url': 'http://127.0.0.1:8000/',
                'description': 'Servidor de Desenvolvimento',
            }
        ],
    )

    app.config.update(
        {
            'APISPEC_SPEC': spec,
            'APISPEC_SWAGGER_URL': '/doc/v1/',
            'APISPEC_SWAGGER_UI_URL': '/api/v1/',
        }
    )

    return FlaskApiSpec(app)
