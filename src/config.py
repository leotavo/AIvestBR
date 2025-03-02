import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    """Classe para centralizar as configurações do projeto."""
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/aivestbr.db")
    API_KEY = os.getenv("API_KEY", "SUA_CHAVE_AQUI")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Criar uma instância global das configurações
config = Config()

# Exemplo de uso
if __name__ == "__main__":
    print(f"Banco de Dados: {config.DATABASE_URL}")
    print(f"API Key: {config.API_KEY}")
    print(f"Nível de Log: {config.LOG_LEVEL}")