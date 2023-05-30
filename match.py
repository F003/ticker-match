import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import namematch
import tickermatch

def browse_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def run_program():
    list_of_companies_path = file_entry.get()
    db_path = "data/db.csv"  # Assuming db.csv is in the data directory

    if os.path.isfile(list_of_companies_path) and os.path.isfile(db_path):
        # run namematch.py
        namematch.run()
        messagebox.showinfo("Success", "Names matched successfully. You can check it in outputs/names_matched.csv file.")

        # run tickermatch.py
        tickermatch.run()
        messagebox.showinfo("Success", "Tickers matched successfully. Program ends its work. You can open outputs/final.csv file.")
        messagebox.showinfo("Thank you", "Thank you for using ticker-match. Have a nice day!")
    else:
        messagebox.showerror("Error", "data/list_of_companies.csv or data/db.csv not found. Check README.md for more information.")

# Create the main window
window = tk.Tk()
window.title("Ticker Match Program")

# Create the file selection button
browse_button = tk.Button(window, text="Select File", command=browse_files)
browse_button.pack()

# Create the file entry field
file_entry = tk.Entry(window, width=50)
file_entry.pack()

# Create the run button
run_button = tk.Button(window, text="Run Program", command=run_program)
run_button.pack()

# Start the GUI event loop
window.mainloop()