import os

from src.db import db_instance as db
from src.db import db_persist
from sqlalchemy.dialects.postgresql import UUID


class FuncaoFuncionarioModel(db.Model):
    __tablename__ = 'FuncaoFuncionario'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    funcionario_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Funcionarios.id', ondelete='CASCADE'),
        nullable=False,
    )
    funcao_id = db.Column(
        db.Integer,
        db.ForeignKey('management.Funcoes.id', ondelete='CASCADE'),
        nullable=False,
    )

    @db_persist
    def salvar(self):
        db.session.add(self)

    @db_persist
    def excluir(self):
        db.session.delete(self)

    @classmethod
    def encontrar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()
