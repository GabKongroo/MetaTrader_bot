from config.logging_config import logger
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes
from utils.helpers import log_command

@log_command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce il comando /start."""
    user = update.effective_user

    welcome_message = (
        f"Ciao {user.first_name}, MetaTrader_Bot ti dà il benvenuto!\n\n"
        "Questo bot nasce per gestire le tue operazioni di trading con Meta Trader.\n"
        "Registra o accedi al tuo account Meta Trader con il pulsante qui sotto.\n\n"
        "⚠️ Nota bene che il bot utilizza un sistema di crittografia, "
        "i tuoi dati saranno cifrati e protetti nel nostro database ⚠️"
    )

    # Creazione della tastiera con un pulsante
    keyboard = [
        [InlineKeyboardButton("🔑 Registrati/Accedi", callback_data="register_or_login")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Invia il messaggio di benvenuto con il pulsante
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)
