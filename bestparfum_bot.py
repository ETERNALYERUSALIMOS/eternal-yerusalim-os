from telegram import Bot
from telegram.ext import Application, CommandHandler
import asyncio

TOKEN = "8277898902:AAESNlZmKD9D7Bkzxe_PcbIbDbAfJiCdz5w"
avito = "https://www.avito.ru/brands/bestparfum"
tg = "t.me/BestParfum1"

promo_msg = """🧴 BESTPARFUM — масляные духи премиум! Стойкость 12ч+ 🔥
Цены от 300₽. Доставка РФ!

Avito: https://www.avito.ru/brands/bestparfum
Telegram: t.me/BestParfum1

#масляныедухи #арабскиедухи"""

async def start(update, context):
    await update.message.reply_text("🧴 BESTPARFUM Bot активирован! /promo — рассылка")

async def promo(update, context):
    await update.message.reply_text(promo_msg)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("promo", promo))

print("🚀 BESTPARFUM Bot v2 запущен! Найди BestParfumBot → /start")
app.run_polling()
