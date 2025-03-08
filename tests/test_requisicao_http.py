import unittest
from unittest.mock import patch, Mock
from aivestbr.data_ingestion.requisicao_http import RequisicaoHTTP
import requests

class TestRequisicaoHTTP(unittest.TestCase):

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_sucesso(self, mock_get):
        # Configura o mock para retornar uma resposta bem-sucedida
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'sucesso'
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.status_code, 200)
        self.assertEqual(resultado.text, 'sucesso')

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_falha_status_code(self, mock_get):
        # Configura o mock para retornar uma resposta com falha
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_timeout(self, mock_get):
        # Configura o mock para lançar uma exceção de timeout
        mock_get.side_effect = requests.exceptions.Timeout

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_conexao_erro(self, mock_get):
        # Configura o mock para lançar uma exceção de erro de conexão
        mock_get.side_effect = requests.exceptions.ConnectionError

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_erro_geral(self, mock_get):
        # Configura o mock para lançar uma exceção geral de requisição
        mock_get.side_effect = requests.exceptions.RequestException

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_resposta_vazia(self, mock_get):
        # Configura o mock para retornar uma resposta vazia
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = ''
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.text, '')

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_resposta_malformada(self, mock_get):
        # Configura o mock para retornar uma resposta malformada
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'malformed json'
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.text, 'malformed json')

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_status_code_500(self, mock_get):
        # Configura o mock para retornar uma resposta com status 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

    @patch('aivestbr.data_ingestion.requisicao.requests.get')
    def test_coletar_status_code_403(self, mock_get):
        # Configura o mock para retornar uma resposta com status 403
        mock_response = Mock()
        mock_response.status_code = 403
        mock_get.return_value = mock_response

        requisicao = RequisicaoHTTP('http://exemplo.com')
        resultado = requisicao.coletar()

        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
