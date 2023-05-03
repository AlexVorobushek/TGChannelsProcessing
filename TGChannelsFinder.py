from Settings import Settings
from bs4 import BeautifulSoup
import requests
import pandas


class TGChannelsFinder:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    @staticmethod
    def get_html_code_from_site():
        page = requests.get(Settings.ChannelsFinder.source, headers=TGChannelsFinder.headers)
        return page.text

    @staticmethod
    def get_html_code_from_file():
        with open(Settings.ChannelsFinder.source, "r") as f:
            result = f.read()
        return result

    @staticmethod
    def get_channels_from_html(html):
        print("start parse html")
        result = []
        soup = BeautifulSoup(html, "html.parser")
        allBlocks = soup.findAll("div",
                                 class_="card card-body peer-item-box py-2 mb-2 mb-sm-3 border border-info-hover position-relative")
        for data in allBlocks:
            new_channel = {"channel_name": data.a.get("href").split("/")[-1],
                           "channel_title": data.a.div.div.div.div.text,
                           "channel_members_count": int(data.a.div.div.find("b").text.replace(" ", ""))}
            if new_channel["channel_members_count"] >= Settings.ChannelsFilter.min_members_to_track:
                result.append(new_channel)

        if Settings.ChannelsFinder.safe_found_data_on_excel:
            TGChannelsFinder.write_statistic_on_exel(result, Settings.ChannelsFinder.safe_found_data_on_excel)
        return result

    @staticmethod
    def get_channels_from_excel():
        data = pandas.read_excel(Settings.ChannelsFinder.source)
        result = []
        for line in data.values:
            new_channel = {"channel_name": line[2],
                           "channel_title": line[1],
                           "channel_members_count": line[3]}
            if new_channel["channel_members_count"] >= Settings.ChannelsFilter.min_members_to_track and new_channel["channel_name"][0]=="@":
                result.append(new_channel)
        return result

    @staticmethod
    def get_channels() -> list:
        # print(1)
        # return [{"channel_name": "podolyak_sumy",
        #                    "channel_title": "f",
        #                    "channel_members_count": "line[3]"}]
        # print(2)
        result = []
        if Settings.ChannelsFinder.parse_from == "html_file":
            result = TGChannelsFinder.get_channels_from_html(TGChannelsFinder.get_html_code_from_file())
        if Settings.ChannelsFinder.parse_from == "site":
            result = TGChannelsFinder.get_channels_from_html(TGChannelsFinder.get_html_code_from_site())
        if Settings.ChannelsFinder.parse_from == "excel":
            result = TGChannelsFinder.get_channels_from_excel()
        print("i have channels")
        return result

    @staticmethod
    def write_statistic_on_exel(table, filename):
        titles = []
        links = []
        members = []

        for line in table:
            link, title, member_count = line.values()
            titles.append(title)
            links.append(link)
            members.append(member_count)

        df = pandas.DataFrame({
            "title": titles,
            "link": links,
            "members": members
        })
        df.to_excel(filename)


if __name__ == "__main__":
    print(TGChannelsFinder.get_channels())
