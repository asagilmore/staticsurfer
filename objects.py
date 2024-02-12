import math

class Object:
    def __init__(self,x,y,dir,s_lim = 15):
        self.x = x
        self.y = y
        self.dir = dir
        self.xVel = 0
        self.yVel = 0
        self.rotVel = 0
        self.s_lim = s_lim


    def update(self):
        drag_factor = 0.99  # Adjust this value to change the amount of drag
        self.xVel *= drag_factor
        self.yVel *= drag_factor
        self.rotVel *= drag_factor
        self.rotVel *= drag_factor
        if abs(self.xVel) > self.s_lim:
            self.xVel = self.s_lim if self.xVel > 0 else -self.s_lim
        if abs(self.yVel) > self.s_lim:
            self.yVel = self.s_lim if self.yVel > 0 else -self.s_lim
        self.x += self.xVel
        self.y += self.yVel
        self.dir += self.rotVel
        if self.dir > 2 * math.pi:
            self.dir -= 2 * math.pi
        elif self.dir < -2 * math.pi:
            self.dir += 2 * math.pi

class Player(Object):
    def __init__(self, x, y, dir):
        super().__init__(x, y, dir)

    def turn(self, dir):
        self.rotVel += dir

    def accelerate(self, mag):
        self.xVel += mag * math.cos(self.dir)
        self.yVel += mag * math.sin(self.dir)