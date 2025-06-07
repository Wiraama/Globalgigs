import asyncio, threading
from v1 import create_bot
from v1.views.bot_reply import run_loop

app = create_bot()

if __name__ == "__main__":
    threading.Thread(target=run_loop, name="bot-loop-thread", daemon=True).start()
    #app.run(port=5555, host='0.0.0.0')
