import unittest
from unittest.mock import patch

import requests
from aivestbr.data_ingestion.requisicao_api import RequisicaoAPI

class TestRequisicaoAPI(unittest.TestCase):

    @patch('requests.get')
    def test_coletar_dados_json(self, mock_get):
        """
        Testa se a requisição para a URL retorna os dados corretamente quando a resposta é bem-sucedida (status 200) e conteúdo JSON válido.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"dados": "test"}
        # Dados JSON válidos
        
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="json")
        dados = requisicao.coletar()
        
        self.assertEqual(dados, {"dados": "test"})  # Verifica se os dados são JSON válidos

    @patch('requests.get')
    def test_coletar_dados_csv(self, mock_get):
        """
        Testa se a requisição para a URL retorna os dados corretamente quando o formato esperado é CSV.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'col1,col2\n1,2\n3,4'  # Dados CSV válidos
        
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="csv")
        dados = requisicao.coletar()
        
        self.assertEqual(dados, 'col1,col2\n1,2\n3,4')  # Verifica se os dados CSV são retornados como texto

    @patch('requests.get')  # Mock para requests.get (simula a requisição)
    def test_coletar_dados_wsdl(self, mock_get):
        """
        Testa se a requisição para a URL retorna os dados corretamente quando o formato esperado é WSDL.
        """
        # Simula a resposta de uma requisição bem-sucedida com um WSDL fictício (conteúdo XML válido)
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'<wsdl><service>Test WSDL</service></wsdl>'  # Dados WSDL válidos (conteúdo binário)
        
        requisicao = RequisicaoAPI("https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl", formato_esperado="wsdl")
        dados = requisicao.coletar()
        
        self.assertIsNotNone(dados)  # Verifica se o WSDL foi processado corretamente
        self.assertIn('<wsdl>', dados)  # Verifica se o conteúdo contém a tag <wsdl>

    @patch('requests.get')
    def test_coletar_dados_html(self, mock_get):
        """
        Testa se a requisição para a URL retorna os dados corretamente quando o formato esperado é HTML.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><body>Test</body></html>'  # Dados HTML válidos
        
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="html")
        dados = requisicao.coletar()
        
        self.assertIn('<html>', dados)  # Verifica se os dados são HTML válidos

    @patch('requests.get')
    def test_coletar_dados_falha_status_code(self, mock_get):
        """
        Testa se a requisição retorna None em caso de falha (status code != 200).
        """
        # Simula a resposta de uma requisição com erro (404)
        mock_get.return_value.status_code = 404
        
        requisicao = RequisicaoAPI("http://qualquerurl.com")
        dados = requisicao.coletar()
        
        # Verifica se o retorno é None devido ao erro
        self.assertIsNone(dados)

    @patch('requests.get')  # Mock para requests.get (simula a requisição)
    def test_coletar_dados_erro_requisicao(self, mock_get):
        """
        Testa se a requisição retorna None em caso de exceção durante a requisição.
        """
        # Simula uma exceção durante a requisição (por exemplo, timeout ou erro de rede)
        mock_get.side_effect = Exception("Erro na requisição")
        
        # Cria uma instância da RequisicaoAPI com qualquer URL (a URL real não importa aqui)
        requisicao = RequisicaoAPI("http://qualquerurl.com")
        dados = requisicao.coletar()  # Executa o método coletar
        
        # Verifica se a função retornou None devido à exceção
        self.assertIsNone(dados, "Esperado None devido ao erro na requisição")

    @patch('requests.get')
    def test_coletar_dados_resposta_vazia(self, mock_get):
        """
        Testa se a requisição retorna None quando a resposta não contém dados válidos (exemplo: conteúdo vazio).
        """
        # Simula uma resposta bem-sucedida, mas com conteúdo vazio
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}  # Resposta vazia
        
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="json")
        dados = requisicao.coletar()
        
        # Verifica se a função retorna None devido à resposta vazia
        self.assertIsNone(dados, "Esperado None devido a resposta vazia")

    @patch('requests.get')
    def test_coletar_dados_resposta_invalida(self, mock_get):
        """
        Testa se a requisição retorna None quando a resposta contém dados malformados ou inesperados.
        """
        # Simula uma resposta bem-sucedida, mas com dados malformados ou inesperados
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = 'dados inválidos'  # Resposta inesperada
        
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="json")
        dados = requisicao.coletar()
        
        # Verifica se a função retorna None devido a resposta malformada
        self.assertIsNone(dados, "Esperado None devido a resposta malformada")

    @patch('requests.get')
    def test_formato_nao_suportado(self, mock_get):
        """
        Testa se a requisição retorna None quando o formato esperado não é suportado.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'<xml><data>Test</data></xml>'
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="xml")
        dados = requisicao.coletar()
        self.assertIsNone(dados, "Esperado None para formato não suportado")

    @patch('requests.get')
    def test_coletar_dados_json_malformado(self, mock_get):
        """
        Testa se a requisição retorna None quando a resposta JSON é malformada.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = ValueError("JSON malformado")
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="json")
        dados = requisicao.coletar()
        self.assertIsNone(dados, "Esperado None para JSON malformado")

    @patch('requests.get')
    def test_coletar_dados_csv_malformado(self, mock_get):
        """
        Testa se a requisição retorna None quando a resposta CSV é malformada.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'col1,col2\n1,2\n3'  # CSV malformado
        requisicao = RequisicaoAPI("http://qualquerurl.com", formato_esperado="csv")
        dados = requisicao.coletar()
        self.assertIsNone(dados, "Esperado None para CSV malformado")

    @patch('requests.get')
    def test_coletar_dados_timeout(self, mock_get):
        """
        Testa se a requisição retorna None em caso de timeout.
        """
        # Simula uma exceção de timeout durante a requisição
        mock_get.side_effect = requests.exceptions.Timeout
        
        requisicao = RequisicaoAPI("http://qualquerurl.com")
        dados = requisicao.coletar()
        
        # Verifica se a função retornou None devido ao timeout
        self.assertIsNone(dados, "Esperado None devido ao timeout")

if __name__ == "__main__":
    unittest.main()
