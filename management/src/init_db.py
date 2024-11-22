from sqlalchemy import inspect

from src.db import db_instance
from src.models.empresa import EmpresaModel
from src.models.funcionario import FuncionarioModel
from src.models.token import TokenBlocklistModel
from src.models.usuario import UsuarioModel


def model_exists(model_class):
    engine = db_instance.get_engine()
    inspector = inspect(engine)
    return inspector.has_table(
        model_class.__tablename__, model_class.__table_args__['schema']
    ) or inspector.has_table(model_class.__tablename__)


def init_load_data():
    if model_exists(UsuarioModel):
        UsuarioModel.init_data()

    if model_exists(EmpresaModel):
        EmpresaModel.init_data()
