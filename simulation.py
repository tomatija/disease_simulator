from simulation_window import SimulationManager

a = SimulationManager(500, 500)

a.create_circle(100, 100, 50, 'red')

while True:
    a.refresh_window()

