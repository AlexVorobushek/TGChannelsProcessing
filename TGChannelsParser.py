from pyrogram import Client
from Settings import Settings
from progress.bar import Bar
from DataHandler import DataHandler

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
    def calculateChannelValue(app, channel_dict: dict) -> int:
        value = 0
        try:
            for message in app.get_chat_history(channel_dict["channel_name"], offset_date=Settings.ChannelsParser.date_to):
                if message.date < Settings.ChannelsParser.date_from: break
                if text := TGChannelsParser.getTextFromMessage(message):
                    value += DataHandler.find_marker_in_message(text)
        except:
            value = "channel not found"

        return value

    @staticmethod
    def parse(channels) -> list:
        # clear file
        with open(Settings.safe_result_in, "w", encoding="utf-8") as result_file:
            result_file.write("")
        # parse and write result
        with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            with Bar('parse messages', max=len(channels), fill="-") as bar:
                for channel_dict in channels:
                    value = TGChannelsParser.calculateChannelValue(app, channel_dict)
                    with open(Settings.safe_result_in, "a", encoding="utf-8") as result_file:
                        result_file.write(", ".join(list(map(str, channel_dict.values())) + [str(value)])+"\n")
                    bar.next()

