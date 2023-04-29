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
    def process_all_data(channels_to_messages: dict) -> dict:
        with Bar('process messages of channels', max=len(channels_to_messages), fill="-") as bar:
            for channel, messages in channels_to_messages.items():
                channels_to_messages[channel] = ParsedChannelsDataHandler.process_channel(messages)
                bar.next()

        return channels_to_messages

    @staticmethod
    def write_statistic():
        pass
