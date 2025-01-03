from bot.handlers import setup_handlers 
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config.settings import BOT_TOKEN
from config.logging_config import logger


def main():
    # Configura l'applicazione
    application = Application.builder().token(BOT_TOKEN).build()

    # Aggiungi gli handler per i comandi 
    setup_handlers(application)

    # Avvia il bot
    logger.info("Il bot è stato avviato!")
    application.run_polling()

if __name__ == "__main__":
    main()
