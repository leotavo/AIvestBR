"""
Módulo principal do AIvestBR. Responsável por iniciar a aplicação.

- Melhoria futura: Implementar integração com outros módulos
do projeto para execução de tarefas específicas.
"""

import logging

from config.settings import config


def main():
    """Função principal do projeto AIvestBR."""
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logging.info("Iniciando o projeto AIvestBR...")

    # Exemplo de variável de configuração carregada do .env
    logging.info("Conectando ao banco de dados: %s", config.DATABASE_URL)

    logging.info("Execução finalizada.")


if __name__ == "__main__":
    main()

# Linha vazia no final para evitar W292
