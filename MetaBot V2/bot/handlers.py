from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, filters
from bot.commands import start
from bot.callback.registration import register_id, handle_registration

def setup_handlers(application):
    """Configura gli handler per il bot."""
    # Handler per il comando /start
    application.add_handler(CommandHandler("start", start))
    # Handler per la registrazione
    application.add_handler(CallbackQueryHandler(register_id, pattern="register"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_registration))