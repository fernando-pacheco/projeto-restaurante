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
        nullable=True,
    )
    cliente_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Clientes.id', ondelete='CASCADE'),
        nullable=True,
    )
    funcionario_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('management.Funcionarios.id', ondelete='CASCADE'),
        nullable=True,
    )

    empresa = db.relationship('EmpresaModel', backref='telefones')
    cliente = db.relationship('ClienteModel', backref='telefones')
    funcionario = db.relationship('FuncionarioModel', backref='telefones')

    @db_persist
    def salvar(self):
        db.session.add(self)

    @db_persist
    def excluir(self):
        db.session.delete(self)

    def obter_portador_id(self):
        return self._obter_campo_valido(
            ['funcionario_id', 'empresa_id', 'cliente_id']
        )

    def _obter_campo_valido(self, campos):
        retorno = None

        for campo in campos:
            value = getattr(self, campo, None)

            if value:
                retorno = value

        return retorno

    @classmethod
    def encontrar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def encontrar_por_numero(cls, numero):
        return cls.query.filter_by(numero=numero).first()

    @classmethod
    def encontrar_por_numero(cls, numero):
        return cls.query.filter_by(numero=numero).first()
