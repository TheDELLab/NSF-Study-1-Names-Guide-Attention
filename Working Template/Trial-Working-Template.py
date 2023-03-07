import time

# Import required libraries
from psychopy import visual, event

# Create a window to display the stimuli
win = visual.Window(fullscr=True, color=(1, 1, 1))

# Create a doll stimulus
doll = visual.ImageStim(win, image='Cookie-Monster.png')

# Create a number stimulus
number = visual.TextStim(win, text='351', color=(0, 0, 0), height=0.35)

# Create a plane stimulus
plane = visual.ImageStim(win, image='plane.png')

# Set the starting position of the plane
plane.setPos([-1, -1])

# Create left and right foiled numbers
left_number = visual.TextStim(win, text='351', color=(0, 0, 0), height=0.35, pos=(-0.3, 0))
right_number = visual.TextStim(win, text='531', color=(0, 0, 0), height=0.35, pos=(0.3, 0))

# Display the doll
doll.draw()
win.flip()

# displays the image for 3 seconds
time.sleep(3)

# Wait for a key press
#event.waitKeys()

# Display the number
number.draw()
win.flip()

time.sleep(3)
# Wait for a key press
#event.waitKeys()

# Animation loop
start_time = time.time()
while time.time() - start_time < 3:
    # Update the position of the plane
    plane.setPos([plane.pos[0]+0.01, plane.pos[1]+0.01])
    
    # Check if the plane has reached the right edge of the screen
    if plane.pos[0] > 1:
        # If so, set the position back to the left edge
        plane.setPos([1, 1])
    
    # Draw the plane
    plane.draw()
    
    # Flip the screen to update the display
    win.flip()

# Display the foiled numbers
left_number.draw()
right_number.draw()
win.flip()

# Wait for a key press
keys = event.waitKeys(keyList=['left', 'right'])

# Animate the selected number
if keys[0] == 'left':
    selected_number = left_number
else:
    selected_number = right_number

start_pos = selected_number.pos
end_pos = doll.pos

start_time = time.time()
while time.time() - start_time < 3:
    pos = [start_pos[0] + (end_pos[0] - start_pos[0]) * (time.time() - start_time) / 3,
           start_pos[1] + (end_pos[1] - start_pos[1]) * (time.time() - start_time) / 3]
    selected_number.setPos(pos)
    
    # Draw the doll and the selected number
    doll.draw()
    selected_number.draw()
    
    # Flip the screen to update the display
    win.flip()
