import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd


def fetch_latest_videotitles(channel_name="",series_regex=""):
    """returns latest videos from channel optionally filtering for series"""
    base_url = "https://www.youtube.com/user/<channel>/videos"

    #TODO check all default

    url = base_url.replace("<channel>",channel_name)
    channel_bs = BeautifulSoup(urllib.request.urlopen(url),"html.parser")
    video_elements = channel_bs.findAll("a", {"class":"yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
    video_titles = pd.Series(list(map(get_title,video_elements)))
    titles = video_titles[video_titles.apply(match_regex,args=(series_regex,))].tolist()
    return titles

def get_title(element):
    return element.get("title")

def match_regex(title,regex):
    return bool(re.match(regex,title))

#print(fetch_latest_videotitles("EthosLab",r"Minecraft - Diversity 3 #[0..9]*"))
#print(fetch_latest_videotitles("EthosLab",r"Etho Plays Minecraft - Episode [0..9]*"))

