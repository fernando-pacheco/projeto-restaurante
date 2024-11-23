import os

from sqlalchemy.dialects.postgresql import UUID
from src.db import db_instance as db
from src.db import db_persist


class TelefoneModel(db.Model):
    __tablename__ = 'Telefones'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    numero = db.Column(db.String(11), nullable=False)
    principal = db.Column(db.Boolean, default=False)
    empresa_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Empresas.id', ondelete='CASCADE'),
    )
    usuario_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Usuarios.id', ondelete='CASCADE'),
    )

    empresa = db.relationship('EmpresaModel', backref='telefones')
    usuario = db.relationship('UsuarioModel', backref='telefones')

    def __init__(self, numero):
        self.numero = numero

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
    def encontrar_por_numero(cls, numero):
        return cls.query.filter_by(numero=numero).first()
