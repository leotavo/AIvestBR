"""Configuração do sistema AIvestBR."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Carregar automaticamente o arquivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


class Config:
    """Classe para centralizar as configurações do sistema AIvestBR."""

    def __init__(self) -> None:
        """Inicializa as configurações do sistema."""
        self._settings: dict[str, str] = {
            "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///data/aivestbr.db"),
            "API_KEY": os.getenv("API_KEY", "SUA_CHAVE_AQUI"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "BACEN_API_BASE_URL": os.getenv(
                "BACEN_API_BASE_URL", "https://api.bcb.gov.br/dados/serie/bcdata.sgs"
            ),
        }

    def get(self, key: str, default: str = "") -> str:
        """Obtém o valor de uma configuração pelo nome da chave."""
        return self._settings.get(key, default)

    def all(self) -> dict[str, str]:
        """Retorna todas as configurações disponíveis."""
        return self._settings.copy()
