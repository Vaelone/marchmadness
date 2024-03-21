import requests
from bs4 import BeautifulSoup
import mysql.connector

Schools07 = [
    "North Carolina", "Eastern Kentucky", "Michigan State", "Marquette", "USC", "Arkansas",
    "Texas", "New Mexico State", "Vanderbilt", "George Washington", "Washington State", "Oral Roberts",
    "Boston College", "Texas Tech", "Georgetown", "Belmont", "Florida", "Jackson State",
    "Purdue", "Arizona", "Butler", "Old Dominion", "Maryland", "Davidson",
    "Winthrop", "Notre Dame", "Oregon", "Miami (Ohio)", "UNLV", "Georgia Tech",
    "Wisconsin", "Texas A&M-Corpus Christi", "Ohio State", "Central Connecticut State", "Xavier", "BYU",
    "Tennessee", "Long Beach State", "Virginia", "Albany", "Louisville", "Stanford",
    "Texas A&M", "Penn", "Nevada", "Creighton", "Memphis", "North Texas", "Kansas", "Niagara",
    "Kentucky", "Villanova", "Virginia Tech", "Illinois", "Southern Illinois", "Holy Cross",
    "VCU", "Duke", "Pittsburgh", "Wright State", "Indiana", "Gonzaga", "UCLA", "Weber State"
]
team_dict07 = {team:0 for team in Schools07}

Schools08 = [
    "North Carolina", "Mount St. Mary's", "Arkansas", "Indiana", "Notre Dame", "George Mason",
    "Washington State", "Winthrop", "Oklahoma", "St. Joseph's", "Louisville", "Boise State",
    "Butler", "South Alabama", "Tennessee", "American", "Kansas", "Portland State", "UNLV", "Kent State",
    "Villanova", "Clemson", "Siena", "Vanderbilt", "Kansas State", "USC", "Wisconsin", "Cal State Fullerton",
    "Davidson", "Gonzaga", "Georgetown", "UMBC", "Memphis", "Texas-Arlington", "Mississippi State", "Oregon",
    "Michigan State", "Temple", "Pittsburgh", "Oral Roberts", "Marquette", "Kentucky", "Stanford", "Cornell",
    "Miami (FL)", "Saint Mary's", "Texas", "Austin Peay", "UCLA", "Mississippi Valley State", "Texas A&M", "BYU",
    "Western Kentucky", "Drake", "San Diego", "UConn", "Purdue", "Baylor", "Xavier", "Georgia",
    "West Virginia", "Arizona", "Duke", "Belmont"
]

team_dict08 = {team: 0 for team in Schools08}

Schools09 = [
    "Pittsburgh", "East Tennessee State", "Oklahoma State", "Tennessee",
    "Wisconsin", "Florida State", "Xavier", "Portland State", "UCLA", "VCU",
    "Villanova", "American", "Texas", "Minnesota", "Duke", "Binghamton",
    "Louisville", "Morehead State", "Siena", "Ohio State", "Arizona", "Utah",
    "Cleveland State", "Wake Forest", "Dayton", "West Virginia", "Kansas",
    "North Dakota State", "USC", "Boston College", "Michigan State", "Robert Morris",
    "North Carolina", "Radford", "LSU", "Butler", "Western Kentucky", "Illinois",
    "Gonzaga", "Akron", "Arizona State", "Temple", "Syracuse", "Stephen F. Austin",
    "Michigan", "Clemson", "Oklahoma", "Morgan State", "UConn", "Chattanooga",
    "Texas A&M", "BYU", "Purdue", "Northern Iowa", "Washington", "Mississippi State",
    "Marquette", "Utah State", "Missouri", "Cornell", "Maryland", "California",
    "Memphis", "Cal State Northridge"
]

team_dict09 = {team:0 for team in Schools09}

