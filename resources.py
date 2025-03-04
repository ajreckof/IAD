# This resource is useful for Agent4

class Interaction:
    interaction_list = []

    def __init__(self, action, outcome, valence):
        self.action = action
        self.outcome = outcome
        self.valence = valence

    def __str__(self):
        """ Print interaction in the form <action><outcome>(<valence>) """
        return str(self.action) + str(self.outcome) + "(" + str(self.valence) + ")"

    def __repr__(self):
        """ Print interaction in the form <action><outcome>(<valence>) """
        return f"(a: {self.action} o:{self.outcome} v:{self.valence})"

    def __hash__(self):
        """ The hash is necessary to use interactions as keys in a dictionary """
        return self.action * 10 + self.outcome

    def __eq__(self, other):
        """ Interactions are equal if they have the same action and the same outcome """
        if isinstance(other, self.__class__):
            return (self.action == other.action) and (self.outcome == other.outcome)
        else:
            return False
    
    @classmethod
    def reset_interactions(cls):
        cls.interaction_list = []

    @classmethod
    def create_or_retrieve(cls, action, outcome, valence=0):
        """ Use this methode to create a new interaction or to retrieve it if it already exists """
        interaction = Interaction(action, outcome, valence)

        if interaction in cls.interaction_list:
            i = cls.interaction_list.index(interaction)
            # print("Retrieving ", end="")
            # print(cls.interaction_list[i])
            return cls.interaction_list[i]
        else:
            # print("Creating ", end="")
            # print(interaction)
            cls.interaction_list.append(interaction)
            return interaction


if __name__ == '__main__':
    """ demonstrate the usage of Interaction.create_or_retrieve() """
    interaction00 = Interaction.create_or_retrieve(0, 0)  # Create
    interaction01 = Interaction.create_or_retrieve(0, 1)  # Create
    interaction10 = Interaction.create_or_retrieve(1, 0)  # Create
    interaction11 = Interaction.create_or_retrieve(1, 1)  # Create
    interaction00 = Interaction.create_or_retrieve(0, 0)  # Retrieve
