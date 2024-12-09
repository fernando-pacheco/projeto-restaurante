import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader
from src.email.cliente_smtp import ClienteSMTP


class EnvioEmailRecuperacao:
    def __init__(self):
        self.carregador_email = FileSystemLoader(
            searchpath=os.path.join(os.path.dirname(__file__), 'template')
        )
        self.template_env = Environment(loader=self.carregador_email)
        self.cliente_smtp = ClienteSMTP()

    def _carregar_template_email(self, data):
        template = self.template_env.get_template(
            'recuperacao_senha.html'
        )
        corpo_email = template.render(
            data={'data': data}
        )
        return corpo_email

    def _configurar_mensagem_email(self, conteudo_email):
        mensagem_email = MIMEMultipart()

        mensagem_email['from'] = os.getenv('EMAIL_FROM')
        mensagem_email['to'] = os.getenv('EMAIL_TO')
        mensagem_email['subject'] = f'Recuperação de senha'

        corpo_email = self._carregar_template_email(conteudo_email)
        mensagem_email.attach(MIMEText(corpo_email, 'html'))

        return mensagem_email

    def enviar_email(self, conteudo_email):
        mensagem_email = self._configurar_mensagem_email(conteudo_email)

        instancia = self.cliente_smtp._fazer_conexao()
        instancia.sendmail(
            from_addr=mensagem_email['from'],
            to_addrs=mensagem_email['to'],
            msg=mensagem_email.as_string(),
        )

        self.cliente_smtp._fechar_conexao()
