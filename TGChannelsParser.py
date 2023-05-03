import time

from pyrogram import Client
from Settings import Settings
from DataHandler import DataHandler, FindMarkersResult


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
    def getChannelMessages(app, channel_name):
        try:
            for message in app.get_chat_history(channel_name, offset_date=Settings.ChannelsParser.date_to):
                if message.date < Settings.ChannelsParser.date_from: break
                yield message
        except Exception as e:
            print(e)
            if "400" in str(e):
                print(channel_name, "не удалось зайти")
            elif "420" in str(e):
                seconds = int(sum(i for i in str(e) if i.isdigit())[3:]) + 1
                print(f"i'l sleep {seconds}s")
                time.sleep(seconds)
                for message in TGChannelsParser.getChannelMessages(app, channel_name): yield message
            else:
                print(e)

    @staticmethod
    def calculateChannel(app, channel_name: str) -> FindMarkersResult:
        result = FindMarkersResult()
        for message in TGChannelsParser.getChannelMessages(app, channel_name):
            if text := TGChannelsParser.getTextFromMessage(message):
                result += DataHandler.find_markers_in_message(text)
        return result

    @staticmethod
    def parse(channels):
        # clear result file
        with open(Settings.safe_result_in, "w", encoding="utf-8") as result_file:
            result_file.write("")

        # parse and write result

        channels_count = len(channels)
        channels_watched = 0

        with Client("my_account", Settings.ChannelsParser.api_id, Settings.ChannelsParser.api_hash) as app:
            for channel_data in channels:
                channel_result = TGChannelsParser.calculateChannel(app, channel_data["channel_name"])
                with open(Settings.safe_result_in, "a", encoding="utf-8") as result_file:
                    result_file.write(Settings.result_separator.join(
                        list(map(str, channel_data.values())) + list(map(str, channel_result.values()))) + "\n")

                channels_watched += 1
                print(f"{channels_watched}/{channels_count}")


if __name__ == "__main__":
    TGChannelsParser.parse([({
        "channel_name": "nationkurs",
        "channel_title": "line[1]",
        "channel_members_count": 1
    })])
