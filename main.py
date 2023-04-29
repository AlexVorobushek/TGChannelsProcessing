import asyncio

import Channel
from TGChannelsParser import TGChannelsParser
from TGChannelsFinder import TGChannelsFinder
from ParsedChannelsDataHandler import ParsedChannelsDataHandler
from time import time


def main():
    startTime = time()
    channel_to_value = ParsedChannelsDataHandler.process_all_data(
        TGChannelsParser.parse(
            TGChannelsFinder.get_channels()
        )
    )
    for channel, value in sorted(channel_to_value.items(), key=lambda x: -x[1]):
        print(f"{channel}: {value}")
    print("time: ", time() - startTime)


if __name__ == "__main__":
    main()
