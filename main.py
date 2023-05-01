from TGChannelsParser import TGChannelsParser
from TGChannelsFinder import TGChannelsFinder
from time import time


def main():
    startTime = time()
    TGChannelsParser.parse(
        TGChannelsFinder.get_channels()
    )
    print("time: ", time() - startTime)


if __name__ == "__main__":
    main()
