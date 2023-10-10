import numpy as np
import random
from resources import Interaction
from cmath import inf
nb_action = 2

class Agent4:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.inter_prec=None
        self.interaction_memory = {}
        self.valence_table = valence_table
        self._action = None
        self.anticipated_outcome = None
        self._increment = 0
        self.predict_outcome = [0 for i in range(nb_action)]
        self.estimated_reward = [0 for i in range(nb_action)]

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("mémoires des interactions :",self.interaction_memory)
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
            inter_cur=Interaction.create_or_retrieve(self._action,outcome,self.valence_table[self._action][outcome])
            if self.inter_prec is not None:
                if not self.inter_prec in self.interaction_memory:
                    self.interaction_memory[self.inter_prec] = [inter_cur]
                elif not inter_cur in self.interaction_memory[self.inter_prec]:
                    self.interaction_memory[self.inter_prec].append(inter_cur)
            self.inter_prec = inter_cur
        else :
            self._action = 0
        


        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        self.anticipated_outcome = 0
        if self._increment>5:
            action_tested = [False for i in range(nb_action)]
            for inter in self.interaction_memory[self.inter_prec]:
                action_tested[inter.action] = True
            if False in action_tested:
                self._action = action_tested.index(False)
            else :
                self._action = (self._action + 1) % nb_action
            self._increment = 0
        elif self.inter_prec in self.interaction_memory:
            possible_interactions = self.interaction_memory[self.inter_prec]
            max = -inf
            maxInter=None
            for inter in possible_interactions:
                if inter.valence>max:
                    max=inter.valence
                    maxInter=inter
            self._action = maxInter.action
            self.anticipated_outcome = maxInter.outcome
        else : 
            self._action = 0 

    
        return self._action

