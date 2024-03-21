import pandas as pd
import numpy as np
import re

teamstats1 = pd.read_csv('NCAAB_teamstats_vaelone_elankumaran.csv')
teamstats2 = pd.read_csv('NCCAB_otherteamstats_0724_nathan_dsouza.csv')
teamwins = pd.read_csv('NCAAB1823_vaelone_elankumaran.csv')
del teamstats1['id']
del teamstats1['rank']
del teamstats2['id']
teamstats= pd.concat([teamstats1, teamstats2], ignore_index=True)
del teamwins['id']
teamstats['year'] = teamstats['year'].astype(str)
teamwins['team'] = teamwins['team'].str.replace(r'St\. Joseph.*', 'St. Josephs')
teamwins['team'] = teamwins['team'].str.replace(r'Saint Peter.*', 'St Peters')
teamwins['team'] = teamwins['team'].str.replace(r'St\. John.*', 'St Johns')
teamwins['team'] = teamwins['team'].str.replace('Michigan State', 'Michigan St.')
teamwins['team'] = teamwins['team'].str.replace('Ohio State', 'Ohio St.')
teamwins['team'] = teamwins['team'].str.replace('Florida State', 'Florida St.')
teamwins['team'] = teamwins['team'].str.replace('Kansas State', 'Kansas St.')
teamwins['team'] = teamwins['team'].str.replace('Murray State', 'Murray St.')
teamwins['team'] = teamwins['team'].str.replace(r'St\. Mary.*', 'St. Mary')
teamwins['team'] = teamwins['team'].str.replace(r'St\. Peter.*', 'St. Peter')
teamwins['team'] = teamwins['team'].str.replace(r'Saint Mary.*', 'Saint Mary')
teamwins['team'] = teamwins['team'].str.replace("St. Mary", "St Marys")
teamwins['team'] = teamwins['team'].str.replace("St. Peter", "St Peters")
teamwins['team'] = teamwins['team'].str.replace('North Carolina A&T', 'NC A&T')
teamwins['team'] = teamwins['team'].str.replace('New Mexico State', 'N Mex State')
teamwins['team'] = teamwins['team'].str.replace('Northwestern State', 'NW State')
teamwins['team'] = teamwins['team'].str.replace('Coastal Carolina', 'Coastal Car')
teamwins['team'] = teamwins['team'].str.replace('Miami (Fla.)', 'Miami')
teamwins['team'] = teamwins['team'].str.replace('South Dakota State', 'S Dakota St')
teamwins['team'] = teamwins['team'].str.replace('Texas Southern', 'TX Southern')
teamwins['team'] = teamwins['team'].str.replace('Saint Mary', 'St Marys')
teamwins['team'] = teamwins['team'].str.replace('George Washington', 'Geo Wshgtn')
teamwins['team'] = teamwins['team'].str.replace('SMU', 'S Methodist')
teamwins['team'] = teamwins['team'].str.replace('Fresno State', 'Fresno St')
teamwins['team'] = teamwins['team'].str.replace('UNC Asheville', 'NC-Asheville')
teamwins['team'] = teamwins['team'].str.replace('James Madison', 'James Mad')
teamwins['team'] = teamwins['team'].str.replace('Kent State', 'Kent St')
teamwins['team'] = teamwins['team'].str.replace('St. John\'s', 'St Johns')
teamwins['team'] = teamwins['team'].str.replace('UMass', 'U Mass')
teamwins['team'] = teamwins['team'].str.replace('Jacksonville State', 'Jksnville St')
teamwins['team'] = teamwins['team'].str.replace('Jacksonville St.', 'Jksnville St')
teamwins['team'] = teamwins['team'].str.replace('UNC Wilmington', 'NC-Wilmgton')
teamwins['team'] = teamwins['team'].str.replace('Northeastern', 'Northeastrn')
teamwins['team'] = teamwins['team'].str.replace('Cal State Bakersfield', 'CS Bakersfld')
teamwins['team'] = teamwins['team'].str.replace('Eastern Kentucky', 'E Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Robert Morris', 'Rob Morris')
teamwins['team'] = teamwins['team'].str.replace('Green Bay', 'WI-Grn Bay')
teamwins['team'] = teamwins['team'].str.replace('North Carolina Central', 'NC Central')
teamwins['team'] = teamwins['team'].str.replace('Weber State', 'Weber St')
teamwins['team'] = teamwins['team'].str.replace('Oklahoma State', 'Oklahoma St')
teamwins['team'] = teamwins['team'].str.replace('Northern Kentucky', 'N Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Milwaukee', 'WI-Milwkee')
teamwins['team'] = teamwins['team'].str.replace('East Tennessee State', 'E Tenn St')
teamwins['team'] = teamwins['team'].str.replace('Oregon State', 'Oregon St')
teamwins['team'] = teamwins['team'].str.replace('Arizona State', 'Arizona St')
teamwins['team'] = teamwins['team'].str.replace('Iowa St.', 'Iowa St')
teamwins['team'] = teamwins['team'].str.replace('Kennesaw St.', 'Kennesaw St')
teamwins['team'] = teamwins['team'].str.replace('Colorado St.', 'Colorado St')
teamwins['team'] = teamwins['team'].str.replace('Montana St.', 'Montana St')
teamwins['team'] = teamwins['team'].str.replace('Grand Canyon', 'Grd Canyon')
teamwins['team'] = teamwins['team'].str.replace('San Diego St.', 'San Diego St')
teamwins['team'] = teamwins['team'].str.replace('Arizona State', 'Arizona St')
teamwins['team'] = teamwins['team'].str.replace('St. Bonaventure', 'St Bonavent')
teamwins['team'] = teamwins['team'].str.replace('Morehead St.', 'Morehead St')
teamwins['team'] = teamwins['team'].str.replace('Boise St.', 'Boise St')
teamwins['team'] = teamwins['team'].str.replace('Wright State', 'Wright St')
teamwins['team'] = teamwins['team'].str.replace('Texas A&M-CC', 'TX A&M-CC')
teamwins['team'] = teamwins['team'].str.replace('Utah State', 'Utah St')
teamwins['team'] = teamwins['team'].str.replace('UNC Greensboro', 'NC-Grnsboro')

