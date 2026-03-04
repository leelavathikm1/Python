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



