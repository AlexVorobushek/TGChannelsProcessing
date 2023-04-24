from Settings import Settings


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
    def process_all_data(channels_to_messages: dict):
        return dict(
            map(
                lambda item: (item[0], ParsedChannelsDataHandler.process_channel(item[1])),
                channels_to_messages.items()
            )
        )
