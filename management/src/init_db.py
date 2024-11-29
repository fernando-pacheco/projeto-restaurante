from sqlalchemy import inspect
from src.db import db_instance
from src.models.empresa import EmpresaModel
from src.models.endereco import EnderecoModel
from src.models.funcao import FuncaoModel
from src.models.funcao_funcionario import FuncaoFuncionarioModel
from src.models.funcionario import FuncionarioModel
from src.models.telefone import TelefoneModel
from src.models.token import TokenBlocklistModel
from src.models.cliente import ClienteModel


def model_exists(model_class):
    engine = db_instance.get_engine()
    inspector = inspect(engine)
    return inspector.has_table(
        model_class.__tablename__, model_class.__table_args__['schema']
    ) or inspector.has_table(model_class.__tablename__)


def init_load_data():
    if model_exists(ClienteModel):
        ClienteModel.init_data()

    if model_exists(EmpresaModel):
        EmpresaModel.init_data()

    if model_exists(FuncaoModel):
        FuncaoModel.init_data()
