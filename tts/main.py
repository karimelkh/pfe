from transformers import pipeline
import os
import numpy as np
from scipy.io.wavfile import write

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "..", "audio")

# Initialize the pipeline
try:
    synthesizer = pipeline("text-to-speech", "suno/bark")
except Exception as e:
    print(f"Failed to initialize the pipeline: {e}")
    exit(1)

# Generate speech
try:
    speech = synthesizer("Hello, my dog is cooler than you!", forward_params={"do_sample": True})
except Exception as e:
    print(f"Error during speech synthesis: {e}")
    exit(1)

# Create output directory if it doesn't exist
os.makedirs(AUDIO_DIR, exist_ok=True)

# Save the output
output_file = os.path.join(AUDIO_DIR, "bark_out.wav")
try:
    # audio_data = np.array(speech["audio"] * 32767, dtype=np.int16)  # Convert to int16 for WAV
    write(output_file, rate=speech["sampling_rate"], data=speech["audio"])
    print(f"Audio saved to {output_file}")
except Exception as e:
    print(f"Error saving the audio file: {e}")