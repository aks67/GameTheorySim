from Tournament import *
from Agents import *


if __name__ == "__main__":
    # agents = [UnconditionalCooperator(name='Agent1'), UnconditionalDefector(name='Agent2')]
    agent_count = 10
    agents, agent_demographics = PrisonersDilemmaAgents.create_agents(agent_count)

    num_rounds = 100
    tournament = Tournament(agents, num_rounds)
    for a in agent_demographics:
        print(f"{a}: {agent_demographics[a]}")


    # tournament.play_tournament()
    # tournament.printMaxDecisions()

