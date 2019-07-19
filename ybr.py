import sys
import argparse
import fetcher as f
import storage as st
import userinterface as us

def main():
    """reading command line arguements and calling respective methods"""
    init_argument_parser()

def init_argument_parser():
    parser = argparse.ArgumentParser(description="A better YouTube recommendation service.")
    parser.add_argument("-f","--fetch",action="store_const",const=f.fetch_latest_videotitles,dest="fetch",help="fetch latest videos")
    parser.add_argument("-s","--series",const="series",help="specify series to work on",nargs="?",default="")
    parser.add_argument("-c","--channel",const="channel",help="specify channel to work on",nargs="?",default="")
    parser.add_argument("--initDB",action="store_const",const=st.init_database,dest="initDB",help="initial init of database. does nothing later")
    parser.add_argument("--add-series",action="store_const",const=st.add_series,dest="add_series",help="adds series-channel pair to database, requires both to be specified")
    parser.add_argument("--remove-series",action="store_const",const=st.remove_series,dest="remove_series",help="removes series-channel pair to database, requires both to be specified")
    parser.add_argument("-p","--print_nel",action="store_const",const=us.print_new_episodes,dest="print_nel",help="printing all the newly fetched episodes")
    parser.add_argument("-l","--print_pairs",action="store_const",const=us.print_pairs,dest="print_pairs",help="prints all channel-series pairs, which have been added")
    parser.add_argument("-n","--nel_index",const="nel_index",nargs="?",default=0,help="specifying an entry from the nel table by index")
    parser.add_argument("-r","--remove_nel_entry",action="store_const",const=st.remove_nel,dest="remove_nel",help="removes an nel entry")
    parser.add_argument("--empty_nel",action="store_const",const=st.empty_nel,dest="empty_nel",help="empties entire new episode list")
    args = parser.parse_args()
    #print(args) #printing namespace

    #calling specified all functions
    for key,value in vars(args).items():
        if (callable(value)):
            if (key == "fetch"):
                value(args.channel,args.series)
            elif (key == "add_series" or key == "remove_series"):
                value(args.series,args.channel)
            elif (key =="remove_nel"):
                value(int(args.nel_index))
            else:
                value()

#main()
