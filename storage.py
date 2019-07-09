import os
from os import path
import pandas as pd

def init_database():
    try:
        os.mkdir("./data")
    except:
        pass
    if (path.exists("data/new_episodes_list.csv") and path.exists("data/series.csv")):
        print("database files already exist")
    else:
        f = open("data/new_episodes_list.csv","w+")
        f.write("episode_name ; url \n")
        f.close
        h = open("data/series.csv","w+")
        h.write("series_name ; channel_name ; latest_watched\n")
        h.close

def open_nel():
    """returns dataframe object of new episodes list table"""
    return pd.read_csv("data/new_episodes_list.csv",names=["episode_name","url"],sep=";",header=0)

def open_series():
    """returns dataframe object of series table"""
    return pd.read_csv("data/series.csv",names=["series_name","channel_name","latest_watched"],sep=";",header=0)

def close_series(df):
    df.drop_duplicates().to_csv("data/series.csv",sep=";",header=["series_name","channel_name","latest_watched"],index=False)

def close_nel(df):
    df.drop_duplicates().to_csv("data/new_episodes_list.csv",sep=";",header=["episode_name","url"],index=False)

"""
def get_series_aslist():
    return open_series()["series_name"].tolist()
"""

def set_latest(latest,series,channel):
    #TODO
    ser = open_series()
    series_match = ser["series_name"] == series
    channel_match = ser["channel_name"] == channel
    b = list(map(all,zip(*[series_match,channel_match])))
    ser.loc[b] = { "series_name" :  series , "channel_name" : channel , "latest_watched" : latest }
    print(ser)
    close_series(ser)
    

def get_latest_episode_name(series,channel):
    ser = open_series()
    series_match = ser["series_name"] == series
    channel_match = ser["channel_name"] == channel
    latest = ser[list(map(all,zip(*[series_match,channel_match])))]["latest_watched"].tolist()
    if (pd.isna(latest[0])):
        return ""
    else:
        print(latest)
        return latest[0]

def add_new_episode(episode_name,url=""):
    try:
        nel = open("data/new_episodes_list.csv","a")
    except:
        print("Database inconsisent. Did you initialize it yet. consider --initDB")
    nel.write(episode_name + ";" + url + "\n")
    nel.close()


def get_series_asdict():
    ser = open_series()
    #ser = ser.drop(["latest_watched"],axis=1)
    return pd.Series(ser["channel_name"].values,index=ser["series_name"]).to_dict()

def get_channels_aslist():
    return open_channels()["channel_name"].tolist()

def get_nel_asdict():
    nel = open_nel()
    return pd.Series(nel["url"].values,index=nel["episode_name"]).to_dict()

def add_series(series_name,channel_name):
    try: 
        ser = open("data/series.csv","a")
    except:
        print("Database inconsisent. Did you initialize it yet. consider --initDB")
    ser.write(series_name + ";" + channel_name + ";" "\n")
    ser.close()

def remove_series(series_name,channel_name):
    ser = open_series()
    series_match = ser["series_name"] == series_name
    channel_match = ser["channel_name"] == channel_name
    ser = ser[[not a for a in list(map(all,zip(*[series_match,channel_match])))]]
    close_series(ser)

#init_database()

"""
add_series("temp1","temp2")
add_series("temp1","temp3")
add_series("temp1","temp9")
remove_series("temp1" ,"temp3")

temp = open_series()
print(temp)
df = pd.DataFrame({'channel_name': ['Raphael', 'Donatello'],'series_name': ['red', 'purple']})
print(df)
close_series(df)
"""

