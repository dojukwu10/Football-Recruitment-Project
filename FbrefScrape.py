import requests
import pandas as pd
from bs4 import BeautifulSoup


from urllib.request import urlopen
import re
import requests
import time

def getReports():

    player_data = []
    completed_passes = ''
    counter = 0
    counter2= 0
    # Open the URL and extract the HTML and write it to a new file
    html = urlopen('https://fbref.com/en/comps/9/stats/Premier-League-Stats#stats_squads_standard_for')
    bs = BeautifulSoup(html, 'html.parser').encode()

    with open("data1.html", "w") as file:
        file.write(str(bs))
    
    # Open the HTML file and replace the comment part with void so that all the tables can now be accessed
    with open("data1.html", 'r') as html1:
        bs2 = BeautifulSoup(html1, 'html.parser')
        text_of_bs2 = str(bs2)
        usable_bs2 = text_of_bs2.replace("<!--", " ").replace("-->", " ")
        with open("data2.html", 'w') as commentless_content:
            commentless_content.write(usable_bs2)

    # Create a text file and write links to player profiles
    with open('data2.html', 'r') as main_page:
        bs3 = BeautifulSoup(main_page, 'html.parser')
        table_contents = bs3.find_all('table')
        with open('player_profiles.csv', 'w') as text_file:
            text_file.write("Name\tLink\n")  # Header


            for content in table_contents:
                list_of_links = content.find_all('a', href=re.compile(r"^/en/players/[a-f0-9]{8}/[A-Za-z-]+$"))
                #print(list_of_links)
                for link in list_of_links:
                    if 'href' in link.attrs:
                        player_name = link.text
                        player_link = link.attrs['href']
                        text_file.write(f"{player_name},{player_link}\n")
                        time.sleep(5)
                        response = requests.get("https://fbref.com/"+player_link)
                        soup = BeautifulSoup(response.text, 'html.parser')

                        url = "https://fbref.com"+player_link
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
                            
                    with open('PremierLeague.txt', 'a') as file:
                            file.write('\n')
                            file.write(player_name+" ")
                            for sum in summary_entries:
                                file.write(sum+" ") 
                                        
                                        

                                                                    
        


getReports()









