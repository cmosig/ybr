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
        h.write("series_name ; channel_name \n")
        h.close

def open_nel():
    """returns dataframe object of new episodes list table"""
    return pd.read_csv("data/new_episodes_list.csv",names=["episode_name","url"],sep=";",header=0)

def open_series():
    """returns dataframe object of series table"""
    return pd.read_csv("data/series.csv",names=["series_name","channel_name"],sep=";",header=0)

def get_series_aslist():
    return open_series()["series_name"].tolist()

def get_series_asdict():
    ser = open_ser()
    return pd.Series(ser["url"].values,index=ser["episode_name"]).to_dict()

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
    ser.write(series_name + ";" + channel_name + "\n")
    ser.close()

init_database()
add_series("tester","chan")
add_series("tester","chan")
print(open_series())

