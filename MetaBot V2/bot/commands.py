from utils.helpers import log_command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from config.logging_config import logger
from database.db_manager import is_user_logged_in

@log_command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce il comando /start e mostra il menu principale."""
    user = update.effective_user
    user_id = user.id

    welcome_message = (
        f"Ciao {user.first_name}, MetaTrader_Bot ti dà il benvenuto!\n\n"
        "Questo bot nasce per gestire le tue operazioni di trading con Meta Trader.\n"
        "Registra o accedi al tuo account Meta Trader con il pulsante qui sotto.\n\n"
        "⚠️ Nota bene che il bot utilizza un sistema di crittografia, "
        "i tuoi dati saranno cifrati e protetti nel nostro database ⚠️"
    )
    # Menu per utenti non connessi
    keyboard = [
        [InlineKeyboardButton("🔑 Registrati", callback_data="register")],
        [InlineKeyboardButton("🔓 Accedi", callback_data="login")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)
