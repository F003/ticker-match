import os.path
import tkinter as tk
from tkinter import filedialog
from message_handler import display_message

import namematch
import tickermatch

def browse_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def change_db_file():
    db_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if db_file_path:
        # Perform any necessary operations with the new db.csv file path
        display_message("Success!\nThe db.csv file has been changed.")

def run_program():
    list_of_companies_path = file_entry.get()
    db_path = "data/db.csv"  # Assuming db.csv is in the data directory

    if os.path.isfile(list_of_companies_path) and os.path.isfile(db_path):
        display_message("Running name matching...")
        namematch.run()
        display_message("Names matched successfully. You can check it in outputs/names_matched.csv file.")

        display_message("Running ticker matching...")
        tickermatch.run()
        display_message("Tickers matched successfully.\n You can open outputs/final.csv file.\n Thank you for using ticker-match and have a nice day! \n Program ends its work.")
    else:
        display_message("Error: data/list_of_companies.csv or data/db.csv not found. Check README.md for more information.")

# Create the main window
window = tk.Tk()
window.title("Ticker Match Program")

# Create the file selection button
browse_button = tk.Button(window, text="Select companies to match in csv file", command=browse_files)
browse_button.pack()

# Create the file entry field
file_entry = tk.Entry(window, width=50)
file_entry.pack()

# Create the message display area
message_text = tk.Text(window, height=7, width=60)
message_text.pack()

# Create the change db file button
change_db_button = tk.Button(window, text="Change database file", command=change_db_file)
change_db_button.pack(pady=10)

# Create the run button
run_button = tk.Button(window, text="Run Program", command=run_program)
run_button.pack()

# Start the GUI event loop
window.mainloop()
