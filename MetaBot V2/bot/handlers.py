from telegram.ext import CallbackQueryHandler, CommandHandler
from bot.commands import start
from bot.callbacks import register_or_login_callback

def setup_handlers(application):
    """Configura gli handler per il bot."""
    # Handler per il callback 'register_or_login'
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(register_or_login_callback, pattern="register_or_login"))
