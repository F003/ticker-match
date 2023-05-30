import pandas as pd

df_to_match = pd.read_csv('outputs/names_matched.csv', encoding='utf-8')
df_db = pd.read_csv('data/db.csv', encoding='utf-8')

df_to_match['MatchingName'] = df_to_match['MatchingName'].astype(str)

# using pandas as pd and astype(str) method change 'CompanyName' and 'Ticker' collums from df_db to strings
df_db['CompanyName'] = df_db['CompanyName'].astype(str)
df_db['Ticker'] = df_db['Ticker'].astype(str)


df_tickersdb = df_db[['Ticker'] ['CompanyName']]
print(df_tickersdb)