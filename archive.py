import argparse
import re
from colorama import Fore, Style,init
from func import save
from func import domain
from func import search
from func import params
from func import common
init()


def exclude(body,blacklist):
    final=[]
    for i in body:
        if len(blacklist) > 0:
            words = re.compile("|".join(blacklist))
            if not words.search(i):
               final.append(i)
        else:
            final.append(i)
    return final
def conn():
    parser = argparse.ArgumentParser(
        usage="./archive.py -u [target] -c [statuscode]",
        add_help=False,
    )
    parser.add_argument("-h", "--help", action="help", help=" How To Use This Tool ")
    parser.add_argument("-u", dest='target', help="target url ex:google.com",metavar='Target',required=True)
    parser.add_argument("-f", dest='fro', help="archive date from",metavar='From')
    parser.add_argument("-t", dest='to', help="archive date to",metavar='To')
    parser.add_argument("-c", dest='fi', help="status code ex:200",metavar='Statuscode',required=True)
    parser.add_argument("-l", dest='limit', help="Archive limit try increase limit for better results default is 20k",metavar='Limit')
    parser.add_argument("-s", dest='search', help="Only print Urls contains searched word",metavar='Search')
    parser.add_argument("-e", dest='exclude', help="Exclude extensions ex:css,js",metavar='Exclude')
    parser.add_argument("--domains", dest='only', action="store_true", help="extract only urls from archive result")
    parser.add_argument("--params", dest='params', action="store_true", help="Extract urls contains parameters")
    parser.add_argument("--common", dest='common', help="Search for common filenames ex:php,aspx,html",metavar='Common')
    parser.add_argument("--save", dest='save', action="store_true", help="Saving results to output directory")

    print(Fore.LIGHTGREEN_EX+
    """
 █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝
███████║██████╔╝██║     ███████║██║██║   ██║█████╗  
██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝  
██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝    
Coded by:Ahmad Shwani

python3 archive.py --help for help
________________________________________________________
"""+Style.RESET_ALL)
    args = parser.parse_args()
    if args.common and args.only or args.common and args.params or args.only and args.params:
        print("Error you can only use parameters mode or domain mode or common mode not together")
    else:
        if args.target and args.fi:
            f=[]
            if args.only:
                f=domain.only(args.target, args.fro, args.to, args.fi, args.only,args.limit)
                for i in f:
                    target = str(args.target)
                    if target.startswith("http://") or target.startswith("https://"):
                        target1 = target.split("://")
                        i = i.replace(target1[1], Fore.RED + target1[1] + Style.RESET_ALL)
                        print(i)
                    else:
                        i=i.replace(args.target, Fore.RED + args.target + Style.RESET_ALL)
                        print(i)
                if not f:
                    print("No Domains Found")
                else:
                    if args.save:
                        file=args.target+"-domains"
                        save.save(f,file)
            elif args.params:
                se = []
                p=[]
                black_list = []
                saving=[]
                if args.exclude:
                    if "," in args.exclude:
                        black_list = args.exclude.split(",")
                        for i in range(len(black_list)):
                            black_list[i] = "." + black_list[i]
                    else:
                        black_list.append("." + args.exclude)
                else:
                 black_list = []
                p=params.params(args.target, args.fro, args.to, args.fi,args.limit,black_list)
                p = list(dict.fromkeys(p))
                while ("" in p):
                    p.remove("")
                if args.search:
                    final = []
                    for line in p:
                        if args.search in line:
                            line = line.strip()

                            if args.search in line:
                                line = line.strip()
                            else:
                                line = line
                            se.append(line)
                    for i in se:
                        i = i.replace(args.search, Fore.MAGENTA +args.search + Style.RESET_ALL)
                        i = i.replace("FUZZ", Fore.RED +"FUZZ" + Style.RESET_ALL)
                        print(i)
                else:
                    for i in p:
                        i = i.replace("FUZZ", Fore.RED +"FUZZ" + Style.RESET_ALL)
                        print(i)
                if args.search:
                    saving=se
                else:
                    saving=p
                if not p:
                    print("No Parameters Found")
                else:
                    if args.save:
                        file=args.target+"-parameters"
                        save.save(saving,file)
            elif args.common:
                comm=[]
                mode = ["php", "css", "html", "asp", "aspx", "wsdl", "tpl", "admin", "install"]
                search1 = []
                if args.common not in mode:
                    print("Please type common mode")
                    print("Modes: "+ str(mode))
                else:
                    filename = f"lists/{args.common}.txt"
                    file = open(filename, "r")
                    for j in file:
                        j = j.replace("\n", "")
                        search1.append(j)
                    comm = common.common(args.target, args.fi, args.limit, search1)
                    for i in comm:
                            for j in search1:
                                if j in i:
                                    i=i.replace(j,Fore.RED+j+Style.RESET_ALL)
                                    print(i)
                    if not comm:
                        print(f"No common {args.common} Files Found")
                    else:
                        if args.save:
                            file = args.target + "-commons"
                            save.save(comm, file)
            else:
                s=search.search(args.target, args.fro, args.to, args.fi, args.search, args.only,args.limit)
                fi=[]
                saving=[]
                if args.search:
                    if args.exclude:
                        black_list = []
                        if "," in args.exclude:
                            black_list = args.exclude.split(",")
                            for i in range(len(black_list)):
                                black_list[i] = "." + black_list[i]
                        else:
                            black_list.append("." + args.exclude)
                        fi=exclude(s,black_list)
                        for i in fi:
                            i = i.replace(args.search, Fore.RED + args.search + Style.RESET_ALL)
                            print(i)
                    else:
                        for i in s:
                         i = i.replace(args.search, Fore.RED + args.search + Style.RESET_ALL)
                         print(i)
                    if args.exclude:
                        saving=fi
                    else:
                        saving=s
                    if not s:
                        print("No Results found")
                    else:
                        if args.save:
                            file = args.target + "-searches"
                            save.save(saving, file)
                else:
                    saving2=[]
                    if args.exclude:
                        black_list = []
                        if "," in args.exclude:
                            black_list = args.exclude.split(",")
                            for i in range(len(black_list)):
                                black_list[i] = "." + black_list[i]
                        else:
                            black_list.append("." + args.exclude)
                        fi=exclude(s,black_list)
                        for i in fi:
                            print(i)
                    else:
                        for i in s:
                            print(i)
                    if args.exclude:
                        saving2 = fi
                    else:
                        saving2 = s
                    if not s:
                        print("No Results found")
                    else:
                        if args.save:
                            file = args.target + "-All"
                            save.save(saving2, file)
        else:
            parser.print_help()


if __name__ == '__main__':
    conn()
