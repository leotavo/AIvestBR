📌 Ordem de Implementação Recomendada

1️⃣ **Implementar os Módulos Utilitários (utils/)**
Começamos pelos módulos de utilidade, pois serão usados por todos os outros componentes.

- `logging_config.py` → Define a configuração centralizada de logs.
- `http_client.py` → Classe para requisições HTTP, necessária para `api_ingestor.py`.
- `file_utils.py` → Funções para manipulação de arquivos (leitura/escrita).
- `validation.py` → Validação de dados antes do armazenamento.

✅ Agora temos funções auxiliares reutilizáveis para os próximos módulos.

2️⃣ **Criar o Gerenciador de Ingestores (ingest_manager.py)**
O `ingest_manager.py` será um Factory Pattern para centralizar a criação de ingestores.

✅ **Por que fazer isso agora?**
Ele depende apenas das classes de ingestão (`sources/`), mas não precisa das implementações finais para ser criado.

3️⃣ **Implementar os Ingestores (sources/)**
Agora que os utilitários estão prontos, podemos criar os ingestores, que farão uso dessas funções.

- `api_ingestor.py` → Depende de `http_client.py` para requisições HTTP.
- `file_ingestor.py` → Depende de `file_utils.py` para ler e salvar arquivos.
- `database_ingestor.py` → Pode usar `configs.py` para obter credenciais do banco de dados.
- `stream_ingestor.py` → Pode utilizar WebSockets, Kafka, MQTT, etc.

✅ Agora temos ingestores que podem ser instanciados pelo `ingest_manager.py`.

4️⃣ **Criar as Configurações (configs.py)**
Agora que os ingestores já existem, podemos criar `configs.py`, que armazenará URLs, credenciais, e parâmetros de configuração.

✅ Isso mantém credenciais e configurações fora do código-fonte principal.

5️⃣ **Implementar os Testes (tests/)**
Agora que a implementação está concluída, podemos garantir a qualidade do código.

- `test_http_client.py` → Testa requisições HTTP sem depender da internet (mocking).
- `test_file_ingestor.py` → Testa a leitura e escrita de arquivos locais.
- `test_api_ingestor.py` → Testa requisições de API utilizando `http_client.py`.
- `test_database_ingestor.py` → Testa conexões a bancos de dados com `database_ingestor.py`.
- `test_ingest_manager.py` → Testa se o `ingest_manager.py` instancia corretamente cada ingestor.

✅ Agora garantimos que tudo funciona corretamente antes de rodar o sistema.

🚀 **Resumo: Ordem de Implementação**

| Ordem | Arquivo                  | Motivo                                               |
|-------|--------------------------|------------------------------------------------------|
| 1️⃣   | `logging_config.py`      | Criar o sistema de logs central.                     |
| 2️⃣   | `http_client.py`         | Criar requisições HTTP reutilizáveis.                |
| 3️⃣   | `file_utils.py`          | Criar funções para manipular arquivos CSV, JSON, etc.|
| 4️⃣   | `validation.py`          | Criar validação de estrutura de dados.               |
| 5️⃣   | `ingest_manager.py`      | Criar o gerenciador central de ingestores (Factory Pattern). |
| 6️⃣   | `api_ingestor.py`        | Implementar ingestão de dados via API.               |
| 7️⃣   | `file_ingestor.py`       | Implementar ingestão de arquivos locais.             |
| 8️⃣   | `database_ingestor.py`   | Implementar ingestão de bancos de dados.             |
| 9️⃣   | `stream_ingestor.py`     | Implementar ingestão de dados em tempo real.         |
| 🔟    | `configs.py`             | Centralizar URLs, credenciais e parâmetros.          |
| 1️⃣1️⃣ | `test_http_client.py`    | Testar requisições HTTP.                             |
| 1️⃣2️⃣ | `test_file_ingestor.py`  | Testar leitura e escrita de arquivos.                |
| 1️⃣3️⃣ | `test_api_ingestor.py`   | Testar o ingestor de API.                            |
| 1️⃣4️⃣ | `test_database_ingestor.py` | Testar conexão a bancos de dados.                |
| 1️⃣5️⃣ | `test_ingest_manager.py` | Testar se os ingestores são instanciados corretamente |
