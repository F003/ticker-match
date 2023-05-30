# Company Ticker Matching Program 

This program aims to match company names with their corresponding tickers.

## Prerequisites 📋

Before using this program, ensure that you have the following:

- Python 3 installed on your machine 🐍
- The `difflib` and `pandas` libraries installed 📚

## Getting Started 🚀

1. Clone the entire code repository to your local machine.

2. Save the CSV file containing the list of companies as `list_of_companies.csv` in the `data` folder. The column containing company names should be named 'CompanyNames'.

3. (Optional) If you want to add your own database of companies, provide a CSV file named `db.csv` with columns 'CompanyNames' and 'Ticker' in the main folder.

4. Run the `match.py` file located in the main folder.

5. The output will be available in the `final.csv` file located in the `outputs` folder.

## Disclaimer ⚠️

Please note that not all companies can be matched correctly due to variations in naming conventions, abbreviations, and other factors. The program matches companies based on approximate string matching techniques, and there may be inaccuracies or mismatches. Therefore, it is important to use the program at your own risk and verify the results before relying on them for any critical applications.

## Contributing 🤝

Thank you for using my program! If you have any suggestions or feedback, feel free to contact me. You can also fork this repository and contribute to its development.

## Contact 📧

- Author: FBPerkowski
- Email: stafilip.bop@gmail.com
