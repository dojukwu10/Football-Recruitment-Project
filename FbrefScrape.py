import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/players/d70ce98e/Lionel-Messi"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

tables = soup.findAll("table")

fileName = "testReq7.txt"
for table in tables:
    footer = table.find("tfoot")
    if footer:
        # print("1")
        header = table.find_all("tr")
        labels = header[1]
        label_data = []
        for i in labels:
            info = i.text
            label_data.append(info)
        filtered_list = [x for x in label_data if x.strip()]
        print(filtered_list)

        summary = footer.find_all("tr")
        summary_data = summary[0]
        summary_entries = []
        for i in summary_data:
            data = i.text
            summary_entries.append(data)
        print(summary_entries)











