class Agent1:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.anticipated_outcome = None
        self._increment = 0
        self.predict_outcome = [[0,0],[0,0]]

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.valence_table[self._action][outcome]) + ")")
            if self.anticipated_outcome == outcome:
                self._increment += 1
            else :
                self._increment = 0
            """ Updating values based on previous outcome """
            self.predict_outcome[self._action][outcome] += 1
        else :
            self._action = 0
        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        if self._increment>5:
            self._action = 1 - self._action
            self._increment = 0

        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = 0 if self.predict_outcome[self._action][0] > self.predict_outcome[self._action][1] else 1
        return self._action