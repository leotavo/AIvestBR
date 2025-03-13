"""Configuração de logging para AIvestBR."""

import logging
import os


class LoggerFactory:
    """Fábrica de loggers para o AIvestBR."""

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """Cria e retorna um logger configurado."""
        logger = logging.getLogger(name)
        if not logger.handlers:
            log_level = os.getenv("LOG_LEVEL", "INFO").upper()
            logger.setLevel(log_level)
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        else:
            # Garantir que o nível de log seja atualizado mesmo se o handler já existir
            log_level = os.getenv("LOG_LEVEL", "INFO").upper()
            logger.setLevel(log_level)
        return logger

    @staticmethod
    def set_level(logger: logging.Logger, level: str) -> None:
        """Define dinamicamente o nível de log."""
        if level.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError(f"Nível de log inválido: {level}")
        logger.setLevel(level.upper())
        logger.setLevel(level.upper())
