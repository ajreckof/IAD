import numpy as np
import random

class Agent3:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.anticipated_outcome = None
        self._increment = 0
        self.predict_outcome = [0,0,0]
        self.estimated_reward = [0,0,0]

    def action(self, outcome):
        print(self.estimated_reward)
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
            self.predict_outcome[self._action] = outcome
            self.estimated_reward[self._action] = self.valence_table[self._action][outcome]
        else :
            self._action = 0
        


        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        if self._increment>5:
            self._action = (self._action + 1) % 3
            self._increment = 0
        else :
            if self.estimated_reward[self._action] <= max(self.estimated_reward):
                rec = self.estimated_reward[0]
                l = []
                for i in range(len(self.estimated_reward)) :
                    if self.estimated_reward[i] > rec :
                        l = [i]
                        rec = self.estimated_reward[i]
                    elif self.estimated_reward[i] == rec :
                        l.append(i)
                print(l)
                k = l.index(self._action) + 1 if self._action in l else 0
                self._action = l[k % len(l)]

        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = self.predict_outcome[self._action]
        return self._action

