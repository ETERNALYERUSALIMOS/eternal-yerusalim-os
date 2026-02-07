import telebot
TOKEN = "8277898902:AAESNlZmKD9D7Bkzxe_PcbIbDbAfJiCdz5w"
bot = telebot.TeleBot(TOKEN)
print("TOKEN OK")

avito = "https://www.avito.ru/brands/bestparfum"
promo = f"🧴 BESTPARFUM! Avito: {avito} TG: t.me/BestParfum1"

@bot.message_handler(commands=['test'])
def test_msg(message):
    bot.reply_to(message, promo)

bot.polling()
