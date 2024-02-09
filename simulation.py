from simulation_window import SimulationManager
from agent import Agent

a = SimulationManager(500, 500)

x, y = a.get_random_position_on_window()

test_agent = Agent(x, y, a.create_circle(x, y, 5, 'green'))


while True:
    #test_agent.move()
    print(test_agent.x, test_agent.y)
    a.refresh_window()
    a.wait(0.1)
