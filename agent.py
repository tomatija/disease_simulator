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

        self.is_infected = False
        self.infected_time = 0
        self.infection_radius = 10
        self.infection_time_limit = random.uniform(300, 500)

        self.direction_change_interval = 5
    
    def infect(self):
        self.is_infected = True
        self.circle.setPen(QPen(QBrush(Qt.red), 1))
    

    def cure(self):
        self.is_infected = False
        self.circle.setPen(QPen(QBrush(Qt.green), 1))
        self.infected_time = 0

    def is_in_radius(self, other_agent, radius=10):
        return math.sqrt((self.x - other_agent.x) ** 2 + (self.y - other_agent.y) ** 2) < radius

    def calculate_new_position(self):
        new_x = self.x + self.speed * math.cos(self.direction)
        new_y = self.y + self.speed * math.sin(self.direction)
        return new_x, new_y

    def move(self):
        x, y = self.calculate_new_position()
        self.check_wall_collision(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.direction_change_interval -= 1
        self.infected_time += 1
        if self.direction_change_interval <= 0:
            self.direction_change_interval = 5
            self.direction = self.direction + random.uniform((-math.pi / 9), (math.pi / 9))
        if self.is_infected and self.infected_time > self.infection_time_limit:
            self.cure()
        self.circle.setPos(x, y)
    
    def check_wall_collision(self, x, y, width, height):
        if x >= width or x < 0:
            self.direction = math.pi - self.direction
        if y >= height or y < 0:
            self.direction = (-self.direction if y < 0 else 2 * math.pi - self.direction)
    
    def reset_position(self, new_x, new_y):
        self.x, self.y = new_x, new_y
        self.num_wall_hits = 0
        self.circle.setPos(self.x, self.y)