import os
import pandas as pd
from playsound import playsound

# Load the dataset
csv_file = "A:\\Aditya\\Pojects\\Internship Projects\\Fine-tuning Text-to-Speech (TTS) Model\\tts_dataset\\dataset.csv"
df = pd.read_csv(csv_file)

# Function to play the generated audio for a specific question
def play_audio_for_question(question_index):
    # Fetch the corresponding audio file
    audio_file = df.loc[question_index, "audio_file"]
    if os.path.exists(audio_file):
        playsound(audio_file)
    else:
        print("Audio file does not exist!")

# Example usage
while True:
    print("Choose a question number to hear its audio (1 to 20) or 'exit' to quit:")
    choice = input()
    
    if choice.lower() == "exit":
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(df):
        play_audio_for_question(int(choice) - 1)
    else:
        print("Invalid choice, please select a valid number.")
