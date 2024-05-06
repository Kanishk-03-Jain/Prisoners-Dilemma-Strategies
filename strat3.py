from agent import BaseAgent

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.grudge = False

    def next_move(self, state):
        op_id = 2 if self.id == 1 else 1
        itr = state["current_iter"]
        history = state["history"]

        if itr == 1:
            return 1  # Start by cooperating

        if self.grudge:
            return -1  # Continue defecting if holding a grudge

        # Check the opponent's pattern in the last few moves to adjust strategy
        last_moves = [history[i][op_id] for i in range(max(1, itr-4), itr)]
        if last_moves.count(-1) > len(last_moves) / 2:
            self.grudge = True  # Start holding a grudge if the opponent defects more than half the time in recent moves
            return -1

        # Adapt to opponent's last move, aiming for mutual cooperation or retaliation
        return history[itr - 1][op_id]




# Agent Test Results
# agent_dumb_score: 140
# your_score: 190
# agent_nice_score: 130
# your_score: 290
# agent_tit_for_tat_score: 200
# your_score: 250
# agent_defect_all_score: 150
# your_score: 50