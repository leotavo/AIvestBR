import logging
from config.settings import config

def main():
    """Função principal do projeto AIvestBR."""
    logging.basicConfig(level=config.LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
    
    logging.info("Iniciando o projeto AIvestBR...")

    # Exemplo de variável de configuração carregada do .env
    logging.info(f"Conectando ao banco de dados: {config.DATABASE_URL}")

    # TODO: Chamar os módulos do projeto aqui

    logging.info("Execução finalizada.")

if __name__ == "__main__":
    main()
