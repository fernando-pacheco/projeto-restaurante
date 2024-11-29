import os

from src.db import db_instance as db
from src.db import db_persist


class FuncaoModel(db.Model):
    __tablename__ = 'Funcoes'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    funcao = db.Column(db.String(20))
    nivel = db.Column(db.Integer)
    funcao_funcionario = db.relationship(
        'FuncaoFuncionarioModel',
        back_populates='nome_funcao',
        cascade='all, delete-orphan',
    )

    def __repr__(self):
        return self.funcao

    @db_persist
    def salvar(self):
        db.session.add(self)

    @db_persist
    def excluir(self):
        db.session.delete(self)

    @classmethod
    def encontrar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def encontrar_por_funcao(cls, funcao):
        return cls.query.filter_by(funcao=funcao).first()

    @classmethod
    def listar_funcoes(cls):
        return cls.query.all()

    @staticmethod
    def init_data():
        funcoes = ['operador', 'financeiro', 'administrador', 'principal']
        niveis = [1, 5, 7, 9]
        if db.session.query(FuncaoModel.id).count() == 0:
            for funcao, nivel in zip(funcoes, niveis):
                registro = FuncaoModel(funcao=funcao, nivel=nivel)
                registro.salvar()
