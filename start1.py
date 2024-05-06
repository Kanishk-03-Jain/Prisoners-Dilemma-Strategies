from agent import BaseAgent
import random

class AdaptiveTitForTat(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        
        # Always cooperate on the first move
        if itr == 1:
            return 1

        history = state["history"][itr - 1]
        last_opponent_move = history[op_id]
        second_last_opponent_move = history[op_id] if itr == 2 else state["history"][itr - 2][op_id]

        # If opponent defected after a streak of cooperation, consider forgiving once
        if last_opponent_move == -1 and second_last_opponent_move == 1:
            # Randomly decide to forgive or not to prevent exploitation; adjust the threshold based on observed behavior
            return 1 if random.random() < 0.75 else -1

        # Mimic the opponent's last move
        return last_opponent_move
