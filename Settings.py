import datetime


class Settings:
    class ChannelsFinder:
        pass

    class ChannelsFilter:
        min_members_to_track = 2

    class ChannelsParser:
        api_id = 29232452
        api_hash = "882ae83505e22099adf178785ba5c3b1"
        date_from = datetime.datetime(2023, 4, 22, 0, 0, 0)
        date_to = datetime.datetime(2023, 4, 22, 21, 4, 0)

    class MessagesHandler:
        marker = "sf"
