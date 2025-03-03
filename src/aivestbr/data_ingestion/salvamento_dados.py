import os
from datetime import datetime
import logging

class SalvamentoDados:
    def __init__(self, dados, formato='json'):
        self.dados = dados
        self.formato = formato
        self.diretorio = 'data'

    def salvar(self):
        """
        Salva os dados coletados no formato desejado.
        """
        try:
            if not os.path.exists(self.diretorio):
                os.makedirs(self.diretorio)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nome_arquivo = f"{self.diretorio}/dados_{timestamp}.{self.formato}"

            if self.formato == 'json':
                with open(nome_arquivo, 'w') as f:
                    f.write(self.dados)
            elif self.formato == 'csv':
                with open(nome_arquivo, 'w') as f:
                    f.write(self.dados)
            else:
                logging.error(f"Formato {self.formato} não suportado.")
                return False

            logging.info(f"Dados salvos em {nome_arquivo}")
            return True
        except Exception as e:
            logging.error(f"Erro ao salvar os dados: {e}")
            return False
