from Tournament import *
from Agents import *
from Observer import *

if __name__ == "__main__":
    
    num_rounds = 100
    tournament = Tournament(num_rounds)
    agent_count = 10
    agents, agent_demographics = PrisonersDilemmaAgents.create_agents(agent_count)

    tournament.play_tournament()

    obs = Observer(tournament)
    obs.get_last_played_by(agents[0].name)
