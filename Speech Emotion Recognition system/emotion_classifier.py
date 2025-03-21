class SimpleEmotionClassifier:
    def __init__(self):
        # Simple rule-based classification
        self.amplitude_thresholds = {
            'high': 20000,
            'medium': 10000
        }
        
    def classify(self, features):
        """Simple rule-based emotion classification."""
        max_amp = features['max_amplitude']
        mean_amp = features['mean_amplitude']
        
        if max_amp > self.amplitude_thresholds['high']:
            return 'angry/excited'
        elif max_amp > self.amplitude_thresholds['medium']:
            return 'happy/neutral'
        else:
            return 'sad/calm'