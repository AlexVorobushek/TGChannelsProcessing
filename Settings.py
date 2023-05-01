import datetime


class Settings:
    class ChannelsFinder:
        parse_from = "html_file"  # "html_file" or "site" or "excel"
        source = "html.txt"  # https://tgstat.ru/politics
        safe_found_data_on_excel = "channels.xlsx"  # file name or False

    class ChannelsFilter:
        min_members_to_track = 2000

    class ChannelsParser:
        api_id = 29232452
        api_hash = "882ae83505e22099adf178785ba5c3b1"
        date_from = datetime.datetime(2023, 4, 15, 0, 0, 0)
        date_to = datetime.datetime(2023, 4, 30, 0, 0, 0)

    class MessagesHandler:
        marker = [
            "суверенитет"
        ]

    safe_result_in = "result.csv"
