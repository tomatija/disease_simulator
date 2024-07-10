import random
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from simulation_window import create_circle

class Agent:
    def __init__(self, x, y, r, color, width, height):
        self.x = x
        self.y = y
        self.r = r
        self.width = width
        self.height = height
        self.circle = create_circle(x, y, r, color)
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)
        self.death_chance = 20

        self.is_infected = False
        self.infected_time = 0
        self.infection_radius = 10
        self.infection_time_limit = random.uniform(300, 700)
        self.infection_change = 90

        self.can_be_infected = True
        self.cannot_be_infected_time = 0
        self.cannot_be_infected_time_limit = random.uniform(100, 200)

        self.is_imune = False
        self.imune_time = 0
        self.imune_time_limit = random.uniform(300, 500)
        self.imune_chance = 50

        self.direction_change_interval = 5

        self.is_dead = False
    
    def infect(self, override=False):
        if override:
            self.is_infected = True
            self.circle.setPen(QPen(QBrush(Qt.red), 3))
            return
        if random.uniform(0, 100) < self.infection_change and self.can_be_infected:
            self.is_infected = True
            self.circle.setPen(QPen(QBrush(Qt.red), 3))
        else:
            self.can_be_infected = False
            self.cannot_be_infected_time += 1
            if self.cannot_be_infected_time > self.cannot_be_infected_time_limit:
                self.can_be_infected = True
                self.cannot_be_infected_time = 0

    
    def set_imune(self):
        self.is_infected = False
        self.is_imune = True
        self.circle.setPen(QPen(QBrush(Qt.black), 3))
        self.imune_time = 0
    
    def cure(self):
        self.is_imune = False
        self.is_infected = False
        self.circle.setPen(QPen(QBrush(Qt.green), 3))
        self.infected_time = 0

    def is_in_radius(self, other_agent, radius=10):
        return math.sqrt((self.x - other_agent.x) ** 2 + (self.y - other_agent.y) ** 2) < radius

    def calculate_new_position(self):
        new_x = self.x + self.speed * math.cos(self.direction)
        new_y = self.y + self.speed * math.sin(self.direction)
        return new_x, new_y

    def check_for_death(self):
        return random.uniform(0, 100) < self.death_chance

    def move(self):
        x, y = self.calculate_new_position()
        self.check_wall_collision(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.direction_change_interval -= 1
        self.infected_time += 1
        self.imune_time += 1
        if self.direction_change_interval <= 0:
            self.direction_change_interval = 5
            self.direction = self.direction + random.uniform((-math.pi / 9), (math.pi / 9))
        if self.is_infected and self.infected_time > self.infection_time_limit:
            if self.check_for_death():
                self.is_dead = True
                self.is_infected = False
                self.is_imune = False
                return False
            if random.uniform(0, 100) < self.imune_chance:
                self.set_imune()
            else:
                self.cure()
        if self.is_imune and self.imune_time > self.imune_time_limit:
            self.cure()
        self.circle.setPos(x, y)
        return True
    
    def check_wall_collision(self, x, y, width, height):
            # Check horizontal walls
        if x < self.r:
            x = self.r  # Reset position to be within bounds if it goes past the left wall.
            self.direction = math.pi - self.direction  # Reflect the direction horizontally.
        elif x > width - self.r:
            x = width - self.r  # Reset position to be within bounds if it goes past the right wall.
            self.direction = math.pi - self.direction  # Reflect the direction horizontally.

        # Check vertical walls
        if y < self.r:
            y = self.r  # Reset position to be within bounds if it goes past the top wall.
            self.direction = -self.direction  # Reflect the direction vertically.
        elif y > height - self.r:
            y = height - self.r  # Reset position to be within bounds if it goes past the bottom wall.
            self.direction = 2 * math.pi - self.direction
