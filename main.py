from telethon import TelegramClient, events
from flask import Flask
import threading
import os

# Dados da API (preencha com os seus)
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
palavras_chave = ["cupom mercado livre", "firetv", "fire tv"]

# Nome da sessão (será salvo como um arquivo .session no replit)
client = TelegramClient('monitor_bot_session', api_id, api_hash)


# Evento de nova mensagem
@client.on(events.NewMessage)
async def handler(event):
    texto = event.raw_text.lower()
    if any(p in texto for p in palavras_chave):
        # Envia mensagem para você mesmo
        await client.send_message(
            'me', f"🔔 Palavra-chave encontrada:\n\n{event.raw_text}")


# Web server para manter o Replit vivo
app = Flask('')


@app.route('/')
def home():
    return "Bot está rodando!"


def run_flask():
    app.run(host='0.0.0.0', port=8080)


# Iniciar o Flask em thread separada
threading.Thread(target=run_flask).start()

# Iniciar o Telegram client
with client:
    print("Bot está rodando...")
    client.run_until_disconnected()
