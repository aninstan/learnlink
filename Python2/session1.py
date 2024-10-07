import tkinter as tk
from tkinter import ttk
import time
import random as rd

def analyze_thoughts():
    for i in range(4):
        label_texts = ["Lader krystallene", "kontakter orakelet", "Doing heavy processing", "Using artificial intelligence"]
        progress_label.config(text=label_texts[i])
        for j in range(100):
          progress_var.set(j)
          root.update()
          time.sleep(0.0)
          
    results = ["Ikke katter", "Katter", "Hunder", "Fisk"]
    randint = rd.randint(0, 3)
    result_label.config(text="You are thinking about: " + results[randint])

root = tk.Tk()
root.title("Useless App")

user_input = tk.StringVar()

input_label = tk.Label(root, text="What are you thinking about?", bg="lightblue")
input_label.pack()

input_entry = tk.Entry(root, textvariable=user_input)
input_entry.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_thoughts)
analyze_button.pack()

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, length=200, variable=progress_var, mode='determinate')
progress_bar.pack()

progress_label = tk.Label(root, text="")
progress_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()