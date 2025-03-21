from audio_processor import extract_features
from emotion_classifier import SimpleEmotionClassifier

def analyze_audio(file_path):
    try:
        # Extract features
        features = extract_features(file_path)
        
        # Classify emotion
        classifier = SimpleEmotionClassifier()
        emotion = classifier.classify(features)
        
        # Print results
        print(f"Audio Analysis Results:")
        print(f"Features extracted: {features}")
        print(f"Detected emotion: {emotion}")
        
    except Exception as e:
        print(f"Error processing audio file: {str(e)}")

if __name__ == "__main__":
    # Example usage
    file_path = "myNewFolder"  # Replace with your WAV file path
    analyze_audio(file_path)