import pandas as pd
from fuzzywuzzy import fuzz

df_testy = pd.read_csv('filipowe-testy.csv', encoding='utf-8')
df_tickers = pd.read_csv('tickers.csv', encoding='utf-8')

# Sort the dataframes by company name
df_testy.sort_values('CompanyName', inplace=True)
df_tickers.sort_values('CompanyName', inplace=True)

# Create new pandas DataFrame with three columns: name, matching name, and similarity score
output_rows = []

# Iterate through unique starting letters or numbers in df_testy
for starting_letter in df_testy['CompanyName'].str[0].unique():
    testy_subset = df_testy[df_testy['CompanyName'].str.startswith(starting_letter)]
    list_subset = df_tickers[df_tickers['CompanyName'].str.startswith(starting_letter)]

    # Calculate similarity score for each pair using fuzzywuzzy's fuzz.ratio
    scores = list_subset['CompanyName'].apply(lambda x: fuzz.ratio(x, testy_subset['CompanyName']))
    best_indices = scores.idxmax()

    # Get the best matching ticker and similarity score
    best_ticker = list_subset.loc[best_indices, 'CompanyName']
    best_score = scores.loc[best_indices]

    # Append the row to the output list
    output_rows.append([testy_subset['CompanyName'], best_ticker, best_score])

# Create the DataFrame from the list of rows
df_output = pd.DataFrame(output_rows, columns=['CompanyName', 'MatchingName', 'SimilarityScore'])

# Save df_output to CSV
df_output.to_csv('output.csv', index=False)
