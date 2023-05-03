import datetime


class Settings:
    class ChannelsFinder:
        parse_from = "excel"  # "html_file" or "site" or "excel"
        source = "channels_1.xlsx"  # https://tgstat.ru/politics
        safe_found_data_on_excel = False  # file name or False

    class ChannelsFilter:
        min_members_to_track = 0

    class ChannelsParser:
        api_id = 28026650
        api_hash = "1cffcc4372876df5819b84dd1f79a635"
        date_from = datetime.datetime(2023, 1, 1, 0, 0, 0)
        date_to = datetime.datetime(2023, 5, 2, 0, 0, 0)

    class MessagesHandler:
        marker = [
            "суверенитет"
        ]

    safe_result_in = "result.csv"
    result_separator = ";"  # разделитель в результирующем файле
