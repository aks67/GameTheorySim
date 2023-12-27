import random
from Agents import *


class Tournament:
    
    def __init__(self, agents, num_rounds) -> None:
        
        self.agents = agents
        self.num_rounds = num_rounds

    def play_round(self, agent1, agent2):
        pass

    def play_tournament(self):
        
        for round_num in range(self.num_rounds):
            # print("\nRound {}".format(round_num + 1))
            
            random.shuffle(self.agents)
            
            for i in range(0, len(self.agents), 2):
                
                agent1 = self.agents[i]
                agent2 = self.agents[i + 1]

                choice1 = agent1.make_choice()
                choice2 = agent2.make_choice()

                payOff1, payOff2 = self.prisonersDilemma(choice1, choice2)
                agent1.update_score(payOff1)
                agent2.update_score(payOff2)
        

        print("\nFinal Scores:")
        for agent in self.agents:
            print("{}: {}".format(agent.name, agent.score))

    def prisonersDilemma(self, choice1, choice2):
        payoff_matrix = {
            ('C', 'C'): (3, 3),
            ('C', 'D'): (-5, 5),
            ('D', 'C'): (5, -5),
            ('D', 'D'): (1, 1)
        }
        return payoff_matrix[(choice1, choice2)]

    def printMaxDecisions(self):
        for a in self.agents:
            a.get_average()