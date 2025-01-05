def validate_id_account(id_account: str) -> bool:
    """
    Valida l'ID conto MetaTrader.

    L'ID conto deve essere composto solo da cifre e avere una lunghezza compresa tra 6 e 12 caratteri.
    """
    return id_account.isdigit() and 6 <= len(id_account) <= 12


def validate_password(password: str) -> bool:
    """
    Valida la password MetaTrader.

    La password deve essere lunga almeno 8 caratteri e contenere almeno:
    - Un carattere alfabetico (a-z, A-Z)
    - Un carattere numerico (0-9)
    """
    return (
        len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password)
    )


def validate_server(server: str) -> bool:
    """
    Valida il nome del server MetaTrader.

    Il server deve essere un dominio valido, contenente almeno un punto e una lunghezza minima di 4 caratteri.
    """
    return "." in server and len(server) > 3 and all(part.isalnum() for part in server.split('.'))
