# Import the necessary modules
from psychopy import visual, core, event

# Create a window
# Screen resolution
SCN_W, SCN_H = (1280, 800)

# Open a PsyhocPy window with the "allowStencil" option 
win = visual.Window((SCN_W, SCN_H), fullscr=True, units='pix', allowStencil=True)

# Create an image stimulus
image_path = 'cookie_monster.png'  # Replace with the actual path to your image
image = visual.ImageStim(win, image=image_path, pos=(-340, 200))

# Draw the image
image.draw()

# Update the display
win.flip()

# Wait for a key press to exit
event.waitKeys()

# Close the window
win.close()
core.quit()
