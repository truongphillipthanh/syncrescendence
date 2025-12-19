class CitationTracker:
    def __init__(self):
        # Only ONE measurement
        self.implemented = None  # Binary: used or not used
        
    def track(self, artifact, user):
        # Simply record implementation
        if user.implemented(artifact):
            return True
        return False
        
    def measure_impact(self):
        # Impact = implementation frequency
        # No complex metrics, just usage
        return count_implementations()