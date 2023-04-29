import re
from pyrogram import Client
from Settings import Settings


class TGChannelsFinder:
    @staticmethod
    def get_html_code():
        with open("html.txt", "r", encoding="utf_8_sig") as file:
            result = file.read()
        return result

    @staticmethod
    def get_channels() -> list:
        # return ["fedorovgd"]
        result = list(
            map(
                lambda string: string[2:-1], re.findall(f"/@[^\"]+\"", TGChannelsFinder.get_html_code())
            )
        )
        return result
