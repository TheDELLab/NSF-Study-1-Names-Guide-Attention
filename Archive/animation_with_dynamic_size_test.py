import time
import csv
from psychopy import visual, event, core, sound

# for animation coordinates
import numpy as np
from scipy.interpolate import make_interp_spline

# circular list
from itertools import cycle

# data reader
import pandas as pd 

# random
from random import choice


# Initialize PsychoPy window and image stimulus
win = visual.Window(units="pix", fullscr=True, color=(1,1,1))

# Get the size of the window in pixels
win_width, win_height = win.size

# Define the size of the image stimulus
image_size = [int(win_width * 0.1), int(win_height * 0.1)]
image = visual.ImageStim(win, image='balloon.png', size=image_size)

# Set the starting position of the plane
x_pos = -win_width / 2  # left edge of the screen
y_pos = spline(x.min()) * win_height - win_height / 2
image.pos = [x_pos, y_pos]

# Loop through the spline points and move the image stimulus
for t in np.linspace(x.min(), x.max(), num=1000):
    # Update the position of the image stimulus based on the window size
    x_pos = t * win_width - win_width / 2
    y_pos = spline(t) * win_height - win_height / 2
    image.pos = [x_pos, y_pos]
    image.draw()
    win.flip()
    if x_pos > win_width / 2:  # check if plane has reached right end of screen
        break
