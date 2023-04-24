from Settings import Settings


class ParsedChannelsDataHandler:
    @staticmethod
    def process_channel(messages: list) -> int:
        return sum(map(lambda text: text.lower().count(Settings.MessagesHandler.marker), messages))

    @staticmethod
    def process_all_data(channels_to_messages: dict):
        return dict(
            map(
                lambda item: (item[0], ParsedChannelsDataHandler.process_channel(item[1])),
                channels_to_messages.items()
            )
        )
