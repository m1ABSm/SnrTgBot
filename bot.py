from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from config import AUTH_USERS
from document_parser import process_file
from response_generator import generate_response
from database import save_letter, init_db
from letter_numbering import get_next_letter_number

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in AUTH_USERS:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("🤖 Здравствуйте! Отправьте входящее письмо в PDF или изображении.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in AUTH_USERS:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return

    file = update.message.document or update.message.photo[-1]
    file_path = await file.get_file()
    file_bytes = await file_path.download_as_bytearray()

    info = process_file(file_bytes)
    number = get_next_letter_number()
    info["number"] = number

    save_letter(info)

    keyboard = [[InlineKeyboardButton("📤 Составить ответ", callback_data=f"reply_{number}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = f"""📩 Входящее письмо № {number}
Компания: {info['company']}
От: {info['sender_name']} ({info['email']})
Тема: {info['subject']}"""

    await update.message.reply_text(text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("reply_"):
        letter_number = data.replace("reply_", "")
        response_text = generate_response(letter_number)
        await query.edit_message_text(f"📤 Исходящее письмо:\n\n{response_text}")

if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()