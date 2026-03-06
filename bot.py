from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 أهلاً بك في أكاديمية المهندس التعليمية\n"
        "بإشراف المهندس نوار عادل\n\n"
        "أنا مدرس كيمياء السادس العلمي.\n"
        "اكتب أي سؤال عن الفصل الأول وسأشرح لك ببساطة."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 شرح مبسط من الفصل الأول (تركيب الذرة):\n\n"
        "الذرة تتكون من:\n"
        "1- نواة تحتوي على البروتونات والنيوترونات.\n"
        "2- إلكترونات تدور حول النواة.\n\n"
        "العدد الذري = عدد البروتونات\n"
        "العدد الكتلي = عدد البروتونات + النيوترونات\n\n"
        "استمر بالسؤال وسأساعدك أكثر."
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
