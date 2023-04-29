from Settings import Settings
from progress.bar import Bar


class ParsedChannelsDataHandler:
    @staticmethod
    def find_marker_in_message(message: str) -> int:
        result = 0
        for item in Settings.MessagesHandler.marker:
            result += message.lower().count(item)
        return result

    @staticmethod
    def process_channel(messages: list):
        return sum(map(ParsedChannelsDataHandler.find_marker_in_message, messages))

    @staticmethod
    def process_all_data(channel_and_messages_table: list) -> list:
        with Bar('process messages of channels', max=len(channel_and_messages_table), fill="-") as bar:
            for line in channel_and_messages_table:
                line["value"] = ParsedChannelsDataHandler.process_channel(line["messages"])
                del line["messages"]
                bar.next()

        return channel_and_messages_table

    @staticmethod
    def write_statistic():
        pass
