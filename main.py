import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import collections


JSON_URL='https://random-data-api.com/api/beer/random_beer?size=20'

r=requests.request(method='get', url=JSON_URL)
data=r.json()


style=[]
for i in data:
    style.append(i['style'])

count=collections.Counter(style)
print(count)

style_array=np.array(style)

x_list=list(count.keys())
x=np.array(x_list)
print(x)
y_list=list(count.values())
y=np.array(y_list)
print(y)

series=pd.Series(style_array)
plt.bar(x,y)
plt.show()

print(series)
