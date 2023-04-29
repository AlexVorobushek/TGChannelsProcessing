from pyrogram import Client
from Settings import Settings
from Channel import Channel
from progress.bar import Bar
from time import sleep


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
    def parceChannelMessages(app, channel_name: str) -> list:
        result = []
        for message in app.get_chat_history(channel_name, offset_date=Settings.ChannelsParser.date_to):
            if message.date < Settings.ChannelsParser.date_from: break
            if text := TGChannelsParser.getTextFromMessage(message):
                result.append(text)
        return result

    @staticmethod
    def channelsFilter(channels: list) -> list:
        return list(
            filter(
                lambda channel: channel.members_count >= Settings.ChannelsFilter.min_members_to_track,
                channels
            )
        )

    @staticmethod
    def reformatChannelsList(app, channel_names: list) -> list:
        # for any item in channels list write some Channel object with data
        result = []
        with Bar('parse channels data', max=len(channel_names), fill="-") as bar:
            for channel_name in channel_names:
                chat = app.get_chat(channel_name)
                result.append(Channel(chat.username, chat.title, chat.members_count))

                bar.next()
                if not bar.index % 2: sleep(2)

        return result

    @staticmethod
    def parse(channels_names) -> dict:
        result = dict()

        with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            channels = TGChannelsParser.channelsFilter(TGChannelsParser.reformatChannelsList(app, channels_names))
            with Bar('parse messages', max=len(channels), fill="-") as bar:
                for channel in channels:
                    result[channel] = TGChannelsParser.parceChannelMessages(app, channel.username)

                    bar.next()
                    if not bar.index % 5: sleep(3)

        return result
