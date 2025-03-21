import wave
import array
import math
from statistics import mean

def extract_features(file_path):
    """Extract basic audio features from a wave file."""
    with wave.open(file_path, 'rb') as wav_file:
        # Get basic parameters
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()
        
        # Read raw audio data
        raw_data = wav_file.readframes(n_frames)
        
        # Convert bytes to integers
        if sample_width == 2:
            data = array.array('h', raw_data)
        else:
            raise ValueError("Only supports 16-bit audio files")
            
        # Calculate basic features
        amplitude = [abs(x) for x in data]
        
        features = {
            'max_amplitude': max(amplitude),
            'mean_amplitude': mean(amplitude),
            'zero_crossings': sum(1 for i in range(1, len(data)) if data[i-1] * data[i] <= 0)
        }
        
        return features