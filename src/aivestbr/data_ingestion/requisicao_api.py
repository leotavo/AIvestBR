import requests
import logging
import csv
from lxml import etree  # Para validar WSDL (XML)
from bs4 import BeautifulSoup  # Para validar HTML
from typing import Optional, Union, Dict

class RequisicaoAPI:
    def __init__(self, url: str, formato_esperado: str = 'json'):
        self.url = url
        self.formato_esperado = formato_esperado.lower()

    def coletar(self) -> Optional[Union[Dict, str, etree._Element]]:
        """
        Realiza a requisição para a URL fornecida e retorna os dados no formato adequado.
        """
        try:
            resposta = requests.get(self.url)
            
            # Verifica o código de status da resposta
            if resposta.status_code == 200:
                logging.info(f"Requisição bem-sucedida para a URL: {self.url}")
                
                # Verifica o tipo de formato esperado e valida a resposta
                if self.formato_esperado == 'json':
                    return self._processar_json(resposta)
                elif self.formato_esperado == 'csv':
                    return self._processar_csv(resposta)
                elif self.formato_esperado == 'wsdl':
                    return self._processar_wsdl(resposta)
                elif self.formato_esperado == 'html':
                    return self._processar_html(resposta)
                else:
                    logging.error(f"Formato {self.formato_esperado} não suportado.")
                    return None
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

    def _processar_json(self, resposta: requests.Response) -> Optional[Dict]:
        """
        Processa a resposta JSON.
        """
        try:
            dados_json = resposta.json()  # Tenta fazer o parse do JSON
            if not isinstance(dados_json, dict):  # Verifica se o JSON é um dicionário válido
                logging.error("Resposta JSON não é um dicionário válido")
                return None
            if not dados_json:  # Verifica se o JSON está vazio
                logging.error("Resposta JSON está vazia")
                return None
            return dados_json
        except ValueError as e:
            logging.error(f"Resposta malformada, não é um JSON válido: {e}")
            return None

    def _processar_csv(self, resposta: requests.Response) -> Optional[str]:
        """
        Processa a resposta CSV.
        """
        try:
            # Tentando ler o CSV e verificar se ele é válido
            csv_reader = csv.reader(resposta.text.splitlines())
            rows = list(csv_reader)
            if not rows or any(len(row) != len(rows[0]) for row in rows):  # Verifica se o CSV está malformado
                logging.error("CSV malformado")
                return None
            return resposta.text  # Retorna o conteúdo como texto, sem conversão para lista
        except Exception as e:
            logging.error(f"Erro ao processar CSV: {e}")
            return None

    def _processar_wsdl(self, resposta: requests.Response) -> Optional[str]:
        """
        Processa a resposta WSDL (XML).
        """
        try:
            # Usa lxml para validar o WSDL (XML)
            root = etree.fromstring(resposta.content)  # Usar .content para lidar com a resposta em binário
            return etree.tostring(root, pretty_print=True).decode()  # Retorna o WSDL como string formatada
        except etree.XMLSyntaxError as e:
            logging.error(f"Erro ao processar WSDL, XML inválido: {e}")
            return None

    def _processar_html(self, resposta: requests.Response) -> Optional[str]:
        """
        Processa a resposta HTML.
        """
        try:
            # Usa BeautifulSoup para validar o HTML
            soup = BeautifulSoup(resposta.text, 'html.parser')
            if soup.html:
                return soup.prettify()  # Retorna HTML formatado
            else:
                logging.error("Resposta não é um HTML válido")
                return None
        except Exception as e:
            logging.error(f"Erro ao processar HTML: {e}")
            return None