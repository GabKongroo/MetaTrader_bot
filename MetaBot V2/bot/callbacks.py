from telegram import Update
from telegram.ext import ContextTypes
from utils.helpers import log_command

@log_command
async def register_or_login_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce il callback del pulsante 'Registrati/Accedi'."""
    query = update.callback_query
    await query.answer()  # Chiude il "caricamento" del pulsante nel client Telegram

    # Rispondi all'utente con un messaggio appropriato
    await query.edit_message_text(
        text=(
            "🔑 Per registrarti o accedere al tuo account Meta Trader, "
            "fornisci le tue credenziali in modo sicuro.\n\n"
            "👉 *Nota*: Inserisci solo dati verificati per garantire l'accesso corretto."
        )
    )
