from datetime import date, datetime


def is_b3_holiday(date: date):
    b3_holidays_2025 = [
        datetime(2025, 1, 1),  # Confraternização Universal
        datetime(2025, 3, 3),  # Carnaval
        datetime(2025, 3, 4),  # Carnaval
        datetime(2025, 4, 18),  # Sexta-feira Santa
        datetime(2025, 4, 21),  # Tiradentes
        datetime(2025, 6, 19),  # Corpus Christi
        datetime(2025, 11, 20),  # Dia Nacional de Zumbi e Consciência Negra
        datetime(2025, 12, 25),  # Natal
    ]
    return date in b3_holidays_2025


if __name__ == "__main__":
    today = datetime.now().date()
    if is_b3_holiday(today):
        print("Hoje é feriado na B3. O script não será executado.")
    else:
        # Coloque aqui o restante do seu código que deve ser executado nos dias úteis da B3
        pass
        pass
        pass
