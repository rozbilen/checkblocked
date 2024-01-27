#!/usr/local/bin/python
from socket import error as SocketError
import errno
import urllib2

h = urllib2
listUrls = open('urltest.txt','r').read().splitlines()
count = 0

for each in listUrls:
    try:
    	print "actual URL: "+listUrls[count]
        content = urllib2.urlopen(listUrls[count])
        if content.geturl() != listUrls[count]:
            print "redirected to: "+ content.geturl() +" "+"response code: "+str(content.getcode())
            if content.geturl().find("DELAY_")>=0:
            	print "!!!!delay seen from the policy"
        else:
        	print "no redirection occured for: " + listUrls[count]
        if content.getcode() == 200:
        	print "latest result code: "+ str(content.getcode())
        	a = content.read()
        	if a.find("Risotto")>=0:
        		print "blocked"
    except SocketError as e:
        if e.errno == errno.ECONNRESET:
			print listUrls[count]+" "+"connection was reset"
    except urllib2.HTTPError as g:
    	print g.code
    except urllib2.URLError as f:
        print f.args
    count = count + 1        
