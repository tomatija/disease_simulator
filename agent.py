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
        self.death_chance = 100

        self.is_infected = False
        self.infected_time = 0
        self.infection_radius = 10
        self.infection_time_limit = random.uniform(200, 1000)

        self.is_imune = False
        self.imune_time = 0
        self.imune_time_limit = random.uniform(50, 100)

        self.direction_change_interval = 5

        self.is_dead = False
    
    def infect(self):
        self.is_infected = True
        self.circle.setPen(QPen(QBrush(Qt.red), 1))
    
    def set_imune(self):
        self.is_infected = False
        self.is_imune = True
        self.circle.setPen(QPen(QBrush(Qt.blue), 1))
        self.imune_time = 0
    
    def cure(self):
        self.is_imune = False
        self.circle.setPen(QPen(QBrush(Qt.green), 1))
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
            self.set_imune()
        if self.is_imune and self.imune_time > self.imune_time_limit:
            self.cure()
        self.circle.setPos(x, y)
        return True
    
    def check_wall_collision(self, x, y, width, height):
        if x >= width or x < 0:
            self.direction = math.pi - self.direction
        if y >= height or y < 0:
            self.direction = (-self.direction if y < 0 else 2 * math.pi - self.direction)
