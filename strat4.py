from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.mistake_threshold = 3  # Forgiveness after 3 perceived mistakes
        self.defections = 0
        self.cooperations = 0

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        history = state["history"]
        
        # Start with cooperation
        if itr == 1:
            return 1

        last_opponent_move = history[itr - 1][self.id]
        
        # Adapt to opponent's moves: tit-for-tat with forgiveness and exploitation
        if last_opponent_move == 1:
            self.cooperations += 1
            self.defections = max(0, self.defections - 1)  # Forgive one defection
            # Exploit consistent cooperation
            if self.cooperations > self.mistake_threshold:
                return 1  # Cooperate if opponent is mostly cooperating
            else:
                return -1  # Defect if still uncertain
        else:
            self.defections += 1
            self.cooperations = max(0, self.cooperations - 1)  # Penalize for defection
            # Retaliate but consider forgiveness if too many defections are due to errors
            if self.defections - self.cooperations > self.mistake_threshold:
                return -1  # Defect if opponent defects significantly more than cooperates
            else:
                return 1  # Cooperate if within forgiveness threshold, considering errors

        # Incorporate randomness to handle unpredictable opponents
        if random.random() < 0.05:  # 5% chance to flip the decision
            return -last_opponent_move
        return last_opponent_move
