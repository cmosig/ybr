import os
import traceback
from os import path
import pandas as pd

data_path = "/home/hacker101/projects/ybr/data/"

def init_database():
    try:
        os.mkdir("./data")
    except:
        pass
    if (path.exists(data_path + "new_episodes_list.csv") and path.exists(data_path + "series.csv")):
        print("database files already exist")
    else:
        f = open(data_path + "new_episodes_list.csv","w+")
        f.write("episode_name ; url \n")
        f.close
        h = open(data_path + "series.csv","w+")
        h.write("series_name ; channel_name ; latest_watched\n")
        h.close

def open_nel():
    """returns dataframe object of new episodes list table"""
    return pd.read_csv(data_path + "new_episodes_list.csv",names=["episode_name","url"],sep=";",header=0)

def open_series():
    """returns dataframe object of series table"""
    return pd.read_csv(data_path + "series.csv",names=["series_name","channel_name","latest_watched"],sep=";",header=0)

def close_series(df):
    df.drop_duplicates().to_csv(data_path + "series.csv",sep=";",header=["series_name","channel_name","latest_watched"],index=False)

def close_nel(df):
    df.drop_duplicates().to_csv(data_path + "new_episodes_list.csv",sep=";",header=["episode_name","url"],index=False)

"""
def get_series_aslist():
    return open_series()["series_name"].tolist()
"""

def remove_nel(index):
    nel = open_nel()
    nel = nel.drop([index])
    close_nel(nel)

def set_latest(latest,series,channel):
    """sets the latest episode of a series-channel pair"""
    ser = open_series()
    #locating channel-series pair in dataframe and replacing latest watched episode
    ser.loc[(ser["series_name"]==series) & (ser["channel_name"]==channel),"latest_watched"] = latest
    close_series(ser)
    

def get_latest_episode_name(series,channel):
    ser = open_series()
    series_match = ser["series_name"] == series
    channel_match = ser["channel_name"] == channel
    latest = ser[list(map(all,zip(*[series_match,channel_match])))]["latest_watched"].tolist()
    if (pd.isna(latest[0])):
        return ""
    else:
        return latest[0]

def add_new_episode(episode_name,url=""):
    try:
        nel = open(data_path + "new_episodes_list.csv","a")
    except:
        print("Database inconsisent. Did you initialize it yet. consider --initDB")
        traceback.print_exc()
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
        ser = open(data_path + "series.csv","a")
    except:
        print("Database inconsisent. Did you initialize it yet. consider --initDB")
        traceback.print_exc()
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

