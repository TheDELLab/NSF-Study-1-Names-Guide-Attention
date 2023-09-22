from psychopy import visual, event, core

# Create a fullscreen window
# myWin = visual.Window(units='norm', fullscr=True, color='white', monitor='testMonitor') ~ Andrew's Code 
myWin = visual.Window(units='norm', fullscr=True, color='white',monitor='testMonitor')
windowSize = myWin.size



## Load the image
#aim_image = visual.ImageStim(myWin, image='aim.png')  # Replace 'aim.png' with your image file path
#
## Define positions for 9 points on the screen
#positions = [
#    (-0.2, 0.5), (0, 0.5), (0.5, 0.5),
#    (-0.5, 0), (0, 0), (0.5, 0),
#    (-0.5, -0.5), (0, -0.5), (0.5, -0.5)
#]
#
## Display the image at each position
#for position in positions:
#    aim_image.pos = position
#    aim_image.draw()
#    myWin.flip()
#    core.wait(1)  # Display each image for 1 second (adjust as needed)

# Define positions for 9 points on the screen
positions = [
    (-1,1), (0,1), (1,1),
    (-1,0.5), (-0.5, 0.5), (0, 0.5), (0.5, 0.5),(1,0.5),
    (-1,0), (-0.5, 0), (0, 0), (0.5, 0),(1,0),
    (-1,-0.5),(-0.5, -0.5), (0, -0.5), (0.5, -0.5),(1,-0.5),
    (-1,-1), (0,-1), (1,-1),
    
]

# Create text stimuli for each position
text_stimuli = [visual.TextStim(myWin, text=f"{pos[0]:.2f}, {pos[1]:.2f}", pos=pos, color='black') for pos in positions]

# Draw all text stimuli on the screen
for text_stimulus in text_stimuli:
    text_stimulus.draw()

# Flip the window to display the text stimuli
myWin.flip()

print(windowSize)

# Wait for a key press or a specific duration (adjust as needed)
event.waitKeys()
# Alternatively, you can use core.wait(1) to display the text for 1 second.

# Close the window when done
myWin.close()

core.quit()



## Create text stimuli for each position
#text_stimuli = [visual.TextStim(myWin, text=f"{pos[0]:.2f}, {pos[1]:.2f}", pos=pos, color='black') for pos in positions]
#
## Display the text stimuli
#for text_stimulus in text_stimuli:
#    text_stimulus.draw()
##    myWin.flip()
#    core.wait(1)  # Display each text for 1 second (adjust as needed)
#
#
#
#
## Close the window when done
#myWin.close()
#core.quit()
#