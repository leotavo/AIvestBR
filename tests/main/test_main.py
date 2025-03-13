import os
from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from flask.testing import FlaskClient

from aivestbr.main import app, main


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    with app.test_client() as client:
        yield client


def test_main_logs_initialization(mocker: MagicMock) -> None:
    mock_logger = mocker.patch("aivestbr.main.logger")
    mock_config = mocker.patch("aivestbr.main.config")
    mock_config.get.return_value = "sqlite:///:memory:"

    main()

    mock_logger.info.assert_any_call("Iniciando AIvestBR...")
    mock_logger.info.assert_any_call(
        "Conectando ao banco de dados: %s", "sqlite:///:memory:"
    )
    mock_logger.info.assert_any_call("Sistema inicializado com sucesso!")


def test_app_runs_on_specified_port(mocker: MagicMock) -> None:
    mocker.patch("aivestbr.main.main")
    mocker.patch.dict(os.environ, {"PORT": "4000"})
    mock_run = mocker.patch("aivestbr.main.app.run")

    if __name__ == "__main__":
        import aivestbr.main as main_module

        main_module.main()
        mock_run.assert_called_once_with(host="0.0.0.0", port=4000)


def test_app_runs_on_default_port(mocker: MagicMock) -> None:
    mocker.patch("aivestbr.main.main")
    mocker.patch.dict(os.environ, {}, clear=True)
    mock_run = mocker.patch("aivestbr.main.app.run")

    if __name__ == "__main__":
        import aivestbr.main as main_module

        main_module.main()
        mock_run.assert_called_once_with(host="0.0.0.0", port=5000)


@patch("aivestbr.main.logger")
@patch("aivestbr.main.config")
def test_main(mock_config: MagicMock, mock_logger: MagicMock) -> None:
    mock_config.get.return_value = "sqlite:///data/aivestbr.db"
    main()
    mock_logger.info.assert_any_call("Iniciando AIvestBR...")
    mock_logger.info.assert_any_call(
        "Conectando ao banco de dados: %s", "sqlite:///data/aivestbr.db"
    )
    mock_logger.info.assert_any_call("Sistema inicializado com sucesso!")


def test_run_app() -> None:
    with patch.dict(os.environ, {"PORT": "5000"}):
        with patch("aivestbr.main.app.run") as mock_run:
            mock_run.assert_called_with(host="0.0.0.0", port=5000)
