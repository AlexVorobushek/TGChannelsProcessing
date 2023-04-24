import asyncio
from TGChannelsParser import TGChannelsParser
from TGChannelsFinder import TGChannelsFinder


def main():
    print(
        asyncio.run(
            TGChannelsParser.parse(
                TGChannelsFinder.get_channels()
            )
        )
    )
    

if __name__=="__main__":
    main()
