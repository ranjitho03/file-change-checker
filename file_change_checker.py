# file_change_checker.py

import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main app window
window = tk.Tk()
window.title("File Change Checker")
window.geometry("400x250")

# This variable will hold the original file's content
original_content = None

# Function to load the original file
def upload_original():
    global original_content
    file_path = filedialog.askopenfilename(title="Select Original File")
    
    if file_path:
        # Read and store the content
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        status_label.config(text="✅ Original file loaded.")
    else:
        status_label.config(text="❌ No file selected.")

# Function to load another file and compare with original
def upload_and_compare():
    global original_content

    if original_content is None:
        messagebox.showwarning("Warning", "Please load the original file first.")
        return

    file_path = filedialog.askopenfilename(title="Select File to Compare")

    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            new_content = file.read()

        if new_content == original_content:
            status_label.config(text="🟢 No changes detected.")
        else:
            status_label.config(text="🔴 File has been modified.")
    else:
        status_label.config(text="❌ No file selected.")

# UI components
title = tk.Label(window, text="File Change Checker", font=("Arial", 16))
title.pack(pady=10)

btn_upload_original = tk.Button(window, text="Upload Original File", command=upload_original, width=30)
btn_upload_original.pack(pady=10)

btn_upload_compare = tk.Button(window, text="Upload File to Compare", command=upload_and_compare, width=30)
btn_upload_compare.pack(pady=10)

status_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=20)

# Start the app
window.mainloop()
