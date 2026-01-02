class ResonanceDetector:
    def __init__(self):
        # Only ONE measurement
        self.phi = None  # Integrated information
        
    def detect(self, interaction):
        # Single question: Does the whole exceed parts?
        phi = calculate_integrated_information(interaction)
        
        # Φ (phi) > sum(parts) indicates resonance
        # Higher Φ indicates deeper resonance
        # Φ approaching infinity indicates phase transition
        
        return {
            'resonance': phi > threshold,
            'depth': log(phi),
            'approaching_criticality': phi > historical_maximum
        }