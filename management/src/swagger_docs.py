from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


def config_swagger(app):
    spec = APISpec(
        title='Gerenciador de Usuários - Documentação API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0',
        info=dict(
            description='API para gerenciamento de clientes e colaboradores do projeto Restaurantes'
        ),
        components={
            'securitySchemes': {
                'BearerAuth': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'JWT',
                }
            }
        },
    )

    spec.options.update(
        {
            'security': [{'BearerAuth': []}],
            'tags': [
                {'name': 'Auth', 'description': 'Operações de autenticação'},
                {'name': 'Usuários', 'description': 'Gestão de usuários'},
                {'name': 'Empresas', 'description': 'Gestão de empresas'},
                {'name': 'Funções', 'description': 'Gestão de funções'},
                {
                    'name': 'Função Funcionário',
                    'description': 'Gestão de permissionamento',
                },
                {
                    'name': 'Funcionários',
                    'description': 'Gestão de funcionários',
                },
                {'name': 'Telefones', 'description': 'Gestão de telefones'},
                {
                    'name': 'Health Checker',
                    'description': 'Verificação de funcionamento do servidor',
                },
            ],
            'servers': [
                {
                    'url': 'http://127.0.0.1:5000/',
                    'description': 'Servidor de Desenvolvimento',
                },
                # {
                #     'url': 'http://api.homologacao.com/api/v1',
                #     'description': 'Servidor de Homologação',
                # },
                # {
                #     'url': 'https://api.producao.com/api/v1',
                #     'description': 'Servidor de Produção',
                # },
            ],
        }
    )

    app.config.update(
        {
            'APISPEC_SPEC': spec,
            'APISPEC_SWAGGER_URL': '/doc/v1/',
            'APISPEC_SWAGGER_UI_URL': '/api/v1/',
        }
    )
    return FlaskApiSpec(app)
