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
    args = parser.parse_args()
    print(args)

    #calling specified all functions
    for key,value in vars(args).items():
        if (callable(value)):
            if (key == "fetch"):
                value(args.channel,args.series)
            else:
                value()

    
main()
