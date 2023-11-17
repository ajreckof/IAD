import numpy as np
import random

class Agent3:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
    
    def reset_agent(self):
        self._action = None
        self.anticipated_outcome = None
        self._increment = 0

        self.total_reward = [0,0,0]
        self.predict_outcome = [0,0,0]
        self.nb_action = [0,0,0]

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
            self.predict_outcome[self._action] = outcome
            self.total_reward[self._action] += self.valence_table[self._action][outcome]
            self.nb_action[self._action] += 1

            #this is to avoid keeping in mind outcomes that are way too far in the past
            self.total_reward[self._action] *= .9
            self.nb_action[self._action] *= .9
        else :
            self._action = 0
        


        """ Computing the next action to enact """
        if self._increment>5:
            # Lorsqu'on s'ennuie, on choisit comme action nouvelle l'action la moins réalisé
            self._action = self.nb_action.index(min(self.nb_action))
            self._increment = 0
        else :
            # Lorsqu'on ne s'ennuie pas on choisit la meilleure action
            average_reward = [total_reward / (max(nb_action,1)) for total_reward, nb_action in zip(self.total_reward,self.nb_action)]
            rec = max(average_reward)
            if average_reward[self._action] < rec:
                self._action = average_reward.index(rec)
        

        self.anticipated_outcome = self.predict_outcome[self._action]
        return self._action

