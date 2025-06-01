from flask import Blueprint, request, jsonify
from telegram import Update
from v1.views.bot_reply import bot_app, loop
import asyncio, threading

bot = Blueprint('bot', __name__)

@bot.route("/")
def home():
    return jsonify({"sucess": "home page"})
    
loop = asyncio.new_event_loop()

def start_loop():
    asyncio.set_event_loop(loop)
    loop.run_forever()

threading.Thread(target=start_loop, daemon=True).start()

@bot.route("/telegram", methods=["POST"]) 
def telegram_webhook():
    try:
        json_data = request.get_json()
        update = Update.de_json(json_data, bot_app.bot)
        asyncio.run_coroutine_threadsafe(bot_app.process_update(update), loop)
        return jsonify({"status": "sucess"})
    except Exception as e:
        print(f"Error : {e}")
        return jsonify({"error": "Error"})
