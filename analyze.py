import pandas as pd
import numpy as np
from sklearn import linear_model 
import statsmodels.api as sm 
from statsmodels.tools.eval_measures import rmse 

#,df1 = pd.read_csv('Full0712.csv')
#df2 = pd.read_csv('Full1317.csv')
df3 = pd.read_csv('Full1823.csv')
df4 = pd.read_csv('Full24.csv')
# combine = pd.concat([df1, df2], ignore_index=True)
final = df3
stats = final.drop(columns=['wins', 'team'])
wins = final['wins']

regr = linear_model.LinearRegression()
regr.fit(stats, wins)

x = sm.add_constant(stats)
model = sm.OLS(wins, stats).fit()
coefficients = model.params
# Create a DataFrame to store the results
result_df = pd.DataFrame(columns=['team', 'wins'])
for name, value in zip(stats.columns, coefficients):
    print(f'Coefficient for {name}: {value}')
# Iterate through each row of the original DataFrame
for index, row in df4.iterrows():
    # Multiply each value in the row by its corresponding coefficient
    multiplied_values = row[stats.columns] * coefficients.values
    
    # Sum up the multiplied values to get the 'wins' value
    wins_value = multiplied_values.sum()
    
    # Append the 'team' and 'wins' values to the result DataFrame
    result_df = result_df.append({
        'team': row['team'],
        'wins': wins_value
    }, ignore_index=True)
pd.set_option('display.max_rows', None)
result_df = result_df.sort_values(by='wins', ascending=False)

print(result_df)



