# -*- coding: utf-8 -*-
import requests

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)

import pandas as pd

data = pd.read_csv('data.csv')
print(data.head())  # Вывести первые строки данных
print(data.describe())  # Вывести основные статистические показатели данных


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Line Plot')
plt.show()
