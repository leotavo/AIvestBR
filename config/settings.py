"""Configuração do sistema AIvestBR."""

import os


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

    def get(self, key: str) -> str:
        """Obtém o valor de uma configuração pelo nome da chave."""
        return self._settings.get(key, "")

    def all(self) -> dict[str, str]:
        """Retorna todas as configurações disponíveis."""
        return self._settings.copy()
        return self._settings.copy()
