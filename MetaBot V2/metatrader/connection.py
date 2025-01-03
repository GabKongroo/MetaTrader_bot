import MetaTrader5 as mt5
from utils.helpers import log_command

def test_connection(account_id: int, password: str, server: str) -> bool:
    """
    Testa la connessione a MetaTrader 5 con le credenziali fornite.
    
    Args:
        account_id (int): ID del conto MetaTrader.
        password (str): Password del conto MetaTrader.
        server (str): Server MetaTrader.

    Returns:
        bool: True se la connessione è avvenuta con successo, False altrimenti.
    """
    # Avvia la libreria MetaTrader 5
    if not mt5.initialize():
        return False

    # Effettua il login
    login_status = mt5.login(account_id, password=password, server=server)
    mt5.shutdown()  # Termina la libreria MetaTrader 5
    
    return login_status

