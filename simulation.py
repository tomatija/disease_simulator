from simulation_window import SimulationManager
from agent import Agent

a = SimulationManager(1000, 1000)



agents = []

for x in range(10):
    x, y = a.get_random_position_on_window()
    new_agent = Agent(x, y, 5, 'green')
    a.add_item_to_scene(new_agent.circle)
    agents.append(new_agent)

# def agent_movement_handler():
#     # check if movement will move out of bounds
#     # if so, change direction
#     if test_agent.x < 0 or test_agent.x > a.view.width():
#         test_agent.direction = math.pi - test_agent.direction
while True:
    for agent in agents:
        new_x, new_y = agent.calculate_new_position()
        agent.check_wall_collision(new_x, new_y, a.view.width(), a.view.height())
        agent.move(new_x, new_y)
    a.refresh_window()
    a.wait(0.01)
