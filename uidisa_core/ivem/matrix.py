class IntentVector:
    """
    Computes and evaluates mathematical vector:
    Vector I = Goal x Context x Boundary
    """
    def __init__(self, goal: str, context_hash: str, boundaries: list):
        self.goal = goal
        self.context_hash = context_hash
        self.boundaries = boundaries

    def evaluate_match(self, target_vector: 'IntentVector') -> bool:
        goal_match = (self.goal == target_vector.goal)
        context_match = (self.context_hash == target_vector.context_hash)
        boundary_match = all(rule in target_vector.boundaries for rule in self.boundaries)
        
        return goal_match and context_match and boundary_match
