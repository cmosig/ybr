import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import storage as st
from tqdm import tqdm

channel_cache = {}

def fetch_latest_videotitles(channel_name="",series_regex=""):
    url_yt = "https://www.youtube.com"
    
    if (channel_name == ""):
        #check entire series list
        to_fetch = st.get_series_as_tuples()
    elif (series_regex == ""):
        #check only of specific channel
        print("TODO")
    else:
        #check channel - series pair
        to_fetch = [(series_regex , channel_name)]

    for s_name,c_name in tqdm(to_fetch):
        #fetch latest episodes
        channel_bs = get_channel_bs(c_name)
        video_elements = channel_bs.findAll("a", {"class":"yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
        video_titles = list(map(get_title,video_elements))
        video_urls = list(map(get_url,video_elements))
        videos = pd.DataFrame.from_dict({"title":video_titles,"url":video_urls})
        videos = videos[videos["title"].apply(match_regex,args=(s_name,))]
        videos = [tuple(x) for x in videos.values]
        #titles = video_titles[video_titles.apply(match_regex,args=(s_name,))].tolist()

        #find the latest episode for a given series-channel pair check if there are new episodes    
        current_latest = st.get_latest_episode_name(s_name,c_name)

        if (len(videos) == 0):
            continue
        if(current_latest == "" or videos[0][0] != current_latest):
            st.set_latest(videos[0][0],s_name,c_name)
        for i in range(len(videos)):
            #going through all found videos matching the given series-channel pair
            if(current_latest == ""):
                st.add_new_episode(videos[0][0],url_yt + videos[0][1])
                break
            if(videos[i][0] == current_latest):
                break
            else:
                st.add_new_episode(videos[i][0],url_yt + videos[i][1])

def get_channel_bs(channel_name):
    #lookup in cache
    if (not channel_name in channel_cache):
        url_videos = "https://www.youtube.com/user/<channel>/videos"
        url = url_videos.replace("<channel>",channel_name)
        channel_cache[channel_name] = BeautifulSoup(urllib.request.urlopen(url),"html.parser")
    return channel_cache[channel_name]
    

def get_title(element):
    return element.get("title")

def get_url(element):
    return element.get("href")

def match_regex(title,regex):
    return bool(re.match(regex,title))

#print(fetch_latest_videotitles("EthosLab",r"Minecraft - Diversity 3 #[0..9]*"))
#print(fetch_latest_videotitles("EthosLab",r"Etho Plays Minecraft - Episode [0..9]*"))

