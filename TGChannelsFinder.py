from Settings import Settings
from bs4 import BeautifulSoup
import requests


class TGChannelsFinder:
    url = 'https://tgstat.ru/politics'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    @staticmethod
    def get_html_code():
        page = requests.get(TGChannelsFinder.url, headers=TGChannelsFinder.headers)
        return page.text

    @staticmethod
    def get_channels() -> list:
        result = []
        soup = BeautifulSoup(TGChannelsFinder.get_html_code(), "html.parser")
        allBlocks = soup.findAll("div", class_="card card-body peer-item-box py-2 mb-2 mb-sm-3 border border-info-hover position-relative")
        for data in allBlocks:
            new_channel = {"channel_name": data.a.get("href").split("/")[-1],
                           "channel_title": data.a.div.div.div.div.text,
                           "channel_members_count": int(data.a.div.div.find("b").text.replace(" ", ""))}
            if new_channel["channel_members_count"] >= Settings.ChannelsFilter.min_members_to_track:
                result.append(new_channel)
        return result
