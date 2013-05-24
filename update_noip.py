#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2
import random

# IPs bag is the IP that will be used to replace your current ip.
# It is the temporary changed ip.
IPS_BAG  = ["74.56.89.5","207.164.79.7","206.47.78.150","64.235.215.181","64.237.254.153",]
HOSTNAME = "home" # noip.com hostname
USERNAME = "drivard" # noip.com username
PASSWORD = "visa-99!" # noip.com password

_old_ = IPS_BAG[random.randrange(0,len(IPS_BAG) - 1)]
_new_ = urllib2.urlopen("http://curlmyip.com/").read().strip()
_url_ = "http://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip}"

# Update no-ip with the fake old ip
_url_called_ = _url_.format(hostname=HOSTNAME, ip=_old_)
r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
print r.status_code # if 200 this means the page was reached
print r.content # should be the response from noip.com

# Update current public ip
_url_called_ = _url_.format(hostname=HOSTNAME, ip=_new_)
r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
print r.status_code # if 200 this means the page was reached
print r.content # should be the response from noip.com

# Successfully forced a change of your domain ip
