from pyrogram import Client, filters
from itertools import cycle

# Import safe placeholder lists from data.py
from data import RAID, REPLYRAID, PORMS, MRAID, SRAID, CRAID

API_ID = 27093880
API_HASH = "03ab44fe40af4c9a87ebf9f866bddf4a"

SUDO_USERS = [8258688313]

bots = [
    {"name": "bot1", "bot_token": "8442959946:AAHO1CRCzwlU__9Rxem2rDX9bUNBA8UU5t4"},
    {"name": "bot2", "bot_token": "8317403381:AAHT61t2hMMV1quqUeI8Hin6C4SorY57fvs"},
]

# EXACT SAME STRUCTURE YOU USED BEFORE
COMMAND_MAP = {
    "raid": cycle(RAID),
    "replyraid": cycle(REPLYRAID),
    "porm": cycle(PORMS),
    "mraid": cycle(MRAID),
    "sraid": cycle(SRAID),
    "craid": cycle(CRAID)
}

clients = []

def get_target(message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.mention
    parts = message.text.split()
    if len(parts) >= 3:
        return parts[2]
    return None

def add_command(app, cmd):
    cycle_list = COMMAND_MAP[cmd]

    @app.on_message(filters.command(cmd, prefixes=".") & (filters.group | filters.private))
    def _(client, message):
        # Only SUDO can use
        if message.from_user.id not in SUDO_USERS:
            return
        
        parts = message.text.split()

        # .raid 10 @user
        if len(parts) < 2:
            return message.reply(f"Usage: .{cmd} <count> <reply/mention>")

        try:
            amount = int(parts[1])
        except:
            return message.reply("Enter a number.")

        target = get_target(message)
        if not target:
            return message.reply("Reply to someone or mention a username.")

        # MAIN LOOP (same as your old system)
        for _ in range(amount):
            message.reply(f"{target}\n\n{next(cycle_list)}")

# Basic ping command
def add_ping(app):
    @app.on_message(filters.command("ping", prefixes="/"))
    def _(client, message):
        message.reply("BLAZE BOT READY TO FUCK ✔")

# START ALL BOTS — EXACT LIKE BEFORE
for bot in bots:
    if not bot["bot_token"]:
        print(f"Skipping {bot['name']}, no token provided.")
        continue

    app = Client(
        bot["name"],
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot["bot_token"]
    )

    # Add all commands like before
    for cmd in COMMAND_MAP:
        add_command(app, cmd)

    add_ping(app)
    app.start()
    clients.append(app)

print("All bots running...")
import asyncio
asyncio.get_event_loop().run_forever()