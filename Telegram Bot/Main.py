from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder, MessageHandler, CommandHandler,
    filters, ContextTypes
)

BOT_TOKEN = '7726484416:AAG1nnF9NeY3V16ag_RpJpeDh9oomx6VkIE'
OWNER_ID = 835641047

# /start команда з видаленням клавіатури
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! 👋\n\nЩо б ти сам(а) хотів(ла) щоб додалося в нашому магазині? 🤔 ",
        reply_markup=ReplyKeyboardRemove()
    )

# Обробка повідомлень
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    message_text = update.message.text
    sender_name = f"{user.first_name} (@{user.username})" if user.username else user.first_name

    text = f"📬 Нова пропозиція від {sender_name}:\n\n{message_text}"

    await context.bot.send_message(chat_id=OWNER_ID, text=text)
    await update.message.reply_text("✅ Ваше повідомлення було успішно відправлено!")

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Бот працює без кнопки ✅")
    app.run_polling()
