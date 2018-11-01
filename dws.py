#!/usr/bin/python2
# Author = Jeff Barron
# Critical Path Security Dark Web Search

#todo add i2p search

import requests
import html2text

import argparse

WARNING = '\033[93m'
FAILRED = '\033[91m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'

def saveastext():
    try:
     writedis=results.encode('utf-8')
     fo = open("cpsdarkwebsearchresults.txt", "w")
     fo.write(writedis)
     fo.close()
     print(OKGREEN + "cpsdarkwebsearchresults.txt successfully created." + ENDC)
    except TypeError as foob:
        print('TypeError:', foob)

    except OSError as err:
      print("OSERROR:", err)


    except ValueError as valerr:
      print("ValueError:", valerr)



def saveashtml():
    try:
     writedis = results.encode('utf-8')
     fo = open("cpsdarkwebsearchresults.html", "w")
     fo.write(r.text)
     fo.close()
     print(OKGREEN + "cpsdarkwebsearchresults.html successfully created." + ENDC)

    except TypeError as foob:
        print('TypeError:', foob)

    except OSError as err:
      print("OSERROR:", err)


    except ValueError as valerr:
      print("ValueError:", valerr)

logo = r"""



             .__  __  .__              .__         
  ___________|__|/  |_|__| ____ _____  |  |        
_/ ___\_  __ \  \   __\  |/ ___\\__  \ |  |        
\  \___|  | \/  ||  | |  \  \___ / __ \|  |__      
 \___  >__|  |__||__| |__|\___  >____  /____/      
     \/                       \/     \/            
              __  .__                              
___________ _/  |_|  |__                           
\____ \__  \\   __\  |  \                          
|  |_> > __ \|  | |   Y  \                         
|   __(____  /__| |___|  /                         
|__|       \/          \/                          
                                  .__  __          
  ______ ____   ____  __ _________|__|/  |_ ___.__.
 /  ___// __ \_/ ___\|  |  \_  __ \  \   __<   |  |
 \___ \\  ___/\  \___|  |  /|  | \/  ||  |  \___  |
/____  >\___  >\___  >____/ |__|  |__||__|  / ____|
     \/     \/     \/                       \/     

"""
parser = argparse.ArgumentParser(description="DWS: Dark Web Search")
parser.add_argument("-q", "--query", type=str, help="Search with keywords")
parser.add_argument("-5", "--html", help="Save the results into an html file", action="store_true")
args=parser.parse_args()

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'

session.proxies['https'] = 'socks5h://localhost:9050'

#header['User-agent'] = "Mozilla Firefox"

if args.query == None:

    print("Welcome to CPSDWS. Enter your search keywords:")

    query=raw_input()

    print("Input received. Requesting. This takes a bit. Like forever.")
    querystring = 'http://msydqstlz2kzerdg.onion/search/?q=' + query
if args.query is not None:

    querystring='http://msydqstlz2kzerdg.onion/search/?q='+query

try:

    r = session.get(querystring)

except:

    print("Something fucked up.")

# render html to console
results = html2text.html2text(r.text)

print results

#save results
saveastext()
if args.html == True:
    saveashtml()
