import datetime


class Settings:
    class ChannelsFinder:
        parse_from = "site"  # "html_file" or "site" or "excel"
        source = "https://tgstat.ru/politics"  # https://tgstat.ru/politics
        safe_found_data_on_excel = "channels.xlsx"  # file name or False

    class ChannelsFilter:
        min_members_to_track = 0

    class ChannelsParser:
        api_id = 29232452
        api_hash = "882ae83505e22099adf178785ba5c3b1" # not active
        date_from = datetime.datetime(2023, 1, 1, 0, 0, 0)
        date_to = datetime.datetime(2023, 5, 2, 0, 0, 0)

    class MessagesHandler:
        markers = {
            "marker 1": r"отечеств.[^н][а-я]*"
        }

    safe_result_in = "result.csv"
    result_separator = ";"  # разделитель в результирующем файле
