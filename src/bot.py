from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from telegram import Update, ReplyKeyboardMarkup
from registration import register_user, process_full_name, process_id_number
from admin import admin_login, add_task, view_team

# Set your token from the environment variable or config file
TOKEN = 'YOUR_BOT_TOKEN'

# Conversation states
FULL_NAME, ID_NUMBER, GROUP_OPTIONS = range(3)

async def start(update: Update, context) -> None:
    keyboard = [["Register for the game", "Get game explanation"], ["Join a group", "Login as admin"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome to Simon Says! Choose an option:", reply_markup=reply_markup)

# Register handlers and states
def main():
    application = Application.builder().token(TOKEN).build()
    
    # Conversation handler for registration
    registration_conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT & filters.Regex("Register for the game"), register_user)],
        states={
            FULL_NAME: [MessageHandler(filters.TEXT, process_full_name)],
            ID_NUMBER: [MessageHandler(filters.TEXT, process_id_number)],
            GROUP_OPTIONS: [
                MessageHandler(filters.TEXT & filters.Regex("Create a new group"), create_group),
                MessageHandler(filters.TEXT & filters.Regex("Join an existing group"), join_group),
            ]
        },
        fallbacks=[CommandHandler("start", start)]
    )
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("login", admin_login))
    application.add_handler(CommandHandler("addtask", add_task))
    application.add_handler(CommandHandler("viewteam", view_team))
    application.add_handler(registration_conv_handler)
    
    application.run_polling()

if __name__ == '__main__':
    main()
