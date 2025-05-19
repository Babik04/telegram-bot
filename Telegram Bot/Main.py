from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, MessageHandler, CommandHandler,
    filters, ContextTypes
)

# Твій токен бота
BOT_TOKEN = '8186449348:AAFzynzScg5PgxF3d7TXjp_Nh8rmJX5PoJU'

# Твій Telegram ID
OWNER_ID = 835641047


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! 👋\n\n Натисни кнопку нижче або просто напиши, що б ти хотів бачити в магазині 🍞",
        reply_markup=keyboard
    )


# Обробка повідомлень
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    message_text = update.message.text
    sender_name = f"{user.first_name} (@{user.username})" if user.username else user.first_name

    text = f"📬 Нова пропозиція від {sender_name}:\n\n{message_text}"

    await context.bot.send_message(chat_id=OWNER_ID, text=text)
    await update.message.reply_text("Дякую, ваше повідомлення надіслано! ✅")


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Бот із кнопкою працює! ✅")
    app.run_polling()

