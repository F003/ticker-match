import pandas as pd
from difflib import SequenceMatcher

def similarity_score(a, b):
    return SequenceMatcher(None, a, b).ratio()

df_to_match = pd.read_csv('data/list_of_companies.csv', encoding='utf-8')
df_db = pd.read_csv('data/db.csv', encoding='utf-8')

# make all company names strings

df_to_match['CompanyName'] = df_to_match['CompanyName'].astype(str)
df_db['CompanyName'] = df_db['CompanyName'].astype(str)

df_namesdb = df_db[['CompanyName']]

# delete df_db
df_db.drop(df_db.index, inplace=True)

# Sort the dataframes by company name
df_to_match = df_to_match.sort_values('CompanyName')
df_namesdb = df_namesdb.sort_values('CompanyName')

# create new pandas dataframe with three collums: name, matching name and similarity score
df_output = pd.DataFrame(columns=['CompanyName', 'MatchingName', 'SimilarityScore']) 

# Iterate through unique starting letters or numbers in df_testy
for starting_letter in df_to_match['CompanyName'].str[0].unique():
    testy_subset = df_to_match[df_to_match['CompanyName'].str.startswith(starting_letter)]
    list_subset = df_namesdb[df_namesdb['CompanyName'].str.startswith(starting_letter)]

    # iterate through each row in testy_subset
    for index, row in testy_subset.iterrows():
        best_score = 0
        # iterate through each row in list_subset
        for index2, row2 in list_subset.iterrows():
            # calculate similarity score for pair
            score = similarity_score(row['CompanyName'], row2['CompanyName'])
            if score > best_score:
                best_score = score
                best_ticker = row2['CompanyName']
        # print checked company name
        print(row['CompanyName'])
        # save company name, best matching name and similarity score to new row in df_output
        df_output.loc[len(df_output)] = [row['CompanyName'], best_ticker, best_score]

# save df_output to csv
df_output.to_csv('outputs/names_matched.csv', index=False)