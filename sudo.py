from pyrogram import Client, filters

API_ID = 27093880
API_HASH = "03ab44fe40af4c9a87ebf9f866bddf4a"
SUDO_USERS = [8258688313]

bots = [
    {"name": "bot1", "bot_token": "8442959946:AAHO1CRCzwlU__9Rxem2rDX9bUNBA8UU5t4"},
    {"name": "bot2", "bot_token": "8317403381:AAHT61t2hMMV1quqUeI8Hin6C4SorY57fvs"},
]

clients = []

def add_basic_commands(app):

    @app.on_message(filters.command("start"))
    def start_cmd(_, message):
        message.reply("Bot running safely ✔")

    @app.on_message(filters.command("ping"))
    def ping_cmd(_, message):
        message.reply("Pong! ✔")

for bot in bots:
    if not bot["bot_token"]:
        print(f"Skipping {bot['name']}: No token")
        continue

    app = Client(
        name=bot["name"],
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot["bot_token"]
    )

    add_basic_commands(app)
    app.start()
    clients.append(app)

print("All bots started ✔")

import asyncio
asyncio.get_event_loop().run_forever()
