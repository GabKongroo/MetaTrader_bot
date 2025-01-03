from functools import wraps
from config.logging_config import logger
from telegram import Update

def log_command(func):
    """Decoratore per loggare l'esecuzione di comandi o callback."""
    @wraps(func)
    async def wrapper(update: Update, context, *args, **kwargs):
        user = update.effective_user
        logger.info(
            f"Esecuzione: {func.__name__} | Utente: {user.username} ({user.id}) | "
            f"Data: {update.message.date if update.message else 'N/A'} | "
            f"Callback: {update.callback_query.data if update.callback_query else 'N/A'}"
        )
        return await func(update, context, *args, **kwargs)
    return wrapper
