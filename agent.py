import random
import math
class Agent:
    def __init__(self, x, y, circle):
        self.x = x
        self.y = y
        self.circle = circle
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = 0.001#random.uniform(1, 5)
    
    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.circle.setPos(self.x, self.y)