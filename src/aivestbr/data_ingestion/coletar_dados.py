import logging

from aivestbr.data_ingestion.requisicao_api import RequisicaoAPI
from aivestbr.data_ingestion.salvamento_dados import SalvamentoDados

def coletar_dados(url, formato='json'):
    """
    Função para coletar e salvar dados a partir de uma URL.
    
    Parâmetros:
    url (str): URL da API para fazer a requisição.
    formato (str): Formato para salvar os dados ('json' ou 'csv').
    """
    try:
        # 1. Realiza a requisição usando a classe RequisicaoAPI
        logging.info(f"Iniciando coleta de dados para a URL: {url}")
        requisicao = RequisicaoAPI(url)
        dados = requisicao.coletar()  # Coleta os dados usando a classe RequisicaoAPI
        
        # Verifica se dados foram coletados com sucesso
        if dados:
            logging.info(f"Dados coletados com sucesso: {dados}")
            # 2. Salva os dados usando a classe SalvamentoDados
            salvamento = SalvamentoDados(dados, formato)
            if salvamento.salvar():
                logging.info("Processo de coleta e salvamento concluído com sucesso.")
                return dados  # Retorna os dados caso o salvamento seja bem-sucedido
            else:
                logging.error("Erro ao salvar os dados.")
                return None
        else:
            logging.error("Erro na coleta dos dados.")
            return None
    except Exception as e:
        # Log de qualquer exceção inesperada que possa ocorrer durante o processo
        logging.error(f"Erro ao fazer a requisição: {e}")
        return None
