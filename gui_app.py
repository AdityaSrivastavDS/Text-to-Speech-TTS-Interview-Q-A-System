import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd
from playsound import playsound

# Load the dataset
csv_file = "A:\\Aditya\\Pojects\\Internship Projects\\Fine-tuning Text-to-Speech (TTS) Model\\tts_dataset\\dataset.csv"
df = pd.read_csv(csv_file)

# Function to play audio when a question is clicked
def play_audio():
    selected_index = question_listbox.curselection()
    if selected_index:
        audio_file = df.loc[selected_index[0], "audio_file"]
        if os.path.exists(audio_file):
            playsound(audio_file)
        else:
            messagebox.showerror("Error", "Audio file not found!")

# Create the main window
root = tk.Tk()
root.title("TTS Question Player")

# Create a listbox to display questions
question_listbox = tk.Listbox(root, width=80, height=20)
for question in df["sentence"]:
    question_listbox.insert(tk.END, question)

question_listbox.pack(pady=10)

# Play button
play_button = tk.Button(root, text="Play Selected Question", command=play_audio)
play_button.pack(pady=10)

# Run the app
root.mainloop()
