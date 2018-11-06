#!/usr/bin/python2
# Author = Jeff Barron
# Critical Path Security osint tool for Dark Web Search
# dws searches tor, i2p and pastebins

#todo add multithreading so all requests occur concurrently
#todo rewrite to use a function and a list of sites, add haystack http://haystakvxad7wbk5.onion/?q=
#todo add OnionLand search http://3bbaaaccczcbdddz.onion/search?q=
#todo fix pastebin.com https://pastebin.com/search?q=sunlakes11%40gmail.com use burp to check for post request
#http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=0+day+exploit&cmd=Search%21


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
     fo.write(writedis)
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
    global r
    try:

        r = session.get(querystring)
        theresults= r.text
    except:

        print("Something fudged up.")
    return r.text

parser = argparse.ArgumentParser(description="DWS: Dark Web Search")
parser.add_argument("-q", "--query", type=str, nargs='+', help="Search with keywords")
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

if args.query is None:

    print("Welcome to CPS DWS.")

    query=raw_input("Enter your keywords:")

    print("Input received. Requesting. This takes a bit. Like forever.")
    querystring = 'http://msydqstlz2kzerdg.onion/search/?q=' + query
if args.query is not None: #used the command line option to query
    print("Command line input received.")
    print("Searching TOR via Ahmia.")
    query=' '.join(args.query)
    print(args.query)
    print query
    querystring='http://msydqstlz2kzerdg.onion/search/?q='+ query
    i2pquerystring='https://ahmia.fi/search/i2p/?q='+ query
    haystackquery='http://haystakvxad7wbk5.onion/?q=' + query
    onionlandquery = 'http://3bbaaaccczcbdddz.onion/search?q=' + query
    torchquery = 'http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=' + query + '&cmd=Search%21&form=extended'
    notevilquery = 'http://hss3uro2hsxfogfq.onion/index.php?q=' + query
   # pastebinquery='https://pastebin.com/search?q='+ query
if query is not None: #should always be true
    i2pquerystring = 'https://ahmia.fi/search/i2p/?q=' + query
    haystackquery = 'http://haystakvxad7wbk5.onion/?q=' + query
    onionlandquery = 'http://3bbaaaccczcbdddz.onion/search?q=' + query
    torchquery = 'http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=' + query + '&cmd=Search%21&form=extended'
    notevilquery = 'http://hss3uro2hsxfogfq.onion/index.php?q=' + query
    #pastebinquery = 'https://pastebin.com/search?q=' + query

    try:
        print("Searching Ahmia on TOR...")
        r = session.get(querystring, headers=headers)

    except ValueError as valerr:
      print("ValueError:", valerr)
    except:

        print("Something fudged up.")
        exit(1)

    try:
        print("Searching Ahmia on I2P...")
        i2prequest = session.get(i2pquerystring, headers=headers)

    except:

        print("Something fudged up.")
        exit(1)

    try:
        print("Searching Haystack on TOR...")

        haystackrequest = session.get(haystackquery, headers=headers)

    except:

        print("Something fudged up.")
        exit(1)


    try:
        print("Searching Onionland on TOR...")

        onionlandrequest = session.get(onionlandquery, headers=headers)

    except:

        print("Something fudged up.")
        exit(1)

    try:
        print("Searching Torch on TOR...")


        torchrequest = session.get(torchquery, headers=headers)

    except:

        print("Something fudged up.")
        exit(1)

    try:
        print("Searching Notevil on TOR...")


        notevilrequest = session.get(notevilquery, headers=headers)

    except:

        print("Something fudged up.")
        exit(1)
   # try:
    #    print("Searching Pastebin.com...")
        #remove tor proxy so pastebin won't throw a captcha at us
     #   session.proxies['https'] = ''
     #   pasterequest = session.get(pastebinquery, headers=headers)

    #except:

     #   print("Something fudged up.")
      #  exit(1)
# render html to console
results = html2text.html2text(r.text)
results+="*****************************BEGIN Ahmia i2P*****************************"
results+= html2text.html2text(i2prequest.text)
results+="*****************************BEGIN HAYSTACK*****************************"
results+=html2text.html2text(haystackrequest.text)
results+="*****************************BEGIN ONIONLAND*****************************"
results+= html2text.html2text(onionlandrequest.text)
results+="*****************************BEGIN ToRCH*****************************"
results+= html2text.html2text(torchrequest.text)
results+="*****************************BEGIN Notevil*****************************"
results+= html2text.html2text(notevilrequest.text)
#results+="*****************************BEGIN PASTEBiN*****************************"
#results+= html2text.html2text(pasterequest.text)
print results



#save results
saveastext()
if args.html == True:
    saveashtml()
