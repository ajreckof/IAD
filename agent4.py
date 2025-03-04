import numpy as np
import random
from resources import Interaction
from cmath import inf

class Agent4:
    def __init__(self, valence_table, patience = 10):
        self.patience = patience
        """ Creating our agent """
        self.valence_table = valence_table
        self.reset_agent()

    def reset_agent(self):
        Interaction.reset_interactions()
        self.need_novelty = False
        self.inter_prec=None
        self.interaction_memory = {}
        self._action = None
        self.anticipated_outcome = None
        self._increment = 0
        self.predict_outcome = [0 for i in range(len(self.valence_table))]
        self.estimated_reward = [0 for i in range(len(self.valence_table))]

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
                self.need_novelty = False
            """ Updating values based on previous outcome """
            self.predict_outcome[self._action] = outcome
            self.estimated_reward[self._action] = self.valence_table[self._action][outcome]
            inter_cur=Interaction.create_or_retrieve(self._action,outcome,self.valence_table[self._action][outcome])
            if self.inter_prec is not None:
                if not self.inter_prec in self.interaction_memory:
                    self.interaction_memory[self.inter_prec] = {inter_cur : 1}
                elif not inter_cur in self.interaction_memory[self.inter_prec]:
                    self.interaction_memory[self.inter_prec][inter_cur] = 1
                else :
                    self.interaction_memory[self.inter_prec][inter_cur] += 1
            self.inter_prec = inter_cur
        else :
            self._action = 0
        


        """ Computing the next action to enact """
        self.anticipated_outcome = 0
        if not self.inter_prec in self.interaction_memory:
            return self._action
        
        if self._increment > self.patience:
            action_tested = [0] * len(self.valence_table)
            for inter, occ in self.interaction_memory[self.inter_prec].items():
                action_tested[inter.action] += occ

            # testez quelque chose de nouveau si c'est possible sinon remettre l’essai à une prochaine fois
            
            if 0 not in action_tested:
                self.need_novelty = True
            
            print(action_tested)
            self._increment = 0
            self._action = action_tested.index(min(action_tested))
        else :
            if self.need_novelty:
                action_tested = [False for i in range(len(self.valence_table))]
                for inter in self.interaction_memory[self.inter_prec]:
                    action_tested[inter.action] = True

                # testez quelque chose de nouveau si c'est possible sinon remettre l’essai à une prochaine fois
                if False in action_tested:
                    self.need_novelty = False
                    self._increment = 0
                    self._action = action_tested.index(False)
                    return self._action
            
            possible_interactions = self.interaction_memory[self.inter_prec]
            sum_valence_per_action = {}
            count_per_action = {}
            for inter in possible_interactions:
                if not inter.action in sum_valence_per_action :
                    sum_valence_per_action[inter.action] = 0
                    count_per_action[inter.action] = 0
                sum_valence_per_action[inter.action] += possible_interactions[inter] * inter.valence
                count_per_action[inter.action] += possible_interactions[inter]
            
            maxValence = -inf
            maxAction = None
            for action in sum_valence_per_action :
                valence = sum_valence_per_action[action]/count_per_action[action]
                if valence > maxValence :
                    maxValence = valence
                    maxAction = action

            maxOccurence = -inf
            maxOutcome = None

            for inter in possible_interactions:
                if inter.action == maxAction and possible_interactions[inter] > maxOccurence:
                    maxOutcome = inter.outcome
                    maxOccurence = possible_interactions[inter]
                
            self._action = maxAction
            self.anticipated_outcome = maxOutcome
    
        return self._action

