import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json
Schools18 = [
    "Villanova", "Radford", "Purdue", "Cal State Fullerton", "Texas Tech", "Stephen F. Austin", 
    "Marshall", "Wichita State", "West Virginia", "Murray State", "Florida", "St. Bonaventure", 
    "Butler", "Arkansas", "Alabama", "Virginia Tech",
    "Xavier", "Texas Southern", "North Carolina", "Lipscomb", "Michigan", "Montana", "Gonzaga", 
    "UNC Greensboro", "Ohio State", "South Dakota State", "Houston", "San Diego State", 
    "Texas A&M", "Providence", "Florida State", "Missouri", "UMBC", "Virginia", "Cincinnati", 
    "Georgia State", "Tennessee", "Wright State", "Buffalo", "Arizona", "Kentucky", "Davidson", 
    "Loyola Chicago", "Miami (Fla.)", "Nevada", "Texas", "Kansas State", "Creighton", "Kansas", 
    "Pennsylvania", "Duke", "Iona", "Michigan State", "Bucknell", "Auburn", "College of Charleston", 
    "Clemson", "New Mexico State", "Syracuse", "TCU", "Rhode Island", "Oklahoma", "Seton Hall", 
    "NC State"
]

team_dict18 = {team: 0 for team in Schools18}

Schools19 = [
    "Duke", "North Dakota State", "Michigan State", "Bradley", "LSU", "Yale", 
    "Virginia Tech", "Saint Louis", "Liberty", "Mississippi State", "Maryland", "Belmont", 
    "Minnesota", "Louisville", "UCF", "VCU",
    "Gonzaga", "Fairleigh Dickinson", "Michigan", "Montana", "Texas Tech", "Northern Kentucky", 
    "Florida State", "Vermont", "Murray State", "Marquette", "Buffalo", "Arizona State", 
    "Florida", "Nevada", "Baylor", "Syracuse",
    "Virginia", "Gardner-Webb", "Tennessee", "Colgate", "Purdue", "Old Dominion", "UC Irvine", 
    "Kansas State", "Oregon", "Wisconsin", "Villanova", "Saint Mary's", "Iowa", "Temple", 
    "Oklahoma", "Ole Miss",
    "North Carolina", "Iona", "Kentucky", "Abilene Christian", "Houston", "Georgia State", 
    "Kansas", "Northeastern", "Auburn", "New Mexico State", "Ohio State", "Iowa State", 
    "Wofford", "Seton Hall", "Washington", "Utah State"
]

team_dict19 = {team: 0 for team in Schools19}


Schools21 = [
    "Illinois", "Drexel", "Loyola Chicago", "Georgia Tech", "Oregon St.", "Tennessee", 
    "Oklahoma St.", "Liberty", "Syracuse", "San Diego St.", "West Virginia", "Morehead St.", 
    "Rutgers", "Clemson", "Houston", "Cleveland St.", "Gonzaga", "Norfolk St.", "Oklahoma", 
    "Missouri", "Creighton", "UCSB", "Ohio", "Virginia", "USC", "Drake", "Kansas", 
    "Eastern Wash.", "Oregon", "VCU", "Iowa", "Grand Canyon", "Michigan", "Texas Southern", 
    "LSU", "St. Bonaventure", "Colorado", "Georgetown", "Florida St.", "UNC Greensboro", 
    "UCLA", "BYU", "Abilene Christian", "Texas", "Maryland", "UConn", "Alabama", "Iona", 
    "Baylor", "Hartford", "Wisconsin", "North Carolina", "Villanova", "Winthrop", "North Texas", 
    "Purdue", "Texas Tech", "Utah St.", "Arkansas", "Colgate", "Florida", "Virginia Tech", 
    "Oral Roberts", "Ohio State"
]

team_dict21 = {team: 0 for team in Schools21}

Schools22 = [
    "Kansas", "Texas Southern", "Creighton", "San Diego St.", "Richmond", "Iowa", "Providence", 
    "S. Dakota St.", "Iowa St.", "LSU", "Wisconsin", "Colgate", "Miami (FL)", "USC", "Auburn", 
    "Jacksonville St.", "Gonzaga", "Georgia St.", "Memphis", "Boise St.", "New Mexico St.", 
    "UConn", "Arkansas", "Vermont", "Notre Dame", "Alabama", "Texas Tech", "Montana St.", 
    "Michigan St.", "Davidson", "Duke", "Cal St. Fullerton", "Baylor", "Norfolk St.", 
    "North Carolina", "Marquette", "Saint Mary’s", "Indiana", "UCLA", "Akron", "Texas", 
    "Virginia Tech", "Purdue", "Yale", "Murray St.", "San Francisco", "St. Peter’s", "Kentucky",
     "Arizona", "Wright St.", "TCU", "Seton Hall", "Houston", "UAB", "Illinois", "Chattanooga", 
    "Michigan", "Colorado St.", "Tennessee", "Longwood", "Ohio St.", "Loyola Chicago", 
    "Villanova", "Delaware"
]

team_dict22 = {team: 0 for team in Schools22}

Schools23 = [
    "Houston", "North Kentucky", "Auburn", "Iowa", "Miami (FL)", "Drake", "Indiana", "Kent St.", 
    "Pitt", "Iowa St.", "Xavier", "Kennesaw St.", "Penn St.", "Texas A&M", "Texas", "Colgate", 
    "Kansas", "Howard", "Arkansas", "Illinois", "St. Mary’s", "VCU", "UConn", "Iona", 
    "TCU", "Arizona St.", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St.", "UCLA", 
    "UNC Asheville", "FDU", "Purdue", "FAU", "Memphis", "Duke", "Oral Roberts", "Tennessee", 
    "Louisiana", "Kentucky", "Providence", "Kansas St.", "Montana St.", "Michigan St.", 
    "USC", "Marquette", "Vermont", "Alabama", "Texas A&M-CC", "Maryland", "West Virginia", 
    "San Diego St.", "Col of Charleston", "Furman", "Virginia", "Creighton", "NC State", 
    "Baylor", "UCSB", "Missouri", "Utah St.", "Princeton", "Arizona"
]

team_dict23 = {team: 0 for team in Schools23}
cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
url = requests.get('https://www.ncaa.com/news/basketball-men/article/2023-04-18/2023-ncaa-bracket-scores-stats-march-madness-mens-tournament')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
filtered_games = [game for game in gameswithupsets if starts_with_no(game.split("||")[0].strip()) and "||" in game]
games = []
for game in filtered_games:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2023 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools23:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2022-07-12/2022-ncaa-bracket-mens-march-madness-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2022 '
team_frequency['North Carolina'] = 5
team_frequency['Miami (FL)'] = 3
del team_frequency['Miami']
del team_frequency['N. Carolina']
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools22:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2022-07-20/2021-ncaa-bracket-scores-stats-records-march-madness-mens-tournament')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
filtered_games = [game for game in gameswithupsets if starts_with_no(game.split("||")[0].strip()) and "||" in game]
games = []
for game in filtered_games:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2021 '
team_frequency['Loyola Chicago'] = 2
del team_frequency['Loyola Chi.']
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools21:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-06/2019-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2019 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools19:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-06/2018-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2018 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools18:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1823_vaelone_elankumaran (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()