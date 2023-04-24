from pyrogram import Client
from Settings import Settings


class TGChannelsParser:
    @staticmethod
    async def parse(channels):
        tracked_messages = dict()
        async with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            for channel in channels:
                if await app.get_chat_members_count(channel) < Settings.ChannelsFilter.min_members_to_track: continue
                async for message in app.get_chat_history(channel, offset_date=Settings.ChannelsParser.date_to):
                    if message.date < Settings.ChannelsParser.date_from: break
                    if not message.text: continue
                    tracked_messages[channel] = tracked_messages.get(channel, []) + [message.text]
        return tracked_messages
