"""Módulo principal do AIvestBR."""

import os

from flask import Flask

from aivestbr.utils.logging_config import LoggerFactory
from config.settings import Config

app = Flask(__name__)


logger = LoggerFactory.get_logger(__name__)
config = Config()  # Instancia a classe Config


def main() -> None:
    """Função principal do sistema AIvestBR."""
    logger.info("Iniciando AIvestBR...")
    logger.info("Conectando ao banco de dados: %s", config.get("DATABASE_URL"))
    logger.info("Sistema inicializado com sucesso!")


if __name__ == "__main__":
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
