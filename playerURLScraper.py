from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def getReports():
    # Open the URL and extract the HTML and write it to a new file
    html = urlopen('https://fbref.com/en/comps/9/stats/Premier-League-Stats')
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
        with open('player_profiles.txt', 'w') as text_file:
            text_file.write("Name\tLink\n")  # Header

            for content in table_contents:
                list_of_links = content.find_all('a', href=re.compile(r"^/en/players/[a-f0-9]{8}/[A-Za-z-]+$"))
                for link in list_of_links:
                    if 'href' in link.attrs:
                        player_name = link.text
                        player_link = link.attrs['href']
                        text_file.write(f"{player_name}\t{player_link}\n")

getReports()

# Since some players have non-English letters in their names like 'ø' for 'o' etc.,
# this code replaces such letters with corresponding English letters
# (Note: The below code is unchanged from your original)
def name_updater():
    count = 1
    # Your existing function here...
    # No changes were made to this function in the provided rewrite

name_updater()
