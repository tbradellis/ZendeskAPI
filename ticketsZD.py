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
ZD_PASS = '*******'

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



# tell computer where to put CSV
outfile_path='file.csv'

# Decode the JSON responses into a dictionary so I can use the data
keyList = {}
dataRows = {}
data = response.json()
x = 0

for item in data['tickets']:
    keylist = item.keys()
    count = len(keylist)

writer = csv.writer(open(outfile_path, 'w'))
#create a list with headings for our columns
headers = keylist

#write the row of headings to our CSV file
writer.writerow(sorted(headers))
#print(keylist)
#write the row of headings to our CSV file
#writer.writerow(headers)

for ticks in data['tickets']:
    #initialize the row
    row = []
    #add every 'cell' to the row list, identifying the item just like an index in a list


    row.append(str(ticks['assignee_id']).encode('utf-8'))
    #row.append(str(ticks['brand_id'].encode('utf-8')))
    row.append(str(ticks['collaborator_ids']).encode('utf-8'))
    row.append(str(ticks['created_at']).encode('utf-8'))
    row.append(str(ticks['custom_fields']).encode('utf-8'))
    row.append(str(ticks['description'].encode('utf-8')))
    row.append(str(ticks['due_at']).encode('utf-8'))
    row.append(str(ticks['external_id']).encode('utf-8'))
    row.append(str(ticks['fields']).encode('utf-8'))
    #row.append(str(ticks['followup_ids']).encode('utf-8'))
    row.append(str(ticks['forum_topic_id']).encode('utf-8'))
    row.append(str(ticks['group_id']).encode('utf-8'))
    row.append(str(ticks['has_incidents']).encode('utf-8'))
    row.append(str(ticks['id']).encode('utf-8'))
    row.append(str(ticks['organization_id']).encode('utf-8'))
    row.append(str(ticks['priority']).encode('utf-8'))
    row.append(str(ticks['problem_id']).encode('utf-8'))
    row.append(str(ticks['raw_subject']).encode('utf-8'))
    row.append(str(ticks['recipient']).encode('utf-8'))
    row.append(str(ticks['requester_id']).encode('utf-8'))
    row.append(str(ticks['satisfaction_rating']).encode('utf-8'))
    row.append(str(ticks['sharing_agreement_ids']).encode('utf-8'))
    row.append(str(ticks['status']).encode('utf-8'))
    row.append(str(ticks['subject']).encode('utf-8'))
    row.append(str(ticks['submitter_id']).encode('utf-8'))
    row.append(str(ticks['tags']).encode('utf-8'))
    row.append(str(ticks['type']).encode('utf-8'))
    row.append(str(ticks['updated_at']).encode('utf-8'))
    row.append(str(ticks['url']).encode('utf-8'))
    row.append(str(ticks['via']).encode('utf-8'))


    writer.writerow(row)
#for val in data['tickets']:
#    rows = val.values()
 #   count2 = len(rows)
#print(count)
#print(keylist)
#print(count2)
#print(rows)
#print(data)
#print(data['tickets'])
#print(data)
print(sorted(headers))










    #for each in keylist:
        #newList = []
       # newList.append(each[x])
       # print(each[x])

     #  x += 1
#newList = dict([newList])
#print(newList.values())

#for item in data['tickets']:
  # print item.keys()
   #keyList = item.keys()

  # print(keyList)





   #for val in data['tickets'].values():

       #dataRows = val.values()
       #print(val)
       #print item.values()
#print(keyList)

#keyDict = response2.json()
#keylist = keyDict.keys()

#print data
#for key in keylist:
    #print key
# Convert the data from dict to csv
##Not right  messed up.  Forgetaboutit

#toCSV = data['tickets']:
#columns = keyList
#f = open('tickets.csv', 'wb')
#dict_writer = csv.DictWriter(f, columns)
#dict_writer.writer.writerow(columns)
#print(toCSV)
#dict_writer.writerows(toCSV)




