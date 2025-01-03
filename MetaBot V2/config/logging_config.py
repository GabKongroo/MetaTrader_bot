import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

# Percorso della cartella dei log
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Nome del file di log basato sulla data di avvio
start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = os.path.join(LOG_DIR, f"bot_{start_time}.log")

# Configurazione del logger
def setup_logger():
    # Configura un handler con rotazione
    rotating_handler = RotatingFileHandler(
        filename=log_filename,
        maxBytes=5_000_000,  # Dimensione massima (5 MB)
        backupCount=5        # Mantieni fino a 5 file di backup
    )

    # Configurazione di base
    logging.basicConfig(
        handlers=[rotating_handler],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger("TradingBot")
    return logger

# Logger globale da utilizzare nel progetto
logger = setup_logger()
logger.info("Logging configurato correttamente.")
