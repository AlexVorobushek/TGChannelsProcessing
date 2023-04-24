import asyncio
from TGChannelsParser import TGChannelsParser
from TGChannelsFinder import TGChannelsFinder
from ParsedChannelsDataHandler import ParsedChannelsDataHandler


def main():
    print(
        ParsedChannelsDataHandler.process_all_data(
            asyncio.run(
                TGChannelsParser.parse(
                    TGChannelsFinder.get_channels()
                )
            )
        )
    )


if __name__ == "__main__":
    main()
