from pyrogram import Client
from Settings import Settings
from progress.bar import Bar


class TGChannelsParser:
    @staticmethod
    def getTextFromMessage(message):
        if message.text:
            return message.text
        elif message.caption:
            return message.caption
        elif message.poll:
            return message.poll.question + " " + " ".join([answer.text for answer in message.poll.options])
    @staticmethod
    async def parse(channels):
        tracked_messages = dict()
        async with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            bar = Bar('Channels', max=len(channels), fill="*")
            for channel in channels:
                if await app.get_chat_members_count(channel) < Settings.ChannelsFilter.min_members_to_track: continue
                async for message in app.get_chat_history(channel, offset_date=Settings.ChannelsParser.date_to):
                    if message.date < Settings.ChannelsParser.date_from: break
                    if text:=TGChannelsParser.getTextFromMessage(message):
                        tracked_messages[channel] = tracked_messages.get(channel, []) + [text]
                bar.next()
            bar.finish()
        return tracked_messages
