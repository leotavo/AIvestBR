import requests
import logging
from typing import Optional

class RequisicaoHTTP:
    def __init__(self, url: str):
        self.url = url

    def coletar(self) -> Optional[requests.Response]:
        """
        Realiza a requisição para a URL fornecida e retorna o objeto requests.Response.
        """
        try:
            resposta = requests.get(self.url)
            
            if resposta.status_code == 200:
                logging.info(f"Requisição bem-sucedida para a URL: {self.url}")
                return resposta
            else:
                logging.error(f"Falha ao acessar {self.url}, status: {resposta.status_code}, tempo de resposta: {resposta.elapsed}")
                return None

        except requests.exceptions.Timeout as e:
            logging.error(f"Erro de timeout ao fazer a requisição: {e}")
            return None
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Erro de conexão ao fazer a requisição: {e}")
            return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro geral na requisição: {e}")
            return None
        except Exception as e:
            logging.error(f"Erro inesperado na requisição: {e}")
            return None
