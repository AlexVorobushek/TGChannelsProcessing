from TGChannelsParser import TGChannelsParser
from TGChannelsFinder import TGChannelsFinder
from ParsedChannelsDataHandler import ParsedChannelsDataHandler
from time import time


def main():
    startTime = time()
    table = ParsedChannelsDataHandler.process_all_data(
        TGChannelsParser.parse(
            TGChannelsFinder.get_channels()
        )
    )
    for line in sorted(table, key=lambda x: -x["value"]):
        print(line)
    print("time: ", time() - startTime)


if __name__ == "__main__":
    main()
