import io
import json
import logging
import os
from unittest.mock import patch

import pytest

from aivestbr.utils.logging_config import LoggerFactory


@pytest.fixture
def logger():
    """Cria um logger para testes."""
    module_name = "test_module"
    logger = LoggerFactory.get_logger(module_name)

    return logger


def test_logger_file_creation(logger):
    """Verifica se o arquivo de log é criado corretamente."""
    log_dir = os.path.join("logs", "test_module")
    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
    assert len(log_files) > 0, "Nenhum arquivo de log foi criado."


@patch("sys.stderr", new_callable=io.StringIO)
def test_log_to_console(mock_stderr, logger):
    """Testa se a saída do console contém o log esperado."""
    test_message = "Teste de log para console"

    # Criar um handler temporário para capturar a saída no mock
    test_handler = logging.StreamHandler(mock_stderr)
    test_handler.setFormatter(LoggerFactory.FORMATTER)
    logger.addHandler(test_handler)

    # Enviar log
    logger.info(test_message)

    # Garantir que os logs foram escritos antes de capturar
    for handler in logger.handlers:
        handler.flush()

    # Capturar a saída do stderr
    output = mock_stderr.getvalue().strip()

    # Verificar se algo foi capturado
    assert output, "Nenhuma saída capturada no stderr."

    # Validar que o JSON contém a mensagem correta
    try:
        log_entries = output.split("\n")
        json_found = False

        for entry in log_entries:
            try:
                log_entry = json.loads(entry)
                if log_entry.get("message") == test_message:
                    json_found = True
                    break
            except json.JSONDecodeError:
                continue

        assert (
            json_found
        ), f"A mensagem '{test_message}' não foi encontrada no JSON do log."

    except Exception as e:
        pytest.fail(f"Erro ao validar JSON do log: {e}")

    # Remover o handler de teste para não interferir em outros testes
    logger.removeHandler(test_handler)


def test_log_format_json(logger):
    """Verifica se os logs estão no formato JSON correto."""
    log_dir = os.path.join("logs", "test_module")
    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]

    assert len(log_files) > 0, "Nenhum arquivo de log encontrado."

    latest_log_file = os.path.join(log_dir, log_files[-1])

    with open(latest_log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) > 0, "O arquivo de log está vazio."

    log_entry = json.loads(lines[-1].strip())

    assert "timestamp" in log_entry
    assert "level" in log_entry
    assert "module" in log_entry
    assert "message" in log_entry
