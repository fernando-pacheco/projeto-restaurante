import os
import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.db import db_instance as db
from src.db import db_persist


class EmpresaModel(db.Model):
    __tablename__ = 'Empresas'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    nome = db.Column(db.String(100), nullable=True)
    razao_social = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    status = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    data_atualizacao = db.Column(
        db.DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    def __init__(self, razao_social, cnpj, nome):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.nome = nome

    def __repr__(self):
        return f'<EmpresaModel(id={self.id}, nome_usuario={self.razao_social}), senha={self.cnpj})>'

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
    def encontrar_por_cnpj(cls, cnpj):
        return cls.query.filter_by(cnpj=cnpj).first()

    @staticmethod
    def init_data():
        if db.session.query(EmpresaModel.id).count() == 0:
            usuario = EmpresaModel(
                cnpj='00.000.000/0001-00',
                razao_social='Empresa XPTO',
            )
            usuario.salvar()


sa.orm.configure_mappers()
