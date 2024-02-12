import math
import numpy as np
import random

class Display:

    ## pixles are stored as pix[y][x]
    def __init__(self,xres,yres):
        self.pixels = [[round(random.random()) for j in range(xres)] for i in range(yres)]

    def box(self,x1,y1,x2,y2):
        for i in range(abs(x2-x1)):
            for j in range(abs(y2-y1)):
                self.pixels[i][j] = abs(self.pixels[i][j] - 1)

    def line(self, x1, y1, x2, y2, thickness=1):
        points = []
        dx = x2 - x1
        dy = y2 - y1

        steps = max(abs(dx), abs(dy))
        Xinc = dx / steps
        Yinc = dy / steps

        for t in range(-thickness//2, thickness//2 + 1):
            x = x1 + t * Yinc
            y = y1 - t * Xinc
            for _ in range(steps):
                points.append((round(x), round(y)))
                x += Xinc
                y += Yinc

        for loc in points:
            self.point(loc[0], loc[1])

    ## switches value of pixels at point
    def point(self,x,y):
        if(x >= 0 and y >= 0 and x < len(self.pixels[0]) and y < len(self.pixels)):
            self.pixels[x][y] = abs(self.pixels[x][y]-1)

    def circle(self, x0, y0, radius):
        x = radius
        y = 0
        err = 0

        while x >= y:
            self.point(x0 + x, y0 + y)
            self.point(x0 + y, y0 + x)
            self.point(x0 - y, y0 + x)
            self.point(x0 - x, y0 + y)
            self.point(x0 - x, y0 - y)
            self.point(x0 - y, y0 - x)
            self.point(x0 + y, y0 - x)
            self.point(x0 + x, y0 - y)

            y += 1
            err += 1 + 2*y
            if 2*(err-x) + 1 > 0:
                x -= 1
                err += 1 - 2*x

    def player(self, x,y, rotation, scale):
        # Define the vertices of the triangle in a "standard" position
        vertices = [
            (scale,0),
            (-scale,-scale*0.7),
            (-scale,scale*0.7)
        ]

        # Apply a rotation and translation to the vertices
        rotated_vertices = []
        for vx, vy in vertices:
            rx = vx * math.cos(rotation) - vy * math.sin(rotation)
            ry = vx * math.sin(rotation) + vy * math.cos(rotation)
            rotated_vertices.append((round(x + rx), round(y + ry)))

        # Draw lines between the vertices
        self.line(*rotated_vertices[0], *rotated_vertices[1],thickness=3)
        self.line(*rotated_vertices[1], *rotated_vertices[2],thickness=3)
        self.line(*rotated_vertices[2], *rotated_vertices[0],thickness=3)