from agent import BaseAgent
import random

class AdjustedAdaptiveTitForTat(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.grudge = False

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1  # Cooperate initially

        history = state["history"]
        last_opponent_move = history[itr - 1][op_id]

        # Early recognition of always defecting strategy
        if itr <= 5 and all(history[i][op_id] == -1 for i in range(1, itr)):
            self.grudge = True  # Hold a grudge if the opponent defects consistently early on

        # If holding a grudge, always defect
        if self.grudge:
            return -1

        # If opponent defected after a streak of cooperation, apply selective forgiveness
        if itr > 2 and last_opponent_move == -1 and history[itr - 2][op_id] == 1:
            # Forgive less often when opponent has a history of defecting after cooperating
            return 1 if random.random() < 0.5 else -1

        return last_opponent_move  # Mimic the opponent's last move
