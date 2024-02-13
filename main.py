import pygame as pg
from screen import Display
import numpy as np
import pygame.surfarray

from objects import Player

# Initialize pygame
pg.init()

# set resolution
xres = 900
yres = 900

# Set up the game window
screen = pg.display.set_mode((xres, yres))
pg.display.set_caption("Static Surfer")
# Game loop
running = True
display = Display(xres,yres)
p1 = Player(100,100,0)

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Check for arrow key presses
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        p1.turn(-0.01)
    elif keys[pg.K_RIGHT]:
        # Handle right arrow key press
        p1.turn(0.01)
    elif keys[pg.K_UP]:
        # Handle up arrow key press
        p1.accelerate(1)
    elif keys[pg.K_DOWN]:
        # Handle down arrow key press
        p1.accelerate(-0.7)

    p1.update()
    # Check if p1.x is past the bounds of the screen
    if p1.x < 0:
        p1.x = xres
    elif p1.x > xres:
        p1.x = 0

    # Check if p1.y is past the bounds of the screen
    if p1.y < 0:
        p1.y = yres
    elif p1.y > yres:
        p1.y = 0
    # print(p1.x,p1.y)
    display.player(p1.x,p1.y,p1.dir,30)


    display.update()
    # Convert display.pixels to a 3D numpy array with shape (height, width, 3)
    pixels = np.array(display.pixels)
    pixels = np.stack([pixels]*3, axis=-1)  # Repeat the pixel values for the R, G, and B channels
    pixels *= 255  # Scale the pixel values from [0, 1] to [0, 255]
    pixels = pixels.astype(np.uint8)  # Convert to 8-bit integers
    # Draw the pixels
    pygame.surfarray.blit_array(screen, pixels)

    # Update the display
    pg.display.flip()



# Quit the game
pg.quit()