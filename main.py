from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Разрешаем веб-странице с GitHub делать запросы к нашему Python-серверу
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Вставь токен твоего бота из @BotFather
BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"

@app.post("/get-invoice")
def get_invoice():
    # Запрос к Telegram Bot API для генерации ссылки на оплату
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/createInvoiceLink"
    
    payload = {
        "title": "VIP-статус",
        "description": "Покупка VIP на сервере Minecraft",
        "payload": "vip_30_days",
        "currency": "XTR",  # XTR — это Telegram Stars
        "prices": [{"label": "VIP 30 дней", "amount": 50}],  # Цена: 50 Звёзд
        "provider_token": ""  # Для XTR обязательно оставляем пустым!
    }

    response = requests.post(url, json=payload).json()
    
    if response.get("ok"):
        return {"link": response["result"]}
    return {"error": "Failed to create invoice"}
