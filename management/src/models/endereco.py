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

    def obter_portador_id(self):
        return self._obter_campo_valido(['empresa_id', 'usuario_id'])

    def _obter_campo_valido(self, campos):
        retorno = None

        for campo in campos:
            value = getattr(self, campo, None)

            if value:
                retorno = value

        return retorno

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
    def encontrar_por_cep(cls, cep):
        return cls.query.filter_by(cep=cep).first()

    @classmethod
    def listar_enderecos_por_entidade(
        cls, entidade_id=None, tipo_entidade=None
    ):
        tipo_entidade_stg = {
            'usuario': cls.usuario_id,
            'empresa': cls.empresa_id,
        }

        filtro = tipo_entidade_stg[tipo_entidade]
        return cls.query.filter(filtro == entidade_id).all()
