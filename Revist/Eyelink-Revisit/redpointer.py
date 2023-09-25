#!/usr/bin/env python3
#
# Filename: gaze_contingent_window.py
# Author: Zhiguo Wang
# Date: 2/6/2021
#
# Description:
# A script that displays a Cookie Monster image at the top center of the screen
# and shows a red pointer at the gaze position using PsychoPy and EyeLink.

import pylink
from psychopy import visual, core, event
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

# Connect to the tracker
tk = pylink.EyeLink('100.1.1.1')

# Open an EDF data file
tk.openDataFile('psychopy.edf')

# Put the tracker in offline mode before we change tracking parameters
tk.setOfflineMode()

# Make all types of sample data available over the link
sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT'
tk.sendCommand(f'link_sample_data  = {sample_flags}')

# Screen resolution
SCN_W, SCN_H = (1280, 800)

# Open a PsyhocPy window with the "allowStencil" option 
win = visual.Window((SCN_W, SCN_H), fullscr=False, units='pix', allowStencil=True)

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
coords = f"screen_pixel_coords = 0 0 {SCN_W - 1} {SCN_H - 1}"
tk.sendCommand(coords)

# Request Pylink to use the custom EyeLinkCoreGraphicsPsychoPy library
# to draw calibration graphics (target, camera image, etc.)
genv = EyeLinkCoreGraphicsPsychoPy(tk, win)
pylink.openGraphicsEx(genv)

# Calibrate the tracker
calib_msg = visual.TextStim(win, text='Press ENTER to calibrate')
calib_msg.draw()
win.flip()
tk.doTrackerSetup()

# Load the Cookie Monster image
cookie_monster_img = visual.ImageStim(win, image='cookie_monster.jpg', size=(200, 200))
cookie_monster_img.pos = (0, SCN_H / 2 - 100)  # Position at the top center

# Create a red pointer stimulus
red_pointer = visual.Circle(win, radius=5, fillColor='red', lineColor='red')

# Put tracker in Offline mode before we start recording
tk.setOfflineMode()

# Start recording
tk.startRecording(1, 1, 1, 1)

# Cache some samples
pylink.msecDelay(100)

# Show the Cookie Monster image at the beginning of the experiment
cookie_monster_img.draw()
win.flip()

# Show the red pointer at the gaze coordinates
while not event.getKeys():
    # Check for new samples 
    smp = tk.getNewestSample() 
    if smp is not None:
        if smp.isRightSample():
            gaze_x, gaze_y = smp.getRightEye().getGaze()
        elif smp.isLeftSample():
            gaze_x, gaze_y = smp.getLeftEye().getGaze()
        
        print(f"gaze_x: {gaze_x}, gaze_y: {gaze_y}")
        
        # Draw the red pointer at the gaze position
        red_pointer.pos = (gaze_x - SCN_W / 2.0, SCN_H / 2.0 - gaze_y)
        red_pointer.draw()
        
        win.flip()
    
# Stop recording
tk.stopRecording()

# Put the tracker to offline mode 
tk.setOfflineMode()

# Close the EDF data file on the Host 
tk.closeDataFile()

# Download the EDF data file from Host
tk.receiveDataFile('psychopy.edf', 'psychopy.edf')

# Close the link to the tracker
tk.close()

# Close the graphics
win.close()
core.quit()
