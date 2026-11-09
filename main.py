import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@simogoldsignal"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحبا بيك فـ SIMO GOLD AI\n\n"
        "🟡 كتوصلك إشارات الذهب XAUUSD هنا و فالقناة\n"
        "@simogoldsignal\n\n"
        "الأوامر:\n"
        "/signal - جيب إشارة دابا"
    )

def make_signal():
    direction = random.choice(["BUY 🟢", "SELL 🔴"])
    price = random.uniform(2640, 2680)
    if direction.startswith("BUY"):
        tp1, tp2, sl = price+8, price+15, price-10
    else:
        tp1, tp2, sl = price-8, price-15, price+10
    return f"🟡 SIMO GOLD SIGNAL 🟡\n\nPair: XAUUSD\nSignal: {direction}\nEntry: {price:.2f}\nTP1: {tp1:.2f}\nTP2: {tp2:.2f}\nSL: {sl:.2f}\n\n@simogoldsignal"

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = make_signal()
    await update.message.reply_text(msg)
    await context.bot.send_message(chat_id=CHANNEL, text=msg)

async def auto_signal(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHANNEL, text=make_signal())

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.job_queue.run_repeating(auto_signal, interval=3600, first=10)
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
