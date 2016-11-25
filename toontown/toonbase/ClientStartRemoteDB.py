#!/usr/bin/env python2
import json
import os
import urllib2
from pandac.PandaModules import *

'''
username = os.environ['ttiUsername']
password = os.environ['ttiPassword']
'''
distribution = ConfigVariableString('distribution', 'dev').getValue()
'''
accountServerEndpoint = 'http://www.toontownrewritten.com/api/'
request = urllib2.urlopen(
    'http://www.toontownrewritten.com/api/login/?format=json',
    data={'username': username, 'password': password})
'''
'''
try:
    response = json.loads(request.read())
    print(response)
except ValueError:
    print "Couldn't verify account credentials."
else:
'''
'''
os.environ['TTI_PLAYCOOKIE'] = 'WUp9wpmcV1XuV1dSijFLOtjbChcewOaZC5E4Fwyl7HRPw'
'''
# Start the game:
import toontown.toonbase.ClientStart
