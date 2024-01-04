import random
from Observer import *

class PrisonersDilemmaAgents:
    def __init__(self, name):
        
        self.name = name
        self.score = 0
        self.decision_count = {'C': 0, 'D': 0}

    def make_choice(self, decision_against):
        pass

    def update_score(self, payoff):
        self.score += payoff

    def get_average(self):
        print("name: ", end='')
        print(self.name, end=' ')
        print("Most played Strategy = ", end=' ')
        max_decision = max(self.decision_count, key=self.decision_count.get)
        print(max_decision, end=' ')
        max_decision_count = max(self.decision_count['C'], self.decision_count['D'])
        print("played: ", end='')
        print(max_decision_count)

    @staticmethod 
    def create_agents(n):
        agent_classes = [RandomAgent, UnconditionalCooperator, UnconditionalDefector, CooperatorP, TitForTat]
        agents = []
        agent_demographics = {}

        for i in range(n):
            agent_class = random.choice(agent_classes)
            name = f"{agent_class.__name__.lower()}{i}"
            if agent_class == CooperatorP:
                coopP = random.uniform(0, 1)
                agent_class_name = agent_class.__name__
                agents.append(agent_class(name, coopP))
                agent_demographics.setdefault(agent_class_name, {'count': 0})
                agent_demographics[agent_class_name]['count'] += 1
                agent_demographics[agent_class_name]['probability'] = coopP

            else:
                agents.append(agent_class(name))
                agent_class_name = agent_class.__name__
                agent_demographics.setdefault(agent_class_name, {'count': 0})
                agent_demographics[agent_class_name]['count'] += 1


        return agents, agent_demographics
     
class RandomAgent(PrisonersDilemmaAgents):
    
    def __init__(self, name):
        super().__init__(name)


    def make_choice(self, decision_against):
        decision =  random.choice(['C', 'D'])
        self.decision_count[decision] += 1
        return decision

class UnconditionalCooperator(PrisonersDilemmaAgents):
    def make_choice(self, decision_against):
        self.decision_count['C'] += 1
        return 'C'

class UnconditionalDefector(PrisonersDilemmaAgents):
    def make_choice(self, decision_against):
        self.decision_count['D'] +=1 
        return 'D'

class CooperatorP(PrisonersDilemmaAgents):
    def __init__(self, name, p):
        super().__init__(name)
        self.coopP = p 
    
    def make_choice(self, decision_against):
        if random.uniform(0, 1) < self.coopP:
            return 'C'
        else:
            return 'D'

class TitForTat(PrisonersDilemmaAgents):
    
    def __init__(self, name):
        super().__init__(name)
     
    def make_choice(self, decision_against):
        
        enemy_agent = decision_against
        # Tournament.printLastPlay()
        # print(enemy_agent.name)

        return 'C'