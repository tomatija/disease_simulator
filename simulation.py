from simulation_window import SimulationManager
from agent import Agent
from gui import show_gui
import csv
sim_stops = [(5, True), (70, True), (0, True)]

def run_simulation():
    if not show_gui():
        return

    a = SimulationManager(700, 700)

    agents = []

    infected_agents = []

    for index in range(200):
        x, y = a.get_random_position_on_window()
        new_agent = Agent(x, y, 5, 'green', a.view.width(), a.view.height())
        a.add_item_to_scene(new_agent.circle)
        agents.append(new_agent)

    for x in agents[:5]:
        infected_agents.append(x)
        x.infect()

    def find_agents_close_to_infected_agent(agent, agents):
        close_agents = []
        for other_agent in agents:
            if not other_agent.is_infected and agent != other_agent and agent.is_in_radius(other_agent,50):
                close_agents.append(other_agent)
        return close_agents
    
    def get_num_of_healthy_agents():
        return len(list(filter(lambda x: not x.is_infected and not x.is_dead and not x.is_imune, agents)))  

    def get_num_of_infected_agents():
        return len(list(filter(lambda x: x.is_infected, agents)))

    def get_num_of_dead_agents():
        return len(list(filter(lambda x: x.is_dead, agents)))

    def get_num_of_imune_agents():
        return len(list(filter(lambda x: x.is_imune, agents))) 

    healthy_agents = list(set(agents) - set(infected_agents))
    time = 0
    dead_agent_count = 0
    csv_rows = []
    fields = ["time", "zdravi_agenti", "okuzeni_agenti", "mrtvi_agenti", "imuni_agenti"]
    while True:
        for agent in agents:
            if not agent.is_infected and agent in infected_agents:
                infected_agents.remove(agent)
                healthy_agents.append(agent)
            # find agents close to the infected agent
            if agent.is_infected and not agent.is_imune:
                for other_agent in find_agents_close_to_infected_agent(agent, agents):
                    if agent != other_agent and agent.is_in_radius(other_agent):
                        if not other_agent.is_infected:
                            infected_agents.append(other_agent)
                            if other_agent in healthy_agents:
                                healthy_agents.remove(other_agent)
                            other_agent.infect()
            if not agent.is_dead and not agent.move():
                a.remove_item_from_scene(agent.circle)
                if agent in infected_agents:
                    infected_agents.remove(agent)
                agents.remove(agent)
                dead_agent_count += 1
                continue
        a.refresh_window()
        a.wait(0.01)
        if time % 10 == 0:
            csv_rows.append({"time":time, "zdravi_agenti":get_num_of_healthy_agents(), "okuzeni_agenti":get_num_of_infected_agents(), "mrtvi_agenti":dead_agent_count, "imuni_agenti":get_num_of_imune_agents()})
        time += 1
        if get_num_of_imune_agents() + get_num_of_infected_agents() == 0:
            break
        else:
            continue

    with open("./csv_export.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
    
        # writing headers (field names)
        writer.writeheader()
    
        # writing data rows
        writer.writerows(csv_rows)

if __name__ == "__main__":
    run_simulation()