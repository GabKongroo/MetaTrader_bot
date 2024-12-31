import config.settings 
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

#importa il token
BOT_TOKEN = config.settings.BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce il comando /start."""
    user = update.effective_user
    await update.message.reply_text(f"Ciao {user.first_name}! Benvenuto nel bot!")

def main():
    # Configura l'applicazione
    application = Application.builder().token(BOT_TOKEN).build()

    # Aggiungi handler per il comando /start
    application.add_handler(CommandHandler("start", start))

    # Avvia il bot
    application.run_polling()

if __name__ == "__main__":
    main()
