import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json

linkstring = ''
url = requests.get("https://www.teamrankings.com/ncaa-basketball/ranking/predictive-by-other")
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('div', attrs = {'class' : 'main-wrapper clearfix has-left-sidebar'}).find('main')
#next = table.find('li', attrs = {'class' : 'expand-section'}).find('ul', attrs = {'class' : 'expand-section'}) 
links = table.find_all('a')
skips = ['yo mama']
teams = []
cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
dates = ['2007-03-11','2008-03-16','2009-03-15'
,'2010-03-14', '2011-03-13', '2012-03-11', '2013-03-17', '2014-03-16', '2015-03-15',
         '2016-03-13', '2017-03-12', '2018-03-11', '2019-03-17', '2021-03-14', '2022-03-13', 
        '2023-03-12', '2024-03-17']
Schools = ["Connecticut", "Houston", "Purdue", "N Carolina", "Tennessee", "Arizona", "Marquette",
    "Iowa St", "Baylor", "Creighton", "Kentucky", "Illinois", "Duke", "Kansas", "Auburn",
    "Alabama", "BYU", "San Diego St", "Wisconsin", "St Marys", "Gonzaga", "Clemson",
    "Texas Tech", "S Carolina", "Florida", "Wash State", "Texas", "Dayton", "Nebraska",
    "Utah State", "Florida Atlantic", "Mississippi State", "Michigan State", "Texas A&M", "TCU",
    "Northwestern", "Nevada", "Boise St", "Colorado", "Drake", "Virginia", "New Mexico",
    "Oregon", "Colorado St", "NC State", "Duquesne", "Grd Canyon", "James Mad",
    "McNeese St", "UAB", "Vermont", "Yale", "Samford", "Col Charlestn", "Oakland", "Akron",
    "Morehead St", "Colgate", "Lg Beach St", "W Kentucky", "S Dakota St",
    "St Peters", "Longwood", "Stetson", "Montana St", "Grambling St", "Howard", "Wagner"]
stats = ["Predictive Power Rating", "Strength of Schedule Power Rating", "Last 5 Games Power Rating",
          "Last 10 Games Power Rating", "Luck Power Rating", "Consistency Power Rating", "Vs. Teams 1-25 Power Rating",
            "Vs. Teams 26-50 Power Rating", "Vs. Teams 51-100 Power Rating"]
for date in dates:
    for link in links:
            linkstring = link.get('href')
            if linkstring == '#':
                category = link.get_text(strip=True)
                continue
            else:
                tablename = link.get_text(strip=True)
                if tablename not in stats:
                    continue
            year = date[:4]
            urlstring = f"https://www.teamrankings.com{linkstring}?date={date}"
            url = requests.get(urlstring)

            soup = BeautifulSoup(url.text, 'html.parser')

            table = soup.find('table')

            tableRows = table.find_all('tr')
            #print (table)
            #print(tableRows)

            for row in tableRows:
                #print (row)
                #print ("-----------")


                columns = row.find_all("td")
                if len (columns) > 0:
                    try:
                        team = columns[1].find('a').text
                    except AttributeError:
                        # If the 'a' tag doesn't exist, continue to the next iteration
                        continue
                
                    team = columns[1].find('a').text
                    if team not in Schools:
                        continue
                        
                    rating = str(columns[2].text)

                    inserts = [team, year, tablename, rating]
                    statement = f"INSERT INTO NCAAB_otherteamstats_0724_nathan_dsouza (team, year, tablename, value) VALUES (%s, %s, %s, %s)"
                    cursor.execute(statement, inserts)
                    cnx.commit()
    print(date)
                    
