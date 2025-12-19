class HybridWorkflow:
    def __init__(self):
        # Only THREE constructs
        self.atoms = []      # Indivisible operations
        self.bonds = []      # Connections between atoms
        self.catalyst = None # Learning/evolution mechanism
        
    def compose(self, intent):
        # Simple grammar
        return f"""
        {intent}:
            human.sense -> ai.interpret
            ai.analyze -> human.decide  
            human.approve -> ai.execute
            both.learn -> workflow.evolve
        """
        
    def compile(self, composition):
        # Transform to executable
        return lambda: execute_with_sovereignty_preservation(composition)