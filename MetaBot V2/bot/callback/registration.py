from telegram import Update
from telegram.ext import ContextTypes
from utils.validation import validate_id_account, validate_password
#from database.db_manager import save_user_credentials
from config.settings import MT_SERVER
from metatrader.connection import test_connection

async def register_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inizia il processo di registrazione dell'ID conto MetaTrader."""
    query = update.callback_query
    user_id = query.from_user.id
    # Chiedi all'utente di inserire l'ID conto
    await query.edit_message_text("Per favore, inserisci il tuo ID conto MetaTrader:")
    context.user_data['registration_step'] = 'id_account'

async def handle_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce i vari passaggi della registrazione."""
    user_id = update.message.from_user.id
    text = update.message.text
    step = context.user_data.get('registration_step')

    if step == 'id_account':
        if validate_id_account(text):
            context.user_data['id_account'] = text
            await update.message.reply_text("Ora inserisci la tua password MetaTrader:")
            context.user_data['registration_step'] = 'password'
        else:
            await update.message.reply_text("ID conto non valido. Riprova.")

    elif step == 'password':
        if validate_password(text):
            context.user_data['password'] = text
            project_settings = {
                "mt5" : { 'username' : context.user_data['id_account'],
                        'password' : context.user_data['password'],
                        'server' : MT_SERVER,
                        'mt5_path' : "C:/Program Files/MetaTrader 5/terminal64.exe"
                    }
                }
            
            # Tenta di connettersi a MetaTrader
            if test_connection(project_settings=project_settings):
                # Salva le credenziali nel database
                #save_user_credentials(user_id, context.user_data['id_account'], context.user_data['password'])
                await update.message.reply_text("Registrazione completata con successo!")
                context.user_data.clear()
            else:
                await update.message.reply_text("Connessione a MetaTrader fallita. Verifica le tue credenziali e riprova.")
                context.user_data.clear()
        else:
            await update.message.reply_text("Password non valida. Riprova.")