Schools10 = [
    "Kentucky", "East Tennessee State", "West Virginia", "Morgan State", "New Mexico", "Montana",
    "Wisconsin", "Wofford", "Cornell", "Temple", "Washington", "Marquette",
    "Missouri", "Clemson", "Wake Forest", "Texas (OT)", "Syracuse", "Vermont",
    "Kansas State", "North Texas", "Pittsburgh", "Oakland", "Murray State", "Vanderbilt",
    "Butler", "UTEP", "Xavier", "Minnesota", "BYU", "Florida (2OT)",
    "Gonzaga", "Florida State", "Duke", "Arkansas-Pine Bluff", "Villanova", "Robert Morris (OT)",
    "Baylor", "Sam Houston State", "Purdue", "Siena", "Texas A&M", "Utah State",
    "Old Dominion", "Notre Dame", "Saint Mary's", "Richmond", "California", "Louisville",
    "Kansas", "Lehigh", "Ohio State", "UC Santa Barbara", "Ohio", "Georgetown",
    "Maryland", "Houston", "Michigan State", "New Mexico State", "Tennessee", "San Diego State",
    "Georgia Tech", "Oklahoma State", "Northern Iowa", "UNLV"
]

team_dict10 = {team: 0 for team in Schools10}

Schools11 = [
    "Ohio State", "UTSA", "North Carolina", "Long Island", "Syracuse", "Indiana State",
    "Kentucky", "Princeton", "West Virginia", "Clemson", "Marquette", "Xavier",
    "Washington", "Georgia", "George Mason", "Villanova", "Duke", "Hampton",
    "San Diego State", "Northern Colorado", "UConn", "Bucknell", "Texas", "Oakland",
    "Arizona", "Memphis", "Cincinnati", "Missouri", "Temple", "Penn State",
    "Michigan", "Tennessee", "Kansas", "Boston University", "Notre Dame", "Akron",
    "Purdue", "Saint Peter's", "Morehead State", "Louisville", "Richmond", "Vanderbilt",
    "VCU", "Georgetown", "Florida State", "Texas A&M", "Illinois", "UNLV",
    "Pitt", "UNC Asheville", "Florida", "UC Santa Barbara", "BYU", "Wofford",
    "Wisconsin", "Belmont", "Kansas State", "Utah State", "Gonzaga", "St. John's",
    "UCLA", "Michigan State", "Butler", "Old Dominion"
]

team_dict11 = {team: 0 for team in Schools11}


Schools12 = [
    "Syracuse", "UNC Asheville", "Ohio State", "Loyola (Md.)", "Florida State", "St. Bonaventure",
    "Wisconsin", "Montana", "Vanderbilt", "Harvard", "Cincinnati", "Texas", "Gonzaga", "West Virginia",
    "Kansas State", "Southern Miss", "Michigan State", "Long Island", "Norfolk State", "Missouri",
    "Marquette", "BYU", "Louisville", "Davidson", "New Mexico", "Long Beach State", "Murray State",
    "Colorado State", "Florida", "Virginia", "Saint Louis", "Memphis", "Kentucky", "Western Kentucky",
    "Lehigh", "Duke", "Baylor", "South Dakota State", "Indiana", "New Mexico State", "VCU", "Wichita State",
    "Colorado", "UNLV", "Xavier", "Notre Dame", "Iowa State", "UConn", "North Carolina", "Vermont",
    "Kansas", "Detroit", "Georgetown", "Belmont", "Ohio", "Michigan", "South Florida", "Temple", "NC State",
    "San Diego State", "Purdue", "Saint Mary's", "Creighton", "Alabama"
]

team_dict12 = {team: 0 for team in Schools12}

cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-07/2007-ncaa-tournament-bracket-scores-stats-records')
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
year = '2007 '
del team_frequency['Niagara']
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools07:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-07/2008-ncaa-tournament-bracket-scores-stats-records')
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
year = '2008 '
del team_frequency["Mount St. Mary's"]
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools08:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-06/2009-ncaa-tournament-bracket-scores-stats-rounds')
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
year = '2009 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools09:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-12/2010-ncaa-tournament-bracket-scores-stats-records')
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
year = '2010 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools10:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()
    
url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-05/2011-ncaa-tournament-bracket-scores-stats-records')
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
year = '2011 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()
for school in Schools11:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()
    
url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-11/2012-ncaa-tournament-bracket-scores-stats-records')
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
year = '2012 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
    cursor.execute(statement, inserts)
    cnx.commit()

for school in Schools12:
    if school not in team_frequency:
        yearteam = year + str(school)
        inserts = [yearteam, 0]
        statement = f"INSERT INTO NCAAB0712_steven_lan (team, wins) VALUES (%s, %s)"
        cursor.execute(statement, inserts)
        cnx.commit()