teamwins['team'] = teamwins['team'].str.replace('Norfolk St.', 'Norfolk St')
teamwins['team'] = teamwins['team'].str.replace('Arizona St.', 'Arizona St')
teamwins['team'] = teamwins['team'].str.replace('Gardner-Webb', 'Gard-Webb')
teamwins['team'] = teamwins['team'].str.replace('Cleveland St.', 'Cleveland St')
teamwins['team'] = teamwins['team'].str.replace('Col of Charleston', 'Col Charlestn')
teamwins['team'] = teamwins['team'].str.replace('Georgia St.', 'Georgia St')
teamwins['team'] = teamwins['team'].str.replace('Northeastern', 'Northeastrn')
teamwins['team'] = teamwins['team'].str.replace('Utah St.', 'Utah St')
teamwins['team'] = teamwins['team'].str.replace('Northern Kentucky', 'N Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Eastern Wash.', 'E Washingtn')
teamwins['team'] = teamwins['team'].str.replace('Wright St.', 'Wright St')
teamwins['team'] = teamwins['team'].str.replace('Fairleigh Dickinson', 'FDU')
teamwins['team'] = teamwins['team'].str.replace('North Kentucky', 'N Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Kent St.', 'Kent St')
teamwins['team'] = teamwins['team'].str.replace('Cal State Fullerton', 'CS Fullerton')
teamwins['team'] = teamwins['team'].str.replace('Cal St. Fullerton', 'CS Fullerton')
teamwins['team'] = teamwins['team'].str.replace('S. Dakota St.', 'S Dakota St')
teamwins['team'] = teamwins['team'].str.replace('Saint Mary', 'St Marys')
teamwins['team'] = teamwins['team'].str.replace('South Dakota State', 'S Dakota St')
teamwins['team'] = teamwins['team'].str.replace('College of Charleston', 'Col Charlestn')
teamwins['team'] = teamwins['team'].str.replace('South Alabama', 'S Alabama')
teamwins['team'] = teamwins['team'].str.replace('Morgan State', 'Morgan St')
teamwins['team'] = teamwins['team'].str.replace('Utah State', 'Utah St')
teamwins['team'] = teamwins['team'].str.replace('Northern Colorado', 'N Colorado')
teamwins['team'] = teamwins['team'].str.replace('Boston University', 'Boston U')
teamwins['team'] = teamwins['team'].str.replace('Texas A&M-Corpus Christi', 'TX A&M-CC')
teamwins['team'] = teamwins['team'].str.replace('South Dakota State', 'S Dakota St')
teamwins['team'] = teamwins['team'].str.replace('Wright State', 'Wright St')
teamwins['team'] = teamwins['team'].str.replace('Long Island', 'LIU-Brooklyn')
teamwins['team'] = teamwins['team'].str.replace('Kent State', 'Kent St')
teamwins['team'] = teamwins['team'].str.replace('Arkansas-Pine Bluff', 'Ark Pine Bl')
teamwins['team'] = teamwins['team'].str.replace('Jackson State', 'Jackson St')
teamwins['team'] = teamwins['team'].str.replace('Texas-Arlington', 'TX-Arlington')
teamwins['team'] = teamwins['team'].str.replace('Mississippi Valley State', 'Miss Val St')
teamwins['team'] = teamwins['team'].str.replace('UTEP', 'TX El Paso')
teamwins['team'] = teamwins['team'].str.replace('UC Santa Barbara', 'UCSB')
teamwins['team'] = teamwins['team'].str.replace('Arizona State', 'Arizona St')
teamwins['team'] = teamwins['team'].str.replace('Cleveland State', 'Cleveland St')
teamwins['team'] = teamwins['team'].str.replace('Long Beach State', 'Lg Beach St')
teamwins['team'] = teamwins['team'].str.replace('Indiana State', 'Indiana St')
teamwins['team'] = teamwins['team'].str.replace('Cal State Northridge', 'Cal St Nrdge')
teamwins['team'] = teamwins['team'].str.replace('Portland State', 'Portland St')
teamwins['team'] = teamwins['team'].str.replace('Robert Morris', 'Rob Morris')
teamwins['team'] = teamwins['team'].str.replace('Rob Morris (OT)', 'Rob Morris')
teamwins['team'] = teamwins['team'].str.replace('Texas (OT)', 'Texas')
teamwins['team'] = teamwins['team'].str.replace('Florida (2OT)', 'Florida')

