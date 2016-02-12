#!/usr/bin/python

import os
import time
import urllib2
from BeautifulSoup import BeautifulSoup
import twitter

api = twitter.Api(consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret='')

# twitter creds debug
#print(api.VerifyCredentials())

url = 'http://hasitleaked.com/2015/kanye-west-so-help-me-god/'

# for debugging
#print leak_status[0].strip()

leaked = False

while not leaked:

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())

    leak_status = soup.find("li", {"class": "fontello-icon-droplet"}).contents
    leak_status = str(leak_status[0]).strip()

    if leak_status == "No leak reported":
        print "Still not here"
        time.sleep(60)

    else:
        api.PostUpdate('It has arrived')
        print "It has arrived"
        leaked = True
