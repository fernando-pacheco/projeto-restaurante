import os
from smtplib import SMTP


class ClienteSMTP:
    def __init__(self):
        self.conexao = None

    def _fazer_conexao(self):
        self.conexao = SMTP(
            host=os.getenv('EMAIL_HOST'), port=int(os.getenv('EMAIL_PORT'))
        )

        return self.conexao

    def _fechar_conexao(self):
        self.conexao.quit()
