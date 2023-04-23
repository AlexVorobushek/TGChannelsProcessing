import asyncio
from pyrogram import Client
import datetime

API_ID = 29232452
API_HASH = "882ae83505e22099adf178785ba5c3b1"

CHANNELS = [
    "safffds",
    "alalalllllla"
]

DATE_FROM = datetime.datetime(2023, 4, 22, 0,  0, 0)
DATE_TO   = datetime.datetime(2023, 4, 22, 21, 4, 0)

MIN_MEMBERS_COUNT_TO_TRACK = 2

async def get_tracked_messages():
    tracked_messages = dict()
    async with Client("my_account", API_ID, API_HASH) as app:
        for channel in CHANNELS:
            if await app.get_chat_members_count(channel) < MIN_MEMBERS_COUNT_TO_TRACK: continue
            async for message in app.get_chat_history(channel, offset_date=DATE_TO):
                if message.date < DATE_FROM: break
                tracked_messages[channel] = tracked_messages.get(channel, []) + [message.text]
    return tracked_messages

def main():
    print(asyncio.run(get_tracked_messages()))
    

if __name__=="__main__":
    main()
