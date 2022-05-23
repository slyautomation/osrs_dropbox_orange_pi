import csv
import requests
import json
import pandas as pd
import webbrowser
import numpy as np
import os
import dropbox
from datetime import datetime

# datetime object containing current date and time
from pandas import json_normalize

now = datetime.now()
print('downloading data from prices.runescape.wiki...')
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

new = 2  # open in a new tab, if possible

# python-requests
# prices.runescape.wiki/api/v1/osrs/1h


# Show all columns
pd.set_option('display.max_columns', None)
# Show all lines
pd.set_option('display.max_rows', None)
# value display length is 100, the default is 50
pd.set_option('max_colwidth', 200)

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        return dbx
    
def ensure_dir():
    directory = os.path.dirname('csv')
    print(directory)
    if not os.path.exists('csv')
        os.makedirs('csv')


def call_http_prices():
    headers = {
        'User-Agent': 'name',
        'From': 'email@email.com'  # This is another valid field
    }
    response = requests.get("https://prices.runescape.wiki/api/v1/osrs/1h", headers=headers)
    stats = json.loads(response.text)
    #print(stats)
    return stats

# average over 12 hour window get data each hour over a week
access_token = '' # add the access token from dropbox
transferData = TransferData(access_token)
ensure_dir()
jsonData = call_http_prices()

data = pd.DataFrame(jsonData)
data['item_id'] = data.index
data['index_id'] = np.arange(len(data))
#print('first data:', data)
test = data['data']





temp_data = pd.DataFrame(json_normalize(test))

text_file = open("data_2.html", "w")

data_w = temp_data.to_html()
text_file.write(data_w )
text_file.close()

temp_data['index_id'] = np.arange(len(temp_data))
data = pd.merge(data, temp_data, left_on='index_id', right_on='index_id', how='left').drop(['index_id','data'], axis=1)

timeframe = data.iloc[0]['timestamp']
datetime_time = datetime.fromtimestamp(timeframe).strftime('%d-%b-%Y-%H%M')

#print(datetime_time)
#print(data)

format_data = pd.DataFrame(data)

data = format_data.drop(columns='timestamp').fillna(0)

#finalData = toptenvalue(dataFile)

#data = pd.DataFrame(finalData)

#addmargins()
#addtestdate()

data.to_csv('csv/' + 'raw_data-' + datetime_time + '.csv', index=False)
print('data saved to csv - data extracted as @', datetime_time)
file_from = filename
file_to = '/' + file_from
# API v2
db = transferData.upload_file(file_from, file_to)
account db.users_get_current_account()
print('data saved to dropbox account for:', account.name.given_name, account.name.surname)
