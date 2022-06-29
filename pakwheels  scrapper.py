#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.pakwheels.com/used-cars/search/-/?page="

all_data = []
for page in range(1, 3):
    r = requests.get(url + str(page))

    soup = BeautifulSoup(r.content, "html.parser")

    for ul in soup.select("ul.search-vehicle-info-2"):
        car_name = ul.find_previous("h3").get_text(strip=True)
        info = [li.get_text(strip=True) for li in ul.select("li")][:5]
        all_data.append([car_name, *info])

df = pd.DataFrame(
    all_data, columns=["Car Name", "Year", "KM", "Type", "CC", "Type 2"]
)
print(df)


# In[ ]:





# In[ ]:




