class AxiologicalConstants:
    def __init__(self):
        # Only THREE absolute principles
        self.principles = {
            'AUTONOMY': 'Preserve capacity for self-determination',
            'REVERSIBILITY': 'Maintain ability to undo changes',
            'COMPREHENSIBILITY': 'Ensure decisions remain understandable'
        }
    
    def evaluate(self, action):
        # Single test: Does this preserve all three?
        return all([
            preserves_autonomy(action),
            maintains_reversibility(action),
            remains_comprehensible(action)
        ])