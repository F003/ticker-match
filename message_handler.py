# message_handler.py

import tkinter.messagebox as messagebox

def display_message(message_type, message=None):
    if message_type is None:
        message_type = "info"

    if message_type == "info":
        messagebox.showinfo("Information", message)
    elif message_type == "warning":
        messagebox.showwarning("Warning", message)
    elif message_type == "error":
        messagebox.showerror("Error", message)
    else:
        messagebox.showinfo("Message", message)
