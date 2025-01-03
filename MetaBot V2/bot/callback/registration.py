from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from utils.validation import validate_id_account, validate_password, validate_server
from metatrader.connection import test_connection

# Stati della registrazione
ID_ACCOUNT, PASSWORD, SERVER = range(3)

async def register_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Avvia la registrazione richiedendo l'ID conto."""
    await update.message.reply_text("Inserisci il tuo ID conto MetaTrader:")
    return ID_ACCOUNT

async def handle_id_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Gestisce e valida l'input dell'ID conto."""
    user_input = update.message.text.strip()
    if validate_id_account(user_input):
        context.user_data["id_account"] = user_input
        await update.message.reply_text("Ora inserisci la tua password:")
        return PASSWORD
    else:
        await update.message.reply_text(
            "L'ID conto non è valido. Deve essere un numero tra 6 e 12 cifre. Riprova:"
        )
        return ID_ACCOUNT


async def handle_password_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Gestisce e valida l'input della password."""
    user_input = update.message.text.strip()
    if validate_password(user_input):
        context.user_data["password"] = user_input
        await update.message.reply_text("Ora inserisci il nome del server ():")
        return SERVER
    else:
        await update.message.reply_text(
            "La password non è valida. Deve avere almeno 8 caratteri con lettere e numeri. Riprova:"
        )
        return PASSWORD


async def handle_server_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Gestisce e valida l'input del server."""
    user_input = update.message.text.strip()
    if validate_server(user_input):
        context.user_data["server"] = user_input
  
        # Tenta la connessione a MetaTrader
        id_account = context.user_data["id_account"]
        password = context.user_data["password"]
        server = context.user_data["server"]

        if test_connection(id_account, password, server):
            await update.message.reply_text("Registrazione completata con successo!")
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                "Connessione a MetaTrader fallita. Riprova registrandoti di nuovo."
            )
            return ID_ACCOUNT
    else:
        await update.message.reply_text(
            "Il nome del server non è valido. Deve essere un dominio valido. Riprova:"
        )
        return SERVER


async def cancel_registration(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Gestisce l'annullamento della registrazione."""
    await update.message.reply_text("Registrazione annullata. Puoi riprovare in qualsiasi momento.")
    return ConversationHandler.END
