import time

# Import required libraries
from psychopy import visual, event


# Create a window to display the stimuli
win = visual.Window(fullscr=True, color=(1, 1, 1))


# Create a plane stimulus
plane = visual.ImageStim(win, image='plane.png')

# Set the starting position of the plane
plane.setPos([1, -1])


# Animation loop
start_time = time.time()
while plane.pos[0] > -1 and plane.pos[1] < 1:
    # Update the position of the plane
    plane.setPos([plane.pos[0]-0.01, plane.pos[1]+0.01])
    
    # Check if the plane has reached the left top corner of the screen
    if plane.pos[0] < -1 and plane.pos[1] > 1:
        # If so, stop updating its position
        break
    
    # Draw the plane
    plane.draw()
    
    # Flip the screen to update the display
    win.flip()
