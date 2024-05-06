from agent import BaseAgent
from random import randint

class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        i = randint(1, 100)
        if i>80:
            return -1
        return 1

# from agent import BaseAgent

# class p2(BaseAgent):
#     def _init_(self, id):
#         super()._init_(id=id)
#         self.cooperate = True

#     def next_move(self, state):
#         op_id = 1 if self.id == 2 else 2
#         itr = state["current_iter"]

#         if itr == 1:
#             return 1  # Start by cooperating
        
#         last_move = state["history"][itr - 2][op_id] if itr - 2 in state["history"] else None

#         if last_move == 1:  # Opponent cooperated
#             return 1 if self.cooperate else -1
#         else:  # Opponent defected
#             self.cooperate = False
#             return -1
