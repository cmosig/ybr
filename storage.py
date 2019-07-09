import os
import pandas as pd

def init_database():
    try:
        os.mkdir("./data")
    except:
        pass
    open("data/new_episodes_list.csv","w+").close()
    open("data/channels.csv","w+").close()
    open("data/series.csv","w+").close()



