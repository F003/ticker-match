import os.path
import namematch
import tickermatch

if __name__ == "__main__":
    if os.path.isfile("data/list_of_companies.csv") and os.path.isfile("data/db.csv"):
        # run namematch.py
        namematch.run()
        print("Names matched successfully. You can check it in outputs/names_matched.csv file.")

        # run tickermatch.py
        tickermatch.run()
        print("Tickers matched successfully. Program ends its work. You can open outputs/final.csv file.")
        print("Thank you for using ticker-match.")
        print("Have a nice day!")
    else:
        print("Error: data/list_of_companies.csv or data/db.csv not found. Check README.md for more information.")
        exit(1)
