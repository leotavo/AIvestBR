import logging
import os
import json
import sys
from datetime import datetime

class LoggerFactory:
    """
    Classe responsável por configurar e fornecer loggers separados por módulo e arquivo.
    """

    LOG_DIR = "logs"
    FORMATTER = logging.Formatter(
        json.dumps({
            "timestamp": "%(asctime)s",
            "level": "%(levelname)s",
            "module": "%(name)s",
            "message": "%(message)s"
        }),
        datefmt="%d/%m/%Y %H:%M"
    )

    @staticmethod
    def get_logger(module_name: str):
        """Cria um logger específico para o módulo fornecido."""

        # Criar diretório de logs do módulo
        module_dir = os.path.join(LoggerFactory.LOG_DIR, module_name)
        os.makedirs(module_dir, exist_ok=True)

        # Criar nome do arquivo com data e hora
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
        log_filename = os.path.join(module_dir, f"{module_name}_{timestamp}.log")

        # Criar logger com `force=True` para garantir que handlers não sejam reutilizados erroneamente
        logger = logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)

        # Remover handlers existentes para evitar duplicação
        while logger.handlers:
            logger.handlers.pop()

        # Configurar log para arquivo
        file_handler = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        file_handler.setFormatter(LoggerFactory.FORMATTER)

        # Configurar log para console (stderr)
        console_handler = logging.StreamHandler(sys.stderr)  # Forçar uso de stderr
        console_handler.setFormatter(LoggerFactory.FORMATTER)

        # Adicionar handlers ao logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger