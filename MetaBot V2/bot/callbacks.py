from utils.helpers import log_command
from telegram import Update
from telegram.ext import ContextTypes
from config.logging_config import logger
from database.db_manager import is_user_registered, logout_user


@log_command
async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce i callback dei pulsanti del menu principale."""
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer()  # Risponde al callback per evitare timeout

    if query.data == "register":
        await query.edit_message_text("Inizia la registrazione con i tuoi dati MetaTrader.")
        # Avvia il processo di registrazione
        from callback.registration import register_id


