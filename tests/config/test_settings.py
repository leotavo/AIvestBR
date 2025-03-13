import os
from unittest.mock import patch

import pytest

from config.settings import Config


@pytest.fixture
def config() -> Config:
    return Config()


def test_get_existing_key(config: Config) -> None:
    assert config.get("DATABASE_URL") == "sqlite:///data/aivestbr.db"


def test_get_non_existing_key(config: Config) -> None:
    assert config.get("NON_EXISTENT_KEY") == ""


def test_all_settings(config: Config) -> None:
    settings = config.all()
    assert isinstance(settings, dict)
    assert settings["DATABASE_URL"] == "sqlite:///data/aivestbr.db"
    assert settings["API_KEY"] == "SUA_CHAVE_AQUI"
    assert settings["LOG_LEVEL"] == "INFO"
    assert (
        settings["BACEN_API_BASE_URL"]
        == "https://api.bcb.gov.br/dados/serie/bcdata.sgs"
    )


@patch.dict(os.environ, {"DATABASE_URL": "postgresql://localhost/aivestbr"})
def test_get_with_env_variable() -> None:
    config = Config()
    assert config.get("DATABASE_URL") == "postgresql://localhost/aivestbr"


def test_all_with_env_variables() -> None:
    with patch.dict(os.environ, {"DATABASE_URL": "postgresql://localhost/aivestbr"}):
        config = Config()
        settings = config.all()
        assert settings["DATABASE_URL"] == "postgresql://localhost/aivestbr"
