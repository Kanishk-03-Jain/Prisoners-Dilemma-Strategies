from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.mistake_threshold = 3
        self.defections = 0
        self.cooperations = 0
        self.grudge = False


    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        history = state["history"]

        if itr == 1:
            return 1

        if self.grudge:
            return -1

        last_opponent_move = history[itr - 1][op_id]
        if random.random() < 0.05:
            return -last_opponent_move


        last_moves = [history[i][op_id] for i in range(max(1, itr-4), itr)]
        if last_moves.count(-1) > len(last_moves) / 2:
            self.grudge = True
            return -1
        
        if last_opponent_move == 1:
            self.cooperations += 1
            self.defections = max(0, self.defections - 1)
            if self.cooperations > self.mistake_threshold:
                return 1
            else:
                return -1
        else:
            self.defections += 1
            self.cooperations = max(0, self.cooperations - 1)
            if self.defections - self.cooperations > self.mistake_threshold:
                return -1
            else:
                return 1

