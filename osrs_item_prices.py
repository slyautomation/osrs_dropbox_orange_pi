import csv
import requests
import json
import pandas as pd
import webbrowser
import numpy as np
from datetime import datetime

# datetime object containing current date and time
from pandas.io.json import json_normalize

now = datetime.now()

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




def call_http_prices():
    headers = {
        'User-Agent': 'name',
        'From': 'email@email.com'  # This is another valid field
    }
    response = requests.get("https://prices.runescape.wiki/api/v1/osrs/1h", headers=headers)
    stats = json.loads(response.text)
    print(stats)
    return stats

# average over 12 hour window get data each hour over a week

jsonData = call_http_prices()

data = pd.DataFrame(jsonData)
data['item_id'] = data.index
data['index_id'] = np.arange(len(data))
print('first data:', data)
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
html = data.to_html()
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()

url = "index.html"
webbrowser.open(url, new=new)