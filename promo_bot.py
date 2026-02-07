import requests
avito = "https://www.avito.ru/brands/bestparfum"
tg = "t.me/BestParfum1"
msg = f"🧴 BESTPARFUM масляные духи премиум!Avito: {avito}TG: {tg}#масляныедухи"

# Твои 200 групп (добавь)
groups = ["@parfum_chat", "@avito_rf"]  # Вставь список

for g in groups:
    requests.post("https://api.telegram.org/bot[ТОКЕН]/sendMessage", data={"chat_id": g, "text": msg})
print("Коллапс отправлен!")
