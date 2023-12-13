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
        with open('player_profiles.csv', 'w') as text_file:
            text_file.write("Name\tLink\n")  # Header


            for content in table_contents:
                list_of_links = content.find_all('a', href=re.compile(r"^/en/players/[a-f0-9]{8}/[A-Za-z-]+$"))
                for link in list_of_links:
                    if 'href' in link.attrs:
                        player_name = link.text
                        player_link = link.attrs['href']
                        text_file.write(f"{player_name},{player_link}\n")
                        time.sleep(5)
                        response = requests.get("https://fbref.com/"+player_link)
                        soup = BeautifulSoup(response.text, 'html.parser')

                        





                      


                        

                        summary_table = soup.find('table', {'id': 'stats_standard_dom_lg'}) 
                        summary_table_foot = summary_table.find_all('tfoot')
                        for tfoot in summary_table_foot:
                            summary_table_bottom_row = tfoot.find('tr')
                        summary = [td for td in summary_table_bottom_row if 'group_start' in td.get('class', []) and 'right' in td.get('class', [])] 


                        shooting_table = soup.find('table', {'id': 'stats_shooting_dom_lg'}) 
                        shooting_table_foot = shooting_table.find_all('tfoot')
                        for tfoot in shooting_table_foot:
                            shooting_table_bottom_row = tfoot.find('tr')
                        shooting_stats = [td for td in shooting_table_bottom_row if 'group_start' in td.get('class', []) and 'right' in td.get('class', []) and 'player_stats_summary_explain' not in td.get('class', [])  and 'comp_level' not in td.get('class', [])]


                        defensive_actions_table = soup.find('table', {'id': 'stats_defense_dom_lg'}) 
                        defensive_actions_table_foot = defensive_actions_table.find_all('tfoot')
                        for tfoot in defensive_actions_table_foot:
                            defensive_actions_table_bottom_row = tfoot.find('tr')
                        defensive_actions = [td for td in defensive_actions_table_bottom_row if 'group_start' in td.get('class', []) and 'right' in td.get('class', []) and 'player_stats_summary_explain' not in td.get('class', [])  and 'comp_level' not in td.get('class', [])]
                        


                        possesion_table = soup.find('table', {'id': 'stats_possession_dom_lg'}) 
                        possesion_table_foot = possesion_table.find_all('tfoot')
                        for tfoot in possesion_table_foot:
                            possesion_table_bottom_row = tfoot.find('tr')
                        possesion = [td for td in possesion_table_bottom_row if 'player_stats_summary_explain' not in td.get('data-stat', [])  and 'team' not in td.get('data-stat', []) and 'comp_level' not in td.get('data-stat', [])]
            




                        






                        passing_table = soup.find('table', {'id': 'stats_passing_dom_lg'})
                        passing_table_foot = passing_table.find_all('tfoot')
                        for tfoot in passing_table_foot:
                            passing_table_bottom_row = tfoot.find('tr')
                        passing_stats = [td for td in passing_table_bottom_row if 'player_stats_summary_explain' not in td.get('data-stat', [])  and 'team' not in td.get('data-stat', []) and 'comp_level' not in td.get('data-stat', [])]
                        for td in passing_stats:
                            counter = counter + 1
                            if 'passes' in td.get('data-stat', []) and 'right' in td.get('class') and counter == 1:
                                completed_passes = td.text
                            if 'passes' in td.get('data-stat', []) and 'right' in td.get('class') and counter2 == 2:
                                completed_passes = td.text


                        goal_and_shots_table = soup.find('table', {'id': 'stats_gca_dom_lg'})
                        goal_and_shots_table_foot = goal_and_shots_table.find_all('tfoot')
                        for tfoot in goal_and_shots_table_foot:
                            goal_and_shots_table_foot_bottom_row = tfoot.find('tr')
                        goal_and_shots = [td for td in goal_and_shots_table_foot_bottom_row if  'team' not in td.get('data-stat', [])  and 'player_stats_summary_explain' not in td.get('data-stat', [])  and 'comp_level' not in td.get('class', []) and 'player_stats_summary_explain' not in td.get('class', [])  and 'comp_level' not in td.get('data-stat', []) and 'comp_level' not in td.get('data-stat', [])]
                        



                        type_pass_table = soup.find('table', {'id': 'stats_passing_types_dom_lg'}) 
                        type_passing_table_foot = type_pass_table.find_all('tfoot')
                        for tfoot in type_passing_table_foot:
                            type_passing_table_bottom_row = tfoot.find('tr')
                        type_passing_stats = [td for td in type_passing_table_bottom_row if 'team' not in td.get('data-stat', []) and 'Seasons' not in td.getText()  and 'comp_level' not in td.get('data-stat', [])] 


                        misc_table = soup.find('table', {'id': 'stats_misc_dom_lg'}) 
                        misc_table_foot = misc_table.find_all('tfoot')
                        for tfoot in misc_table_foot:
                            misc_table_bottom_row = tfoot.find('tr')
                        misc_stats = [td for td in misc_table_bottom_row if 'team' not in td.get('data-stat', []) and 'player_stats_summary_explain' not in td.get('data-set', [])  and 'comp_level' not in td.get('data-stat', []) and 'Seasons' not in td.getText()]

                        

                        output = f"{player_name},"

                        # Concatenating elements only if they are non-empty
                        output += ','.join(td.text.strip()  for td in summary_table_bottom_row if td.text.strip())
                        output += ','.join(td.text.strip()  for td in shooting_stats if td.text.strip())
                        output += ','.join(td.text.strip()  for td in passing_stats if td.text.strip())
                        output += ','.join(td.text.strip()  for td in type_passing_stats if td.text.strip())
                        output += ','.join(td.text.strip()  for td in goal_and_shots if td.text.strip())
                        output += ','.join(td.text.strip()  for td in defensive_actions if td.text.strip())
                        output += ','.join(td.text.strip()  for td in possesion if td.text.strip())
                        output += ','.join(td.text.strip()  for td in misc_stats if td.text.strip())

                        # Removing the trailing comma if present
                        output = output.rstrip(',')
                        print(output)

                        with open('PremierLeague.csv', 'a') as file:
                            file.write(output + '\n')

                      
                        
                       
                

                        
                        
                        
                                

                

                    




getReports()

# Since some players have non-English letters in their names like 'ø' for 'o' etc.,
# this code replaces such letters with corresponding English letters
# (Note: The below code is unchanged from your original)
def name_updater():
    count = 1
    # Your existing function here...
    # No changes were made to this function in the provided rewrite

name_updater()
