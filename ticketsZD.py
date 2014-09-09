#-------------------------------------------------------------------------------
# Name:        TicketsZD.py
# Purpose:
# Extract ticket data (json format) and convert to csv
# Author:      Brad Ellis
#
# Created:     09/08/2014
# Copyright:   (c) bellis 2014
# License:     <BMF>
#-------------------------------------------------------------------------------

import requests, json, csv

def main():
    pass


# Set credentials for Zendesk

ZD_USER = 'username@email.com'
ZD_PASS = 'Password'

# Build and execute GET request
# This section will grab the complete list of tickets
# and the associated fields (in json format)

url = 'https://apptio.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json'}
response = requests.get( url, auth=(ZD_USER, ZD_PASS), headers=headers )

# Check for HTTP codes and status other than 200

if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
# Pull json list of ticket fields (will be used as keys/columns in
# dict/csv)
####THIS Will probably not work.  Need to read the nested json from the first get
url2 = 'https://apptio.zendesk.com/api/v2/ticket_fields.json'
response2 = requests.get( url2, auth=(ZD_USER, ZD_PASS), headers=headers )

# Check for HTTP codes and status other than 200

if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()


# Decode the JSON responses into a dictionary so I can use the data

data = response.json()
keyDict = response2.json()
keylist = keyDict.keys()

print data
for key in keylist:
    if k2 in d.get(k1, {}):
    print key
# Convert the data from dict to csv
##Not right  messed up.  Forgetaboutit
toCSV = data
columns = keylist
f = open('tickets.csv', 'wb')
dict_writer = csv.DictWriter(f, columns)
dict_writer.writer.writerow(columns)
dict_writer.writerows(toCSV)





if __name__ == '__main__':
    main()
