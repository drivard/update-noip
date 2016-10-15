#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2
import random
import syslog

# Adding syslog support.
# I want to make sure that when the crontab runs it really execute
# the update of the IP at noip.com.
log = syslog.syslog

# IPs bag is the IP that will be used to replace your current ip.
# It is the temporary changed ip.
IPS_BAG = ['74.56.89.5', '207.164.79.7', '206.47.78.150', '64.235.215.181', '64.237.254.153', '9.32.98.95',
           '145.187.75.190', '250.154.138.232', '187.210.74.88', '24.30.68.55', '71.131.203.96', '142.130.17.152',
           '118.213.193.121', '201.135.104.165', '126.210.53.5', '161.26.48.222', '141.92.53.246', '233.187.119.252',
           '77.253.221.248', '71.65.248.207', '215.94.12.105', '214.149.59.160', '69.184.41.24', '69.129.207.56',
           '223.180.110.45', '214.148.188.184', '178.110.125.181', '8.40.104.86', '40.254.106.213', '32.153.45.141']

try:
    from settings import USERNAME, PASSWORD, HOSTNAMES
except:
    HOSTNAMES = ["hostname1", "hostname2", "hostname3"]  # noip.com hostnames
    USERNAME = ""  # noip.com username
    PASSWORD = ""  # noip.com password

_old_ = IPS_BAG[random.randrange(0, len(IPS_BAG) - 1)]
_new_ = urllib2.urlopen("http://api.enlightns.com/tools/whatismyip/?format=text").read().strip()
_url_ = "https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip}"

log('... Update www.noip.com account ...')
log('... OLD IP: {ip}'.format(ip=_old_))
log('... NEW IP: {ip}'.format(ip=_new_))

for hostname in HOSTNAMES:
  # Update no-ip with the fake old ip
  _url_called_ = _url_.format(hostname=hostname, ip=_old_)
  r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
  print r.status_code  # if 200 this means the page was reached
  print r.content  # should be the response from noip.com

  # Update current public ip
  _url_called_ = _url_.format(hostname=hostname, ip=_new_)
  r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
  print r.status_code  # if 200 this means the page was reached
  print r.content  # should be the response from noip.com

  if r.status_code == 200:
      success = 'yes'
  else:
      success = 'no'

log('... Succeed: {success}'.format(success=success))
# Successfully forced a change of your domain ip

