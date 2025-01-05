import MetaTrader5 as mt5
import os
import signal
from config.settings import MT_SERVER

def test_connection(project_settings) -> bool:
    """Tenta di connettersi a MetaTrader con le credenziali fornite e restituisce True se la connessione ha successo, altrimenti False."""
    username = project_settings['mt5']['username']
    username = int(username)
    password = project_settings['mt5']['password']
    server = project_settings['mt5']['server']
    mt5_path = project_settings['mt5']['mt5_path']
    
    # Inizializza MetaTrader 5 con le credenziali
    if not mt5.initialize(login=username, password=password, server=server, path=mt5_path):
        error_code, description = mt5.last_error()
        print(f"Errore di inizializzazione di MetaTrader5: {description} (codice errore: {error_code})")
        return False

    try:
        # Tenta di connettersi con le credenziali fornite
        authorized = mt5.login(login=username, password=password, server=server, path=mt5_path)
        if not authorized:
            error_code, description = mt5.last_error()
            print(f"Errore di connessione a MetaTrader5: {description} (codice errore: {error_code})")
            return False
        
        # Connessione riuscita
        return True
    
    finally:
        # Disconnette MetaTrader 5
        mt5.shutdown()
        # Chiude l'applicazione MetaTrader5
        os.system("taskkill /f /im terminal64.exe")  # Per Windows
        # os.system("pkill terminal64")  # Per Linux/Mac