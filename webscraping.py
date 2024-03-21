import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json

url = requests.get('https://www.teamrankings.com/ncb/team-stats/')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('div', attrs = {'class' : 'main-wrapper clearfix has-left-sidebar'}).find('main')
#next = table.find('li', attrs = {'class' : 'expand-section'}).find('ul', attrs = {'class' : 'expand-section'}) 
links = table.find_all('a')
# dates = ['2002-03-10', '2003-03-16','2004-03-14','2005-03-13',
#         '2006-03-12','2007-03-11','2008-03-16','2009-03-15'
# ,'2010-03-14', '2011-03-13', '2012-03-11', '2013-03-17', '2014-03-16', '2015-03-15',
#          '2016-03-13', '2017-03-12', '2018-03-11', '2019-03-17', '2021-03-14', '2022-03-13', 
#         '2023-03-12', '2024-03-17']
# '1998-03-08', '1999-03-07', '2000-03-12', '2001-03-11', 
dates = ['2023-03-12', '2024-03-17']
category = "empty"
cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
skips = ['Average Scoring Margin', '1st Half Points per Game', '2nd Half Points per Game', 'Average Overtime Margin', 'Points from 2 Pointers', 
         'Points from 3 Pointers',
         'Effective Field Goal %',  'Non-blocked 2 Pt %', 
          'Offensive Rebounds per Game', 'Defensive Rebounds per Game', 
          'Team Rebounds per Game', 'Total Rebounds per Game', 'Blocks per Game', 'Steals per Game', 'Assists per Game',
          'Turnovers per Game', 'Personal Fouls per Game', 'Opponent Average Scoring Margin', 'Opponent 1st Half Points Per Game'
          ,'Opponent 2nd Half Points per Game', 'Opponent Overtime Points per Game', 'Opponent Points from 2 Pointers',
          'Opponent Points from 3 Pointers', 'Opponent Effective Field Goal %', 'Opponent Field Goals Made per Game', 
          'Opponent Field Goals Attempted per Game', 'Opponent Three Pointers Made per Game','Opponent Three Pointers Attempted per Game',
            'Opponent Free Throws Attempted per Game', 'Opponent Free Throws Made per Game', 'Opponent Non-blocked 2 Pt %', 
            'Opponent Offensive Rebounds per Game','Opponent Defensive Rebounds per Game',
           'Opponent Team Rebounds per Game', 'Opponent Total Rebounds per Game', 'Opponent Offensive Rebounding %', 
          'Opponent Defensive Rebounding %', 'Opponent Blocks per Game', 'Opponent Steals per Game', 'Opponent Assists per Game',
           'Opponent Turnovers per Game', 'Opponent Personal Fouls per Game', 'Games Played', 
           'Opponent Win % - All Games', 'Opponent Win % - Close Games']
#Need to adjust the columns for shooting and shooting defense
teams = {}
for date in dates:
    for link in links:
        linkstring = link.get('href')
        if linkstring == '#':
            category = link.get_text(strip=True)
            continue
        else:
            tablename = link.get_text(strip=True)
            if tablename in skips:
                continue
        year = date[:4]
        # At this point we have a var category containing the overarching categories like shooting, passing, etc
        # We also have a var tablename that contains the name of the current table
        # Finally we have a year variable. These are also useful for the naming conventions for SQL
        urltext = f"https://www.teamrankings.com{linkstring}?date={date}"
        url = requests.get(urltext)
        soup = BeautifulSoup(url.text, 'html.parser')
        # print(soup.prettify())
        
        table = soup.find('table')
        if table is None:
            print('Fail')
            print(date)
            print(tablename)
            continue
        else:
            tableRows = table.find_all('tr')
            
        #print(tableRows)
        
    
        # print(table)
        for row in tableRows:
            #print(row)
            #print("----------------")
            
            columns = row.find_all("td")
            if len(columns) > 0:
            
                rank = int(columns[0].text)
                a_tag = columns[1].find('a')
                if a_tag:
                    # Extract the text if 'a' tag is present
                    team = a_tag.text
                else:
                    # Handle the case where 'a' tag is not present
                    team = columns[1].text
                value = columns[2].text
                # we are getting multiple data points of interest from this single column so we must split it
                if team in teams:
                    # Check if the year exists for that team
                    if year in teams[team]:
                        # Append table_name, rank, and value to the list
                        teams[team][year].append([tablename, rank, value])
                    else:
                        # Create a new inner dictionary for the year
                        teams[team][year] = [[tablename, rank, value]]
                else:
                    # Create a new entry for the team and initialize it with the inner dictionary for that year
                    teams[team] = {year: [[tablename, rank, value]]}
                            # inserts = [year, rank, team, value]
                            # statement = f"INSERT INTO '{category}/{tablename}(year, rank, team, values) VALUES (%s, %s, %s, %s)'" 
    print(date + ' complete')       
json_string = json.dumps(teams)    
with open("2023-2024.json", "w") as f:
  f.write(json_string)  
#df = pd.DataFrame.from_dict(teams, orient='index')
#count = 0``
# for team in teams:
#     for year in teams[team]:
#         for statList in teams[team][year]:
#             values = [team, year, statList[0], statList[1], statList[2]]
#             inserts = [team, year, statList[0], statList[1], statList[2]]
#             statement = f"INSERT INTO NCAAB_teamstats_2001_2003_vaelone_elankumaran (team, year, tablename, rank, value) VALUES (%s, %s, %s, %s, %s)"
#             cursor.execute(statement, inserts)
#             cnx.commit()
#     print(team)