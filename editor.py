import tkinter as tk
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as file:
            content = file.read()
            text.delete('1.0', tk.END)
            text.insert(tk.END, content)

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, 'w') as file:
            content = text.get('1.0', tk.END)
            file.write(content)

def search():
    search_str = search_entry.get()
    text.tag_remove('found', '1.0', tk.END)
    if search_str:
        count = tk.IntVar()
        idx = '1.0'
        while True:
            idx = text.search(search_str, idx, nocase=True, stopindex=tk.END, count=count)
            if not idx:
                break
            lastidx = f"{idx}+{count.get()}c"
            text.tag_add('found', idx, lastidx)
            idx = lastidx

        text.tag_config('found', background="yellow")

def replace():
    search_str = search_entry.get()
    replace_str = replace_entry.get()
    if search_str:
        content = text.get('1.0', tk.END)
        new_content = content.replace(search_str, replace_str)
        text.delete('1.0', tk.END)
        text.insert('1.0', new_content)

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a Text widget
text = tk.Text(root)
text.pack(expand=True, fill="both")

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Button to open file
open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(side="left", padx=5)

# Button to save file
save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side="left", padx=5)

# Search functionality
search_entry = tk.Entry(button_frame)
search_entry.pack(side="left", padx=5)
search_button = tk.Button(button_frame, text="Search", command=search)
search_button.pack(side="left", padx=5)

# Replace functionality
replace_entry = tk.Entry(button_frame)
replace_entry.pack(side="left", padx=5)
replace_button = tk.Button(button_frame, text="Replace", command=replace)
replace_button.pack(side="left", padx=5)

# Run the application
root.mainloop()
