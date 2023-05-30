import pandas as pd

df_to_match = pd.read_csv('outputs/names_matched.csv', encoding='utf-8')
df_db = pd.read_csv('data/db.csv', encoding='utf-8')

df_to_match['MatchingName'] = df_to_match['MatchingName'].astype(str)

# using pandas as pd and astype(str) method change 'CompanyName' and 'Ticker' collums from df_db to strings
df_db['CompanyName'] = df_db['CompanyName'].astype(str)
df_db['Ticker'] = df_db['Ticker'].astype(str)

# create new dataframe with CompanyName and Ticker collums from df_db
df_tickersdb = df_db[['CompanyName', 'Ticker']]

df_merged = pd.merge(df_to_match, df_tickersdb, left_on='MatchingName', right_on='CompanyName', how='left')
df_merged.rename(columns={'Ticker': 'Ticker'}, inplace=True)

# drop CompanyName_y collumn from df_merged

df_merged.drop(columns=['CompanyName_y'], inplace=True)

#rename 'CompanyName_x' collumn to 'CompanyName'

df_merged.rename(columns={'CompanyName_x': 'CompanyName'}, inplace=True)

# Make SimilarityScore 4th collumn and Ticker 3rd collumn in df_merged
df_placeholder = df_merged['SimilarityScore'].copy()
df_merged.drop(columns=['SimilarityScore'], inplace=True)
df_merged['SimilarityScore'] = df_placeholder

# save df_merged to csv file
df_merged.to_csv('outputs/final.csv', index=False)
