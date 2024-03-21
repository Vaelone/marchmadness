import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json
cnx = mysql.connector.connect(user = "wsa", host = "34.68.250.121", database = "Tutorials-Winter2024", password = "LeBron>MJ!")
cursor = cnx.cursor(buffered = True)
dicts = []
with open("2007-2009.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
with open("2010-2012.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
with open("2013-2015.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
with open("2016-2018.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
with open("2019-2022.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
with open("2023-2024.json", "r") as f:  # Replace "data.json" with your filename
    json_data = f.read()
dict1 = json.loads(json_data)
dicts.append(dict1)
for teams in dicts:
    for team in teams:
        for year in teams[team]:
            for statList in teams[team][year]:
                values = [team, year, statList[0], statList[1], statList[2]]
                inserts = [team, year, statList[0], statList[1], statList[2]]
                statement = f"INSERT INTO NCAAB_teamstats_vaelone_elankumaran (team, year, tablename, rank, value) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(statement, inserts)
                cnx.commit()
        print(team)