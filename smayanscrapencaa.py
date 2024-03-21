import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json
Schools13 = [
    "Louisville", "North Carolina A&T", "Duke", "Albany", "Michigan State", "Valparaiso",
    "Saint Louis", "New Mexico State", "Oregon", "Oklahoma State", "Memphis", "Saint Mary's",
    "Creighton", "Cincinnati", "Colorado State", "Missouri", "Gonzaga", "Southern", "Ohio State",
    "Iona", "Harvard", "New Mexico", "La Salle", "Kansas State", "Ole Miss", "Wisconsin", "Arizona",
    "Belmont", "Iowa State", "Notre Dame", "Wichita State", "Pittsburgh", "Indiana", "James Madison",
    "Miami (Fla.)", "Pacific", "Marquette", "Davidson", "Syracuse", "Montana", "California", "UNLV",
    "Butler", "Bucknell", "Illinois", "Colorado", "Temple", "NC State", "Kansas", "Western Kentucky",
    "Florida Gulf Coast", "Georgetown", "Florida", "Northwestern State", "Michigan", "South Dakota State",
    "VCU", "Akron", "Minnesota", "UCLA", "San Diego State", "Oklahoma", "North Carolina", "Villanova"
]

team_dict13 = {team: 0 for team in Schools13}

Schools14 = [
    "Wichita State", "Cal Poly", "Michigan", "Wofford", "Mercer", "Duke", "Louisville", "Manhattan",
    "Saint Louis", "NC State", "Tennessee", "UMass", "Texas", "Arizona State", "Kentucky", "Kansas State",
    "Arizona", "Weber State", "Wisconsin", "American", "Creighton", "Louisiana", "San Diego State",
    "New Mexico State", "North Dakota State", "Oklahoma", "Baylor", "Nebraska", "Oregon", "BYU",
    "Gonzaga", "Oklahoma State", "Virginia", "Coastal Carolina", "Villanova", "Milwaukee", "Iowa State",
    "North Carolina Central", "Michigan State", "Delaware", "Harvard", "Cincinnati", "North Carolina",
    "Providence", "UConn", "Saint Joseph's", "Memphis", "George Washington", "Florida", "Albany",
    "Kansas", "Eastern Kentucky", "Syracuse", "Western Michigan", "UCLA", "Tulsa", "Stephen F. Austin",
    "VCU", "Dayton", "Ohio State", "Stanford", "New Mexico", "Pittsburgh", "Colorado"
]

team_dict14 = {team: 0 for team in Schools14}

Schools15 = [
    "Kentucky", "Hampton", "Kansas", "New Mexico State", "Notre Dame", "Northeastern", "Maryland", "Valparaiso", 
    "West Virginia", "Buffalo", "Butler", "Texas", "Wichita State", "Indiana", "Cincinnati", "Purdue", "Wisconsin", 
    "Coastal Carolina", "Arizona", "Texas Southern", "Georgia State", "Baylor", "North Carolina", "Harvard", "Arkansas", 
    "Wofford", "Xavier", "Ole Miss", "Ohio State", "VCU", "Oregon", "Oklahoma State", "Villanova", "Lafayette", "Virginia", 
    "Belmont", "Oklahoma", "Albany", "Louisville", "UC Irvine", "Northern Iowa", "Wyoming", "Dayton", "Providence", 
    "Michigan State", "Georgia", "NC State", "LSU", "Duke", "Robert Morris", "Gonzaga", "North Dakota State", "UAB", 
    "Iowa State", "Georgetown", "Eastern Washington", "Utah", "Stephen F. Austin", "UCLA", "SMU", "Iowa", "Davidson", 
    "San Diego State", "St. John's"
]

team_dict15 = {team: 0 for team in Schools15}

Schools16 = [
    "North Carolina", "Florida Gulf Coast", "Xavier", "Weber State", "Stephen F. Austin", "West Virginia",
    "Kentucky", "Stony Brook", "Indiana", "Chattanooga", "Notre Dame", "Michigan",
    "Wisconsin", "Pittsburgh", "Providence", "Southern California", "Oregon", "Holy Cross",
    "Oklahoma", "Cal State Bakersfield", "Texas A&M", "Green Bay", "Duke", "UNC Wilmington",
    "Yale", "Baylor", "Northern Iowa", "Texas", "VCU", "Oregon State",
    "Saint Joseph's", "Cincinnati", "Kansas", "Austin Peay", "Villanova", "UNC Asheville",
    "Miami (Fla.)", "Buffalo", "Hawai'i", "California", "Maryland", "South Dakota State",
    "Wichita State", "Arizona", "Iowa", "Temple", "UConn", "Colorado",
    "Virginia", "Hampton", "Middle Tennessee", "Michigan State", "Utah", "Fresno State",
    "Iowa State", "Iona", "Little Rock", "Purdue", "Gonzaga", "Seton Hall",
    "Syracuse", "Dayton", "Butler", "Texas Tech"
]

team_dict16 = {team: 0 for team in Schools16}

Schools17 = [
    "Villanova", "Mount St. Mary's", "Duke", "Troy", "Baylor", "New Mexico State", "Florida", "East Tennessee State",
    "Virginia", "UNC Wilmington", "Southern California", "SMU", "South Carolina", "Marquette", "Wisconsin", "Virginia Tech",
    "Gonzaga", "South Dakota State", "Arizona", "North Dakota", "Florida State", "Florida Gulf Coast", "West Virginia", "Bucknell",
    "Notre Dame", "Princeton", "Xavier", "Maryland", "Saint Mary's", "VCU", "Northwestern", "Vanderbilt",
    "North Carolina", "Texas Southern", "Kentucky", "Northern Kentucky", "UCLA", "Kent State", "Butler", "Winthrop",
    "Middle Tennessee", "Minnesota", "Cincinnati", "Kansas State", "Wichita State", "Dayton", "Arkansas", "Seton Hall",
    "Kansas", "UC Davis", "Louisville", "Jacksonville State", "Oregon", "Iona", "Purdue", "Vermont",
    "Iowa State", "Nevada", "Rhode Island", "Creighton", "Michigan", "Oklahoma State", "Michigan State", "Miami (Fla.)"
]

team_dict17 = {team: 0 for team in Schools17}
cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-06/2017-ncaa-tournament-bracket-scores-stats-records')
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
year = '2017 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools17:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-07/2016-ncaa-tournament-bracket-scores-stats-records')
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
year = '2016 '
team_frequency['Notre Dame'] = 3
del team_frequency['Notre']
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools16:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-08/2015-ncaa-tournament-bracket-scores-stats-records')
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
year = '2015 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools15:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-10/2014-ncaa-tournament-bracket-scores-stats-records')
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
year = '2014 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools14:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()



url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-11/2013-ncaa-tournament-bracket-scores-stats-records')
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
year = '2013 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools13:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB1317_smayan_ranjan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()
