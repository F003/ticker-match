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

    # Filter out rows with missing values in 'CompanyName' column
    list_subset = df_tickers.dropna(subset=['CompanyName'])
    list_subset = list_subset[list_subset['CompanyName'].str.startswith(starting_letter)]

    scores = []
    # Calculate similarity score for each pair using fuzzywuzzy's fuzz.ratio
    for x in testy_subset['CompanyName']:
        scores.append(list_subset['CompanyName'].apply(lambda y: fuzz.ratio(x, y)).max())

    best_indices = pd.Series(scores).idxmax()

    # Get the best matching ticker and similarity score
    best_ticker = list_subset['CompanyName'].iloc[best_indices]
    best_score = scores[best_indices]

    # Append the row to the output list
    output_rows.append([testy_subset['CompanyName'], best_ticker, best_score])

# Create the DataFrame from the list of rows
df_output = pd.DataFrame(output_rows, columns=['CompanyName', 'MatchingName', 'SimilarityScore'])

# Save df_output to CSV
df_output.to_csv('output.csv', index=False)
