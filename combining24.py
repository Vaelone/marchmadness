import pandas as pd
import numpy as np

teamstats1 = pd.read_csv('NCAAB_teamstats_vaelone_elankumaran.csv')
teamstats2 = pd.read_csv('NCCAB_otherteamstats_0724_nathan_dsouza.csv')
teamwins = pd.read_csv('NCAAB1317_smayan_ranjan.csv')
del teamstats1['id']
del teamstats1['rank']
del teamstats2['id']
teamstats= pd.concat([teamstats1, teamstats2], ignore_index=True)
del teamwins['id']
teamstats['year'] = teamstats['year'].astype(str)
teamwins['team'] = teamwins['team'].str.replace('Michigan State', 'Michigan St.')
teamwins['team'] = teamwins['team'].str.replace('Ohio State', 'Ohio St.' )
teamwins['team'] = teamwins['team'].str.replace('Florida State', 'Florida St.' )
teamwins['team'] = teamwins['team'].str.replace('Kansas State', 'Kansas St.', )
teamwins['team'] = teamwins['team'].str.replace('Murray State', 'Murray St.' )
teamwins['team'] = teamwins['team'].str.replace(r'St\. Mary.*', 'St. Mary')
teamwins['team'] = teamwins['team'].str.replace(r'St\. Peter.*', 'St. Peter')
teamwins['team'] = teamwins['team'].str.replace(r'Saint Mary.*', 'Saint Mary')
teamwins['team'] = teamwins['team'].str.replace("St. Mary", "St Marys" )
teamwins['team'] = teamwins['team'].str.replace("St. Peter", "St Peters" )
teamwins['team'] = teamwins['team'].str.replace("Saint Mary", "St Marys" )

teamwins['team'] = teamwins['team'].str.replace('Georgia State', 'Georgia St')
teamwins['team'] = teamwins['team'].str.replace('South Carolina', 'S Carolina' )
teamwins['team'] = teamwins['team'].str.replace('San Diego State', 'San Diego St' )
teamwins['team'] = teamwins['team'].str.replace('Iowa State', 'Iowa St' )
teamwins['team'] = teamwins['team'].str.replace('Pittsburgh', 'Pitt')
teamwins['team'] = teamwins['team'].str.replace('Stephen F. Austin', 'Ste F Austin' )
teamwins['team'] = teamwins['team'].str.replace('Wichita State', 'Wichita St')
teamwins['team'] = teamwins['team'].str.replace('Middle Tennessee', 'Middle Tenn' )
teamwins['team'] = teamwins['team'].str.replace('Colorado State', 'Colorado St' )
teamwins['team'] = teamwins['team'].str.replace('Florida Gulf Coast', 'Fla Gulf Cst')
teamwins['team'] = teamwins['team'].str.replace('Southern California', 'USC' )
teamwins['team'] = teamwins['team'].str.replace('Ole Miss', 'Mississippi' )
teamwins['team'] = teamwins['team'].str.replace('Northern Iowa', 'N Iowa')
teamwins['team'] = teamwins['team'].str.replace('Little Rock', 'AR Lit Rock' )
teamwins['team'] = teamwins['team'].str.replace('North Dakota State', 'N Dakota St')
teamwins['team'] = teamwins['team'].str.replace(r'Hawai.*', 'Hawaii')
teamwins['team'] = teamwins['team'].str.replace(r'Saint Joseph.*', 'Saint Joseph')
teamwins['team'] = teamwins['team'].str.replace("Saint Joseph", "St Josephs" )

teamstats = teamstats.replace({'team': {'N Carolina': 'North Carolina'}})
teamstats = teamstats.replace({'team': {'Loyola-Chi': 'Loyola Chicago'}})
teamstats = teamstats.replace({'team': {'TX Christian': 'TCU'}})
teamstats = teamstats.replace({'team': {'Abl Christian': 'Abilene Christian'}})
teamstats = teamstats.replace({'team': {'Connecticut': 'UConn'}})
teamstats = teamstats.replace({'team': {'Oregon St': 'Oregon St.'}})
teamstats = teamstats.replace({'team': {'N Mex State': 'New Mexico St.'}})
teamstats = teamstats.replace({'team': {'Kansas St': 'Kansas St.'}})
teamstats = teamstats.replace({'team': {'Ohio St': 'Ohio St.'}})
teamstats = teamstats.replace({'team': {'Fla Atlantic': 'FAU'}})
teamstats = teamstats.replace({'team': {'Miami': 'Miami (Fla.)'}})
teamstats = teamstats.replace({'team': {'Maryland BC': 'UMBC'}})
teamstats = teamstats.replace({'team': {'Michigan St': 'Michigan St.'}})
teamstats = teamstats.replace({'team': {'Murray St': 'Murray St.'}})
teamstats = teamstats.replace({'team': {'Florida St': 'Florida St.'}})
teamstats = teamstats.replace({'team': {'Oklahoma St': 'Oklahoma St.'}})
teamstats = teamstats.replace({'team': {'Penn St': 'Penn St.'}})
teamstats = teamstats.replace({'team': {'New Mexico St': 'New Mexico St.'}})
teamstats = teamstats.replace({'team': {'W Virginia': 'West Virginia'}})
teamstats = teamstats.replace({'team': {'VA Tech': 'Virginia Tech'}})
teamstats = teamstats.replace({'team': {'F Dickinson': 'FDU'}})
teamstats = teamstats.replace({'team': {'Pittsburgh': 'Pitt'}})

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
# merged_df = pd.merge(teamwins, cleanstats, on='team', how='left')
# pd.set_option('display.max_rows', None)
# merged_df.to_csv('Full1317', index=False)
    