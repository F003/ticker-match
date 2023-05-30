import pandas as pd

df_to_match = pd.read_csv('output/names_matched.csv', encoding='utf-8')
df_db = pd.read_csv(data/db.csv, encoding='utf-8')

df_to_match['MatchingName'] = df_to_match['MatchingName'].astype(str)
df_db['Ticeker', 'CompanyName'] = df_db['Ticker', 'CompanyName'].astype(str)

df_tickersdb = df_db[['Ticker'] ['CompanyName']]
print(df_tickersdb)