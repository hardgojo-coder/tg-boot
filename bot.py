from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8621215028:AAENtTWCyV6DLzhpVpdJbKWwdZsQ_7Shq7k"

def convert_link(text: str) -> str:
    if "instagram.com/reel/" in text:
        # remove www if exists, then add kk.
        text = text.replace("www.", "")
        text = text.replace("https://", "https://kk.")
        text = text.replace("http://", "http://kk.")
        return text
    return None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    new_link = convert_link(text)

    if new_link:
        await update.message.reply_text(new_link)
    else:
        await update.message.reply_text("Send Instagram REEL link only.")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
