#!/usr/bin/env python

# 09/26/2016
# eric@pythonicneteng.com
# Usage: python <script> <sub name> <sub email>

import requests, sys, json


api_key = '<replace with your API key>'

# Squence Subscribtion: POST /v3/courses/<course_id>/subscribe

sub_first_name = sys.argv[1]
sub_email = sys.argv[2]

sequenceID = '<replace with your sequence ID>'

base_url = 'https://api.convertkit.com/v3/'

url = base_url + 'courses/' + sequenceID + '/subscribe'
headers = {'Content-Type': 'application/json'}
post_payload = {
    'api_key': api_key,
    'email': sub_email,
    'name': sub_first_name
}

r = requests.post(url, data=json.dumps(post_payload), headers=headers, verify=False)

print(r.content)

# Add Sub to Tag: POST /v3/tags/<tag_id>/subscribe

tagID = '<replace with your Tag ID>'
url = base_url + 'tags/' + tagID + '/subscribe'
r = requests.post(url, data=json.dumps(post_payload), headers=headers, verify=False)

print(r.content)

