import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

# الحصول على المفاتيح من Environment Variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# إنشاء عميل OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# إعداد سجل التشغيل
logging.basicConfig(level=logging.INFO)

# دالة البداية / start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🔥 أهلاً بك في أكاديمية نوار الذكية\n"
"أنا مدربك في كيمياء السادس العلمي.\n\n"
"اسألني أي سؤال عن الفصل الأول وسأشرح لك بأسلوب شبابي وحازم 😉"
)

# دالة الرد على أي رسالة من الطالب
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
user_message = update.message.text

# إنشاء الرد من GPT-4o-mini
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "أنت مدرس كيمياء عراقي متخصص بالصف السادس العلمي، تشرح بأسلوب شبابي، حازم، مشوق، ومبسط جداً."},
{"role": "user", "content": user_message}
]
)

ai_reply = response.choices[0].message.content
await update.message.reply_text(ai_reply)

# الدالة الرئيسية لتشغيل البوت
def main():
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# إضافة الHandlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# تشغيل البوت
app.run_polling()

# تشغيل البوت عند تنفيذ الملف مباشرة
if __name__ == "__main__":
main()
