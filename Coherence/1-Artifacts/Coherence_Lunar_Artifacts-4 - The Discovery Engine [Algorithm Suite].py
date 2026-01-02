class DiscoveryEngine:
    def __init__(self):
        # Only TWO core methods (maximum simplicity)
        self.explore = None  # Generate next experiment
        self.learn = None    # Update from results
        
    def explore(self, state, curiosity):
        # Single principle: Maximum divergence from known
        return maximize_kullback_leibler_divergence(
            current_distribution=state,
            curiosity_temperature=curiosity
        )
        
    def learn(self, experiment, result):
        # Single principle: Compress surprise into structure
        return minimize_description_length(
            prior_model=self.state,
            new_observation=(experiment, result)
        )