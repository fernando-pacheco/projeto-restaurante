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

    def __init__(self, funcao, nivel):
        self.funcao = funcao
        self.nivel = nivel

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
    def encontrar_por_numero(cls, funcao):
        return cls.query.filter_by(funcao=funcao).first()

    @staticmethod
    def init_data():
        funcoes = ['operador', 'financeiro', 'administrador', 'principal']
        niveis = [1, 5, 7, 9]
        if db.session.query(FuncaoModel.id).count() == 0:
            for funcao, nivel in zip(funcoes, niveis):
                registro = FuncaoModel(funcao=funcao, nivel=nivel)
                registro.salvar()
