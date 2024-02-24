from simulation_window import SimulationManager
from agent import Agent
from gui import show_gui

show_gui()

a = SimulationManager(1000, 1000)



agents = []

for x in range(200):
    x, y = a.get_random_position_on_window()
    new_agent = Agent(x, y, 5, 'green', a.view.width(), a.view.height())
    a.add_item_to_scene(new_agent.circle)
    agents.append(new_agent)

for x in agents[:10]:
    x.infect()

def find_agents_close_to_infected_agent(agent, agents):
    close_agents = []
    for other_agent in agents:
        if not other_agent.is_infected and agent != other_agent and agent.is_in_radius(other_agent,50):
            close_agents.append(other_agent)
    return close_agents

while True:
    for agent in agents:
        # find agents close to the infected agent
        if agent.is_infected:
            for other_agent in find_agents_close_to_infected_agent(agent, agents):
                if agent != other_agent and agent.is_in_radius(other_agent):
                    if not other_agent.is_infected:
                        other_agent.infect()
        agent.move()
    a.refresh_window()
    a.wait(0.01)
