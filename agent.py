import random
import math

from simulation_window import create_circle
class Agent:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.circle = create_circle(x, y, r, color)
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = 2#random.uniform(1, 5)
    
    def calculate_new_position(self):
        new_x = self.x + self.speed * math.cos(self.direction)
        new_y = self.y + self.speed * math.sin(self.direction)
        return new_x, new_y
        # self.x = new_x
        # self.y = new_y 
        # self.circle.setPos(new_x, new_y)
    
    def change_direction(self, hit_wall=False):
        if hit_wall:
            self.direction = random.uniform(0, 2 * math.pi)
        else:
            self.direction = self.direction - math.pi

    def move(self, x, y):
        self.x = x
        self.y = y
        self.direction = self.direction + random.uniform((-math.pi / 9), (math.pi / 9))
        self.circle.setPos(x, y)
    
    def check_wall_collision(self,x , y, width, height):
        if(x >= width):
            self.direction = math.pi - self.direction
        elif (x < 0):
            self.direction = -math.pi - self.direction
        elif(y >= height):
            self.direction = 2*math.pi - self.direction
        elif (y < 0):
            self.direction = -self.direction
    
    # TODO: add check if wall hit 20 times in 5 seconds then reset position, and if out of bounds reset position