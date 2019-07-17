import storage as st
from tabulate import tabulate as tab

def print_new_episodes():
    """prints out all episodes from new_episodes_list"""
    print("")
    print("NEW EPISODES:")
    print(tab(st.open_nel(),headers="keys", tablefmt="psql"))

def print_pairs():
    """prints out all pairs from series"""
    print("")
    print("CHANNEL - SERIES CONFIGURATIONS:")
    print(tab(st.open_series(),headers="keys", tablefmt="psql"))
