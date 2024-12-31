from config.logging_config import logger

def connect_to_metatrader(credentials):
    """Connette l'utente a MetaTrader."""
    try:
        logger.info(f"Tentativo di connessione per l'utente {credentials['username']}")
        # Logica di connessione...
        logger.info("Connessione a MetaTrader avvenuta con successo.")
    except Exception as e:
        logger.error(f"Errore durante la connessione: {e}")
        raise
