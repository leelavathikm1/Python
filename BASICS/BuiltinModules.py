#date and time
import datetime

today=datetime.date.today()
print(today)    
now=datetime.datetime.now()
print(now)

#operating system
import os
current_directory=os.getcwd()
print(current_directory)

#JSON Data
import json 
data={"name": "Leela", "age": 30}
json_string=json.dumps(data)
print(json_string)

#import specific function
from math import sqrt
result=sqrt(16)
print(result)

#circle_area=pi*radius**2
#print(circle_area)


import requests
response=requests.get("https://api.github.com")
print(response.json())  

import pandas as pd
data={"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df=pd.DataFrame(data)
print(df)   

import requests
latitude=40.7128
longitude=-74.0060  
response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
weather_data=response.json()
print(weather_data) 


from datetime import datetime,timedelta
today=datetime.now()
week_ago=today-timedelta(days=7)
start_date=week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")
url=f"https://api.covid19api.com/country/united-states/status/confirmed?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z"
response=requests.get(url)
data=response.json()
print(data)

#-----------------------
#extract the daily data 
daily_data=['daily']

#create adataframe
df=pd.dataFrame({
    'date':daily_data['time'],
   ' max_temp':daily_data['temperature_2m_max'],
    'min_temp':daily_data['temperature_2m_min'],
    
})

#convertdate string to datetime
df['date']=pd.to_datetime(df['date'])   
print(df)



