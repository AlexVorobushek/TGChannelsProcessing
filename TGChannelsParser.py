import pyrogram.errors.exceptions.all
from pyrogram import Client
from Settings import Settings
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
    def parceChannel(app, channel_dict: dict) -> dict:
        channel_dict["messages"] = []
        for message in app.get_chat_history(channel_dict["channel_name"], offset_date=Settings.ChannelsParser.date_to):
            if message.date < Settings.ChannelsParser.date_from: break
            if text := TGChannelsParser.getTextFromMessage(message):
                channel_dict["messages"].append(text)
        return channel_dict

    # @staticmethod
    # def channelsFilter(channels: list) -> list:
    #     return list(
    #         filter(
    #             lambda channel: channel.members_count >= Settings.ChannelsFilter.min_members_to_track,
    #             channels
    #         )
    #     )

    # @staticmethod
    # def reformatChannelsList(app, channel_names: list) -> list:
    #     # for any item in channels list write some Channel object with data
    #     result = []
    #     with Bar('parse channels data', max=len(channel_names), fill="-") as bar:
    #         for channel_name in channel_names:
    #             chat = app.get_chat(channel_name)
    #             result.append(Channel(chat.username, chat.title, chat.members_count))
    #
    #             bar.next()
    #             if not bar.index % 2: sleep(2)
    #
    #     return result

    @staticmethod
    def parse(channels) -> list:
        import warnings
        warnings.filterwarnings('ignore')

        result = []

        with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            with Bar('parse messages', max=len(channels), fill="-") as bar:
                for channel_dict in channels:
                    try:
                        result.append(TGChannelsParser.parceChannel(app, channel_dict))
                    except pyrogram.errors.exceptions.RPCError:
                        pass
                    bar.next()

        return result
