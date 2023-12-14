import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/players/774cf58b/Max-Aarons"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

tables = soup.findAll("table")

summary_entries = []
label_data = []

# fileName = "testReq7.txt"
for table in tables:
    footer = table.find("tfoot")
    if footer:
        # print("1")
        # header = table.find_all("tr")
        # labels = header[1]
        
        # for i in labels:
        #     info = i.text
        #     label_data.append(info)
        # filtered_list = [x for x in label_data if x.strip()]
        

        summary = footer.find_all("tr")
        summary_data = summary[0]
        
        for i in summary_data:
            data = i.text
            if data:
                summary_entries.append(data)
        
# print(filtered_list)
print(summary_entries)









