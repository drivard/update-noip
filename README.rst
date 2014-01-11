Update your no-ip.com domain name through crontab
=================================================

Reason
------

I created this script because my IP address does not change really often and I was bothered by the fact that www.noip.com sends email about your domain name expiring after more than 30 days without a change. To remedy this behavior I decided to write that script and run it into a scheduled job every 10 days.

How does this work
------------------

The script can be run every 20 days and it will force your domain name to update with a wrong IP address and a moment after it will update it with the proper IP address. This will bypass the expiration rule.

Installation
------------

*Requirements
This little script requires the ``requests`` python module from http://docs.python-requests.org/en/latest/

.. code-block:: bash

	git clone git@github.com:drivard/update-noip.git
	
	cd update-noip
	
	pip install -r requirements.txt
	
	# or
	
	pip install -U requests
	
	# or
	 
	easy_install requests


Configuration
=============

The script
----------

1. Clone the script

.. code-block:: bash
	
	git clone git@github.com:drivard/update-noip.git

2. Edit the script with your username, password, hostname and ip addresses bag.

.. code-block:: pycon
	
	IPS_BAG  = ["152.25.65.88", "154.58.69.25", "45.255.6.54"]
	HOSTNAME = "yourhostname.no-ip.com"
	USERNAME = "username"
	PASSWORD = "password" 

Execution
---------
To run the script once you edited the parameters.

.. code-block:: bash
	
	python update_noip.py

Crontab
-------

.. code-block:: bash
	
	15 3 */10 * *   /usr/bin/python /<path_to_python_script>/update_noip.py


