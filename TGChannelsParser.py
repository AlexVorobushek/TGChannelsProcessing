import time

from pyrogram import Client
from Settings import Settings
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
            for message in app.get_chat_history(channel_dict["channel_name"],
                                                offset_date=Settings.ChannelsParser.date_to):
                if message.date < Settings.ChannelsParser.date_from: break
                if text := TGChannelsParser.getTextFromMessage(message):
                    value += DataHandler.find_marker_in_message(text)
        except Exception as e:
            print(e)
            if "400" in str(e):
                value = "приватный"
            elif "420" in str(e):
                seconds = int(sum(i for i in str(e) if i.isdigit())[3:])+1
                print(f"i'l sleep {seconds}s")
                time.sleep(seconds)
                return TGChannelsParser.calculateChannelValue(app, channel_dict)
            else:
                value = str(e).replace(";", "")

        return value

    @staticmethod
    def parse(channels):
        # clear file
        with open(Settings.safe_result_in, "w", encoding="utf-8") as result_file:
            result_file.write("")
        # parse and write result
        channels_count = len(channels)
        i = 0
        with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            for channel_dict in channels:
                value = TGChannelsParser.calculateChannelValue(app, channel_dict)
                with open(Settings.safe_result_in, "a", encoding="utf-8") as result_file:
                    result_file.write(
                        Settings.result_separator.join(list(map(str, channel_dict.values())) + [str(value)]) + "\n")
                i += 1
                print(f"{i}/{channels_count}")


if __name__ == "__main__":
    TGChannelsParser.parse([({
        "channel_name": "nationkurs",
        "channel_title": "line[1]",
        "channel_members_count": 1
    })])
