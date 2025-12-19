class MetamorphicFitness:
    def __init__(self):
        # ONE metric to rule them all
        self.omega = None  # The capacity to continue becoming
        
    def evaluate(self, state, trajectory):
        # Omega = Optionality
        # The number of viable futures remaining open
        return count_reachable_futures(
            from_state=state,
            given_trajectory=trajectory,
            constraint="preserves_sovereignty"
        )