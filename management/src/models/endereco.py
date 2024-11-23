import os
import sqlalchemy as sa
import uuid

from sqlalchemy.dialects.postgresql import UUID
from src.db import db_instance as db
from src.db import db_persist


class EnderecoModel(db.Model):
    __tablename__ = 'Enderecos'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    logradouro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    complemento = db.Column(db.String(100), nullable=True)
    principal = db.Column(db.Boolean, default=False)
    empresa_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Empresas.id', ondelete='CASCADE'),
        nullable=True,
    )
    usuario_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Usuarios.id', ondelete='CASCADE'),
        nullable=True,
    )

    empresa = db.relationship('EmpresaModel', backref='enderecos')
    usuario = db.relationship('UsuarioModel', backref='enderecos')

    def __init__(self, logradouro, numero, bairro, cidade, estado, cep):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    @db_persist
    def salvar(self):
        db.session.add(self)

    @db_persist
    def excluir(self):
        db.session.delete(self)

    @classmethod
    def encontrar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()
