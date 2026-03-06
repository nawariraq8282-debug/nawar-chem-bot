import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 أهلاً بك في أكاديمية المهندس التعليمية\n"
        "بإشراف المهندس نوار عادل\n\n"
        "أنا مدرس كيمياء السادس العلمي.\n"
        "اسألني أي سؤال عن أي فصل من منهج الكيمياء للصف السادس العلمي العراقي، "
        "وسأشرح لك بأسلوب شبابي، حازم، ومبسط 😉"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "أنت مدرس كيمياء للصف السادس العلمي العراقي، تشرح بأسلوب شبابي، حازم، مشوق، ومبسط جداً."},
            {"role": "user", "content": user_message}
        ]
    )

    ai_reply = response.choices[0].message.content
    await update.message.reply_text(ai_reply)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
