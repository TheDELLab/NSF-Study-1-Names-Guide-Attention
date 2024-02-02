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
from psychopy import visual, core, sound, event, gui, data
import pandas as pd 
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

# Open a Psychopy window with the "allowStencil" option 
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

# Create a red pointer stimulus
red_pointer = visual.Circle(win, radius=5, fillColor='red', lineColor='red')


# Put tracker in Offline mode before we start recording
tk.setOfflineMode()

# Start recording
tk.startRecording(1, 1, 1, 1)

# Cache some samples
pylink.msecDelay(100)
# Show the red pointer at the gaze coordinates
while program_state == 'running':
    # Check for new samples 
    smp = tk.getNewestSample() 
    if smp is not None:
        if smp.isRightSample():
            gaze_x, gaze_y = smp.getRightEye().getGaze()
        elif smp.isLeftSample():
            gaze_x, gaze_y = smp.getLeftEye().getGaze()
        
        # Calculate PsychoPy coordinates
        psycho_x = gaze_x - SCN_W / 2.0
        psycho_y = SCN_H / 2.0 - gaze_y
        
        # Draw the red pointer at the gaze position
        red_pointer.pos = (psycho_x, psycho_y)
        red_pointer.draw()
        
        # Check if gaze is within the bounding box of the Cookie Monster image
        if cookie_monster_bbox.contains(psycho_x, psycho_y):
            # Display the "Welcome" text and change program state
            if not welcome_displayed:
                welcome_text.draw()
                win.flip()
                core.wait(2)
                welcome_displayed = True
                program_state = 'start'
        else:
            welcome_displayed = False
        
        win.flip()

# Display the sentences based on the program state
if program_state == 'start':
    for iteration in range(4):
    
        # Shuffle
        test_df = test_df.sample(frac=1)
        train_df = train_df.sample(frac=1)
        

        training_phase_text.draw()
        win.flip()
        control = event.waitKeys(keyList=['space'])

        if control[0] == 'space':
            
            
            for i,row in enumerate(train_df.iterrows(),1):
                block_data = {}
                block_data['block'] = iteration + 1 
                block_data['trial'] = i
                
                
                trial_data = row[1]
                if choice_data[0] == "Condition 1":
                    CONDITION = 1 
                    condition_column = "Condition 1"
                else:
                    CONDITION = 2
                    condition_column = "Condition 2"
                audio_path = os.path.join('Audio',trial_data[condition_column] + '.wav')
                
                block_data['audio'] = audio_path[:-4]
        
                sound_stim = sound.Sound(audio_path)
                images = trial_data['Visual'].split(',')
                
                for j, image in enumerate(images,1):
                    block_data[f"S{j}"] = image
                    
                
                num_images = len(images)
                spacing = 70  # Adjust the spacing between images as needed
                total_width = (num_images - 1) * spacing
                start_x = -total_width / 2
                
                # Create a list of ImageStim objects with appropriate positions
                image_stims = []
                
                for image_name, i in zip(images, range(num_images)):
                    image_path = os.path.join('Images', image_name.strip())
                    x = start_x + i * spacing
                    image_stim = visual.ImageStim(win, image=image_path, pos=(x, 0), size=(61, 61))
                    image_stims.append(image_stim)
                
                
                # Presenting Images
                sound_stim.play()
                for image_stim in image_stims:
                    image_stim.draw()
                    
                win.flip()
                    
                
                BLOCK_DATA_TRAIN.append(block_data)
                keys = event.waitKeys(keyList=['space']) 
                
        
    

   

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
