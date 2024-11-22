import logging
import os
from logging.config import fileConfig

from alembic import context
from flask import current_app

from src.db import db_instance as db

# Configuração básica de logging
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Função para obter o engine
def get_engine():
    try:
        return current_app.extensions['migrate'].db.get_engine()
    except (TypeError, AttributeError):
        return current_app.extensions['migrate'].db.engine


# Função para obter a URL do banco de dados
def get_engine_url():
    try:
        return (
            get_engine()
            .url.render_as_string(hide_password=False)
            .replace('%', '%%')
        )
    except AttributeError:
        return str(get_engine().url).replace('%', '%%')


# Defina a URL no arquivo de configuração
config.set_main_option('sqlalchemy.url', get_engine_url())

# Defina o target_metadata como a metadata principal do SQLAlchemy
target_metadata = db.Model.metadata

# Função para rodar as migrações em modo offline
def run_migrations_offline():
    url = config.get_main_option('sqlalchemy.url')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        include_schemas=True,
        version_table_schema=os.getenv('MANAGEMENT_DB_SCHEMA'),
    )

    with context.begin_transaction():
        context.run_migrations()


# Função para rodar as migrações em modo online
def run_migrations_online():
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema=os.getenv('MANAGEMENT_DB_SCHEMA'),
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


# Escolha o modo de execução com base no contexto
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
