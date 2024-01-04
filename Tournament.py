import random
from Agents import *


class Tournament:
    
    def __init__(self, num_rounds) -> None:
        self.num_rounds = num_rounds
        self.last_play_history = {}
        self.agents = []


    def add_agents(self, agents):
        self.agents = agents

    def play_round(self, agent1, agent2):
        pass

    def play_tournament(self):
        
        for round_num in range(self.num_rounds):
            # print("\nRound {}".format(round_num + 1))
            
            random.shuffle(self.agents)
            
            for i in range(0, len(self.agents), 2):
                
                agent1 = self.agents[i]
                agent2 = self.agents[i + 1]

                choice1 = agent1.make_choice(agent2)
                choice2 = agent2.make_choice(agent1)

                self.last_play_history[agent1.name] = choice1
                self.last_play_history[agent2.name] = choice2


                payOff1, payOff2 = self.prisonersDilemma(choice1, choice2)
                agent1.update_score(payOff1)
                agent2.update_score(payOff2)
        
    def printFinalScore(self):
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

    def printLastPlay(self):
        for k, v in self.last_play_history.items():
            print(f"Agent {k} chose {v}")