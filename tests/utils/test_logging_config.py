import logging
import os
from typing import Generator
from unittest.mock import patch

import pytest

from aivestbr.utils.logging_config import LoggerFactory


@pytest.fixture
def clear_log_level_env() -> Generator[None, None, None]:
    """Fixture para limpar a variável de ambiente LOG_LEVEL antes de cada teste."""
    if "LOG_LEVEL" in os.environ:
        del os.environ["LOG_LEVEL"]
    yield
    if "LOG_LEVEL" in os.environ:
        del os.environ["LOG_LEVEL"]


def test_get_logger_default_level(clear_log_level_env: Generator[None, None, None]):
    """Testa se o logger é configurado com o nível padrão INFO."""
    logger = LoggerFactory.get_logger("test_logger_default")
    assert logger.level == logging.INFO


def test_get_logger_custom_level(clear_log_level_env: Generator[None, None, None]):
    """Testa se o logger é configurado com um nível customizado."""
    os.environ["LOG_LEVEL"] = "DEBUG"
    logger = LoggerFactory.get_logger("test_logger_custom")
    assert logger.level == logging.DEBUG


def test_get_logger_add_handler_once():
    """Testa se o handler é adicionado apenas uma vez ao logger."""
    logger = LoggerFactory.get_logger("test_logger_handler")
    initial_handler_count = len(logger.handlers)
    logger = LoggerFactory.get_logger("test_logger_handler")
    assert len(logger.handlers) == initial_handler_count


def test_get_logger_formatter():
    """Testa se o formatter do handler está configurado corretamente."""
    logger = LoggerFactory.get_logger("test_logger_formatter")
    handler = logger.handlers[0]
    assert isinstance(handler.formatter, logging.Formatter)
    assert (
        handler.formatter._fmt == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def test_set_level_valid():
    """Testa se o nível do logger é configurado corretamente para níveis válidos."""
    logger = logging.getLogger("test_set_level_valid")
    LoggerFactory.set_level(logger, "WARNING")
    assert logger.level == logging.WARNING


def test_set_level_invalid():
    """Testa se um ValueError é levantado para um nível de log inválido."""
    logger = logging.getLogger("test_set_level_invalid")
    with pytest.raises(ValueError, match="Nível de log inválido: INVALID"):
        LoggerFactory.set_level(logger, "INVALID")


def test_get_logger_with_mocked_env():
    """Testa se o logger é configurado corretamente com um nível de log mockado."""
    with patch.dict(os.environ, {"LOG_LEVEL": "ERROR"}):
        logger = LoggerFactory.get_logger("test_logger_mocked_env")
        assert logger.level == logging.ERROR
    with patch.dict(os.environ, {"LOG_LEVEL": "ERROR"}):
        logger = LoggerFactory.get_logger("test_logger_mocked_env")
        assert logger.level == logging.ERROR


def test_get_logger_creates_handler(clear_log_level_env: Generator[None, None, None]):
    """Testa se o logger cria e adiciona um StreamHandler corretamente."""
    logger = LoggerFactory.get_logger("test_logger_handler_creation")
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_get_logger_sets_formatter(clear_log_level_env: Generator[None, None, None]):
    """Testa se o logger configura o formatter corretamente."""
    logger = LoggerFactory.get_logger("test_logger_formatter_creation")
    handler = logger.handlers[0]
    assert isinstance(handler.formatter, logging.Formatter)
    assert (
        handler.formatter._fmt == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
