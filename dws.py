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
def search(searchquery, theresults):
    """sends get requests and returns the results"""
   # global r
    try:

        r = session.get(querystring)
        theresults= r.text
    except:

        print("Something fucked up.")
    return r.text

parser = argparse.ArgumentParser(description="DWS: Dark Web Search")
parser.add_argument("-q", "--query", type=str, help="Search with keywords")
parser.add_argument("-5", "--html", help="Save the results into an html file", action="store_true")
args=parser.parse_args()

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'

session.proxies['https'] = 'socks5h://localhost:9050'



#Change user agent so ahmia doesn't think we are doing a mitm scam

requests.utils.default_user_agent('Mozilla Firefox')
headers = {
    'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
}

if args.query == None:

    print("Welcome to CPSDWS.")

    query=raw_input("Enter your keywords:")

    print("Input received. Requesting. This takes a bit. Like forever.")
    querystring = 'http://msydqstlz2kzerdg.onion/search/?q=' + query
if args.query is not None:
    print("Input received.")
    print("Searching TOR via Ahmia.")
    querystring='http://msydqstlz2kzerdg.onion/search/?q='+query
    i2pquerystring='https://ahmia.fi/search/i2p/?q='+query
if query is not None:
    i2pquerystring = 'https://ahmia.fi/search/i2p/?q=' + query
    try:
        print("Querying Ahmia TOR...")
        r = session.get(querystring, headers=headers)

    except ValueError as valerr:
      print("ValueError:", valerr)
    except:

        print("Something fucked up.")
        exit(1)

    try:
        print("Searching I2P on Ahmia.")
        i2prequest = session.get(i2pquerystring, headers=headers)

    except:

        print("Something fucked up.")
        exit(1)
# render html to console
results = html2text.html2text(r.text)
results+= html2text.html2text(i2prequest.text)
print results

#save results
saveastext()
if args.html == True:
    saveashtml()