teamwins['team'] = teamwins['team'].str.replace('Loyola (Md.)', 'Loyola-MD')
teamwins['team'] = teamwins['team'].str.replace('Southern Miss', 'S Mississippi')
teamwins['team'] = teamwins['team'].str.replace('Oklahoma State', 'Oklahoma St')
teamwins['team'] = teamwins['team'].str.replace('Weber State', 'Weber St')
teamwins['team'] = teamwins['team'].str.replace('Central Connecticut State', 'Central Conn')
teamwins['team'] = teamwins['team'].str.replace('Penn State', 'Penn St')
teamwins['team'] = teamwins['team'].str.replace('Eastern Kentucky', 'E Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Miami (Ohio)', 'Miami (OH)')
teamwins['team'] = teamwins['team'].str.replace('East Tennessee State', 'E Tenn St')
teamwins['team'] = teamwins['team'].str.replace('Boise State', 'Boise St')
teamwins['team'] = teamwins['team'].str.replace('Cal State Fullerton', 'CS Fullerton')
teamwins['team'] = teamwins['team'].str.replace('Sam Houston State', 'Sam Hous St')
teamwins['team'] = teamwins['team'].str.replace('UNC Asheville', 'NC-Asheville')
teamwins['team'] = teamwins['team'].str.replace('Saint Mary', 'St Marys')
teamwins['team'] = teamwins['team'].str.replace('George Washington', 'Geo Wshgtn')
teamwins['team'] = teamwins['team'].str.replace('St. Bonaventure', 'St Bonavent')
teamwins['team'] = teamwins['team'].str.replace('Georgia State', 'Georgia St')
teamwins['team'] = teamwins['team'].str.replace('South Carolina', 'S Carolina')
teamwins['team'] = teamwins['team'].str.replace('San Diego State', 'San Diego St')
teamwins['team'] = teamwins['team'].str.replace('Iowa State', 'Iowa St')
teamwins['team'] = teamwins['team'].str.replace('Pittsburgh', 'Pitt')
teamwins['team'] = teamwins['team'].str.replace('Stephen F. Austin', 'Ste F Austin')
teamwins['team'] = teamwins['team'].str.replace('Wichita State', 'Wichita St')
teamwins['team'] = teamwins['team'].str.replace('Middle Tennessee', 'Middle Tenn')
teamwins['team'] = teamwins['team'].str.replace('Colorado State', 'Colorado St')
teamwins['team'] = teamwins['team'].str.replace('Florida Gulf Coast', 'Fla Gulf Cst')
teamwins['team'] = teamwins['team'].str.replace('Southern California', 'USC')
teamwins['team'] = teamwins['team'].str.replace('Ole Miss', 'Mississippi')
teamwins['team'] = teamwins['team'].str.replace('Northern Iowa', 'N Iowa')
teamwins['team'] = teamwins['team'].str.replace('Little Rock', 'AR Lit Rock')
teamwins['team'] = teamwins['team'].str.replace('North Dakota State', 'N Dakota St')
teamwins['team'] = teamwins['team'].str.replace(r'Hawai.*', 'Hawaii')
teamwins['team'] = teamwins['team'].str.replace(r'Saint Joseph.*', 'Saint Joseph')
teamwins['team'] = teamwins['team'].str.replace("Saint Joseph", "St Josephs")
teamwins['team'] = teamwins['team'].str.replace('Washington State', 'Wash State')
teamwins['team'] = teamwins['team'].str.replace('Mount St Marys', 'Mt St Marys')
teamwins['team'] = teamwins['team'].str.replace('Boston College', 'Boston Col')
teamwins['team'] = teamwins['team'].str.replace('Southern Illinois', 'S Illinois')
teamwins['team'] = teamwins['team'].str.replace('Mississippi State', 'Miss State')
teamwins['team'] = teamwins['team'].str.replace('Georgia Tech', 'GA Tech')
teamwins['team'] = teamwins['team'].str.replace('South Florida', 'S Florida')
teamwins['team'] = teamwins['team'].str.replace('Norfolk State', 'Norfolk St')
teamwins['team'] = teamwins['team'].str.replace('Western Kentucky', 'W Kentucky')
teamwins['team'] = teamwins['team'].str.replace('Morehead State', 'Morehead St')
teamwins['team'] = teamwins['team'].str.replace('George Mason', 'Geo Mason')
teamwins.loc[teamwins['team'] == 'Pennsylvania', 'team'] = 'U Penn'
teamwins.loc[teamwins['team'] == 'Penn', 'team'] = 'U Penn'
teamstats = teamstats.replace({'team': {'N Carolina': 'North Carolina'}})
teamstats = teamstats.replace({'team': {'Loyola-Chi': 'Loyola Chicago'}})
teamstats = teamstats.replace({'team': {'TX Christian': 'TCU'}})
teamstats = teamstats.replace({'team': {'Abl Christian': 'Abilene Christian'}})
teamstats = teamstats.replace({'team': {'Connecticut': 'UConn'}})
teamstats = teamstats.replace({'team': {'Oregon St': 'Oregon St.'}})
teamstats = teamstats.replace({'team': {'Kansas St': 'Kansas St.'}})
teamstats = teamstats.replace({'team': {'Ohio St': 'Ohio St.'}})
teamstats = teamstats.replace({'team': {'Fla Atlantic': 'FAU'}})
teamstats = teamstats.replace({'team': {'Maryland BC': 'UMBC'}})
teamstats = teamstats.replace({'team': {'Michigan St': 'Michigan St.'}})
teamstats = teamstats.replace({'team': {'Murray St': 'Murray St.'}})
teamstats = teamstats.replace({'team': {'Florida St': 'Florida St.'}})
teamstats = teamstats.replace({'team': {'Penn St': 'Penn St.'}})
teamstats = teamstats.replace({'team': {'New Mexico St': 'N Mex State'}})
teamstats = teamstats.replace({'team': {'W Virginia': 'West Virginia'}})
teamstats = teamstats.replace({'team': {'VA Tech': 'Virginia Tech'}})
teamstats = teamstats.replace({'team': {'F Dickinson': 'FDU'}})
teamstats = teamstats.replace({'team': {'Pittsburgh': 'Pitt'}})

