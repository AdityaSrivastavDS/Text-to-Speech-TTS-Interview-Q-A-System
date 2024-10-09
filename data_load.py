import pandas as pd

# Load the dataset
csv_file = "A:\\Aditya\\Pojects\\Internship Projects\\Fine-tuning Text-to-Speech (TTS) Model\\tts_dataset\\dataset.csv"
df = pd.read_csv(csv_file)

# Display the first few rows to verify
print(df.head())

# Check the file paths and audio files
print("\nAudio files in the dataset:")
for index, row in df.iterrows():
    print(f"Question: {row['sentence']} -> Audio file: {row['audio_file']}")
