from telegram.ext import CallbackContext
from telegram import Update
from db.utils import get_connection

# Admin login
async def admin_login(update: Update, context: CallbackContext):
    username = context.args[0]
    password = context.args[1]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM Admins WHERE username=?", (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        await update.message.reply_text("Admin authenticated.")
    else:
        await update.message.reply_text("Invalid login credentials.")

# Add task
async def add_task(update: Update, context: CallbackContext):
    task_description = context.args[0]
    difficulty = context.args[1]
    points = int(context.args[2])

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Tasks (task_name, difficulty, points) VALUES (?, ?, ?)",
                   (task_description, difficulty, points))
    conn.commit()

    await update.message.reply_text(f"Task '{task_description}' added successfully.")

# View team
async def view_team(update: Update, context: CallbackContext):
    team_name = context.args[0]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Teams WHERE team_name=?", (team_name,))
    team = cursor.fetchone()

    if team:
        await update.message.reply_text(f"Team {team_name} has {team[2]} points.")
    else:
        await update.message.reply_text("Team not found.")
