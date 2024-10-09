import os
import pandas as pd
from gtts import gTTS

# Step 1: Setup
output_dir = "tts_dataset"
audio_dir = os.path.join(output_dir, "audio")
os.makedirs(audio_dir, exist_ok=True)

# List of technical interview questions and terms
dataset = [
    "What is an API? Explain with examples.",
    "How does REST API differ from SOAP API?",
    "What is OAuth, and how does it work in API authentication?",
    "Explain the importance of using CUDA in parallel programming.",
    "Describe the role of TTS systems in AI applications.",
    "What is the function of a GPU in deep learning models?",
    "Explain WebSockets and their advantages over HTTP.",
    "How do you manage state in a React application using Redux?",
    "Explain containerization and how Docker is used in DevOps.",
    "What is Kubernetes, and how does it handle microservices?",
    "Describe the role of an API gateway in microservices architecture.",
    "Explain JWT and its role in authentication.",
    "What is a machine learning pipeline, and how does TensorFlow use them?",
    "Explain continuous integration in a CI/CD pipeline.",
    "How do you fine-tune a pre-trained model using transfer learning in PyTorch?",
    "The API allows two systems to communicate by exposing functionality to external systems.",
    "CUDA enables efficient parallel processing on GPUs.",
    "OAuth provides secure resource access without revealing credentials.",
    "REST architecture ensures that API calls are stateless.",
    "TTS converts written text into audible speech."
]

# Step 2: Generate audio files and save paths
csv_data = []
for idx, sentence in enumerate(dataset):
    audio_file = os.path.join(audio_dir, f"sentence_{idx + 1}.mp3")
    
    # Use gTTS to generate the speech
    tts = gTTS(text=sentence, lang='en')
    tts.save(audio_file)
    
    # Append sentence and audio file path to CSV data
    csv_data.append([sentence, audio_file])

# Step 3: Save the dataset metadata in a CSV file
df = pd.DataFrame(csv_data, columns=["sentence", "audio_file"])
csv_file = os.path.join(output_dir, "dataset.csv")
df.to_csv(csv_file, index=False)

print(f"Dataset generated successfully. Audio files are in '{audio_dir}' and CSV metadata is in '{csv_file}'")
