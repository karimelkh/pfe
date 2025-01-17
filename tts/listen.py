import os
import sys
from IPython.display import Audio

# Define a default sampling rate if the model is not available
try:
    sampling_rate = model.generation_config.sample_rate  # Ensure 'model' is properly defined
except NameError:
    sampling_rate = 22050  # Default sampling rate

# Check if the file is provided and exists
if len(sys.argv) > 1:
    audio_file = sys.argv[1]
    if os.path.isfile(audio_file):
        try:
            print(f"Playing audio: {audio_file}")
            # Return Audio object (works in Jupyter or IPython environment)
            audio_obj = Audio(audio_file, rate=sampling_rate)
            # Directly return the audio object for playback in Jupyter/IPython
            audio_obj
        except Exception as e:
            print(f"Error playing audio: {e}")
            sys.exit(2)
    else:
        print(f"Error: File not found - {audio_file}")
        sys.exit(3)
else:
    print("Usage: python script_name.py <audio_file_path>")
    sys.exit(4)