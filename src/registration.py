from telegram import Update
from telegram.ext import CallbackContext
from db.utils import get_connection

# Steps for registration
async def register_user(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Please enter your full name:")
    return FULL_NAME

async def process_full_name(update: Update, context: CallbackContext) -> int:
    context.user_data['full_name'] = update.message.text
    await update.message.reply_text("Please enter your ID number:")
    return ID_NUMBER

async def process_id_number(update: Update, context: CallbackContext) -> int:
    full_name = context.user_data['full_name']
    id_number = update.message.text

    conn = get_connection()
    cursor = conn.cursor()

    # Check if ID is already registered
    cursor.execute("SELECT * FROM users WHERE id_number=?", (id_number,))
    user = cursor.fetchone()

    if user:
        await update.message.reply_text("This ID number is already registered.")
    else:
        cursor.execute("INSERT INTO users (full_name, id_number) VALUES (?, ?)", (full_name, id_number))
        conn.commit()
        await update.message.reply_text(f"Thank you {full_name}! Registration successful.")
    
    conn.close()
    return GROUP_OPTIONS