teamwins['team'] = teamwins['team'].str.replace('Iowa Stte', 'Iowa St')
teamwins['team'] = teamwins['team'].str.replace('Georgia Stte', 'Georgia St')
teamwins['team'] = teamwins['team'].str.replace('San Diego Stte', 'Iowa St')
teamwins['team'] = teamwins['team'].str.replace('Pennsylvania', 'U Penn')
teamwins.loc[teamwins['team'] == 'Morehead Stte', 'team'] = 'Morehead St'
teamwins.loc[teamwins['team'] == 'New Mexico St.', 'team'] = 'N Mex State'
teamwins.loc[teamwins['team'] == 'Boise Stte', 'team'] = 'Boise St'
teamwins.loc[teamwins['team'] == 'St. Josephs', 'team'] = 'St Josephs'
teamwins.loc[teamwins['team'] == 'Cleveland Stte', 'team'] = 'Cleveland St'
teamwins.loc[teamwins['team'] == 'Florida (2OT)', 'team'] = 'Florida'
teamwins.loc[teamwins['team'] == 'Rob Morris (OT)', 'team'] = 'Rob Morris'
teamwins.loc[teamwins['team'] == 'Loyola (Md.)', 'team'] = 'Loyola (Md)'
teamwins.loc[teamwins['team'] == 'Miami (Ohio)', 'team'] = 'Miami (OH)'
teamwins.loc[teamwins['team'] == 'San Diego Stte', 'team'] = 'San Diego St'
teamwins.loc[teamwins['team'] == 'Iowa Stte', 'team'] = 'Iowa St'
teamwins.loc[teamwins['team'] == 'Colorado Stte', 'team'] = 'Colorado St'
teamwins.loc[teamwins['team'] == 'Georgia Stte', 'team'] = 'Georiga St'
teamwins.loc[teamwins['team'] == 'Pennsylvania', 'team'] = 'U Penn'
teamwins['team'] = teamwins['team'].str.replace(r'New Mexico St\.', 'N Mex State')
teamwins['team'] = teamwins['team'].str.replace(r'Miami \(Fla\.\)', 'Miami')
teamwins['team'] = teamwins['team'].str.replace(r'Oklahoma St\.', 'Oklahoma St')
teamwins['team'] = teamwins['team'].str.replace(r'Miami \(FL\)', 'Miami')
# Concatenate 'year' and 'team' columns with a space in between
teamstats['team'] = teamstats['year'] + ' ' + teamstats['team']

