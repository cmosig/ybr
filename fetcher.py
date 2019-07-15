import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import storage as st


def fetch_latest_videotitles(channel_name="",series_regex=""):
    base_url = "https://www.youtube.com/user/<channel>/videos"
    
    if (channel_name == ""):
        #check entire series list
        to_fetch = st.get_series_asdict()
    elif (series_regex == ""):
        #check only of specific channel
        #TODO
        print("TODO")
    else:
        #check channel - series pair
        to_fetch = { series_regex : channel_name }

    for s_name,c_name in to_fetch.items():

        #fetch latest episodes
        url = base_url.replace("<channel>",c_name)
        channel_bs = BeautifulSoup(urllib.request.urlopen(url),"html.parser")
        video_elements = channel_bs.findAll("a", {"class":"yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"})
        video_titles = pd.Series(list(map(get_title,video_elements)))
        titles = video_titles[video_titles.apply(match_regex,args=(s_name,))].tolist()

        #find the latest episode for a given series-channel pair check if there are new episodes    
        current_latest = st.get_latest_episode_name(s_name,c_name)

        if (len(titles) == 0):
            continue
        if(current_latest == "" or titles[0] != current_latest):
            st.set_latest(titles[0],s_name,c_name)
        for i in range(len(titles)):
            #TODO also add URL
            #going through all found titles matching the given series-channel pair
            if(current_latest == ""):
                st.add_new_episode(titles[0])
                break
            if(titles[i] == current_latest):
                break
            else:
                st.add_new_episode(titles[i])
    

def get_title(element):
    return element.get("title")

def match_regex(title,regex):
    return bool(re.match(regex,title))

#print(fetch_latest_videotitles("EthosLab",r"Minecraft - Diversity 3 #[0..9]*"))
#print(fetch_latest_videotitles("EthosLab",r"Etho Plays Minecraft - Episode [0..9]*"))

