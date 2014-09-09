#-------------------------------------------------------------------------------
# Name:        OrganizationsTag.py
# Purpose:
#     Tag all organizations in Zendesk as "Customer"
# Author:      Brad Ellis
#
# Created:     09/07/2014
# Copyright:   (c) bellis 2014
# License:     <BMF>
#-------------------------------------------------------------------------------

import requests, json

def main():
    pass


# Set credentials for Zendesk

ZD_USER = 'username@email.com'
ZD_PASS = 'password'

# Build and execute GET request
# This section will grab the complete organization list
# and the associate fields (in json format)

url = 'https://{subdomain}.zendesk.com/api/v2/organizations.json'
headers = {'Accept':'application/json'}
response = requests.get( url, auth=(ZD_USER, ZD_PASS), headers=headers )

# Check for HTTP codes and status other than 200

if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()


# Decode the JSON response into a dictionary so I can use the data

data = response.json()

# Here's what we'll be posting to each organization - json format

tag = { 'organization': { 'tags': ['Customer'] } }

# Set session parameters for new request (put).
# Using session to accomodate multiple requests

headers2 = {'content-type':'application/json'}
session = requests.Session()
session.auth = (ZD_USER, ZD_PASS)
session.headers = headers2

# Go through the data and grab the id value
# deliver payload via post

org_list = data['organizations']
for organization in org_list:
    id = str(organization['id'])
    url2 = 'https://{subdomain}.zendesk.com/api/v2/organizations/' + id + '.json'
    payload = json.dumps(tag)
    response2 = session.put(url2, data=payload, auth=(ZD_USER, ZD_PASS),
    headers=session.headers)

# Check for HTTP codes other than 200

    if response2.status_code != 200:
        print('Status:', response2.status_code, 'Problem with the request. Exiting.')
        exit()
    print('Successfully added tag to organizations #{}'.format(id))

if __name__ == '__main__':
    main()