# Now 'team' column contains the concatenated values
# You might want to drop the 'year' column if it's no longer needed
teamstats.drop(columns=['year'], inplace=True)
teamstats['value'] = teamstats['value'].str.replace('%', '')
teamstats['value'] = teamstats['value'].str.replace('+', '')
teamstats['value'] = teamstats['value'].replace('--', np.nan)
teamstats['value'] = teamstats['value'].astype(float)
# Pivot the dataframe
cleanstats = teamstats.pivot_table(index='team', columns='tablename', values='value', aggfunc='first')

# Reset index to make 'team' a column again
cleanstats = cleanstats.reset_index()

# Fill NaN values with 0 if needed
cleanstats  = cleanstats .fillna(0)
# Left join the dataframes on the 'team' column

# cleanstats['team'] = cleanstats['team'].str.replace(r'^\d+\s+', '')
# teamwins['team'] = teamwins['team'].str.replace(r'^\d+\s+', '')

# # Get unique team names from both dataframes
# cleanstats_teams = cleanstats['team'].unique()
# teamwins_teams = teamwins['team'].unique()

# # Find teams present in teamwins but not in cleanstats
# missing_teams = set(teamwins_teams) - set(cleanstats_teams)

# # Output the missing teams
# print("Teams present in teamwins but not in cleanstats:")
# for team in missing_teams:
#     print(team)
# Teams that are inconsistent
# Michigan state 
# ohio state
# Florida
# Kansas 
# Murray
# St. Mary's
merged_df = pd.merge(teamwins, cleanstats, on='team', how='left')
pd.set_option('display.max_rows', None)

merged_df.to_csv('Full1823.csv', index=False)
    