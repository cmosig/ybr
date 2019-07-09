import sys
import argparse
import fetcher as f
import storage as st

def main():
    """reading command line arguements and calling respective methods"""
    init_argument_parser()

def test():
    print("test worked")

def test2():
    print("test2 worked")

def init_argument_parser():
    parser = argparse.ArgumentParser(description="A better YouTube recommendation service.")
    parser.add_argument("-f","--fetch",action="store_const",const=f.fetch_latest_videotitles,dest="fetch",help="fetch latest videos")
    parser.add_argument("-s","--series",const="series",help="specify series to work on",nargs="?",default="")
    parser.add_argument("-c","--channel",const="channel",help="specify channel to work on",nargs="?",default="")
    parser.add_argument("--initDB",action="store_const",const=st.init_database,dest="initDB",help="initial init of database. does nothing later")
    parser.add_argument("--add-series",action="store_const",const=st.add_series,dest="add_series",help="adds series-channel pair to database, requires both to be specified")
    parser.add_argument("--remove-series",action="store_const",const=st.remove_series,dest="remove_series",help="removes series-channel pair to database, requires both to be specified")
    args = parser.parse_args()
    print(args)

    #calling specified all functions
    for key,value in vars(args).items():
        if (callable(value)):
            if (key == "fetch"):
                value(args.channel,args.series)
            elif (key == "add_series" or key == "remove_series"):
                value(args.series,args.channel)
            else:
                value()

    
main()
