class PracticeCommons:
    def __init__(self):
        # Only TWO core structures
        self.nodes = []  # Knowledge atoms
        self.edges = []  # Relationships between knowledge
        
    def contribute(self, knowledge, contributor):
        # Add node
        node = Node(knowledge, contributor)
        # Let edges emerge from use
        self.nodes.append(node)
        
    def navigate(self, seeker, intent):
        # No prescribed paths
        # Navigation creates paths
        path = follow_resonance(
            seeker.position,
            intent.direction,
            self.nodes
        )
        strengthen_edges(path)  # Paths strengthen through use
        return path