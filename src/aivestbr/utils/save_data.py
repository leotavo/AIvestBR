# src/aivestbr/utils/save_data.py
def save_data(df: pd.DataFrame, filename: str, format: str = 'csv') -> None:
    """
    Salva os dados processados em um arquivo no formato especificado.

    Parâmetros:
    df (pd.DataFrame): DataFrame com os dados a serem salvos.
    filename (str): Caminho do arquivo de saída.
    format (str): Formato do arquivo (padrão 'csv'). Pode ser 'csv' ou 'json'.
    """
    try:
        if format == 'csv':
            df.to_csv(filename)
        elif format == 'json':
            df.to_json(filename, orient='records', lines=True)
        else:
            raise ValueError("Formato não suportado. Use 'csv' ou 'json'.")
        print(f"Dados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
