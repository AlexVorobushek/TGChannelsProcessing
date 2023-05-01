from Settings import Settings


class DataHandler:
    @staticmethod
    def find_marker_in_message(message: str) -> int:
        result = 0
        for item in Settings.MessagesHandler.marker:
            result += message.lower().count(item)
        return result
