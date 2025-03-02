"""
Módulo de configuração do AIvestBR.
Carrega variáveis de ambiente e define parâmetros globais do sistema.
"""

import os
from dotenv import load_dotenv

# Caminho do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), "../config/.env")

# Carregar as variáveis de ambiente do .env (se existir)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    """Classe para armazenar configurações globais do projeto."""

    # 🔹 Configurações Gerais
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    # 🔹 Banco de Dados (caso queira armazenar dados)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

    # 🔹 Diretórios do Projeto
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    # 🔹 Chaves de API (exemplo para Yahoo Finance ou outras fontes)
    API_KEY = os.getenv("API_KEY", "")

    @staticmethod
    def verificar_diretorios():
        """Garante que os diretórios necessários existam."""
        for diretorio in [Config.DATA_DIR, Config.OUTPUT_DIR]:
            os.makedirs(diretorio, exist_ok=True)

# Criar diretórios automaticamente ao carregar o módulo
Config.verificar_diretorios()