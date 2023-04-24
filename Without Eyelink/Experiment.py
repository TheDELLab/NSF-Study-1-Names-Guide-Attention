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


def animation_screen(win, orientation,imgs):
    
    if orientation == 'normal':
        # Generate random x and y coordinates
        #    x = np.sort(np.random.rand(15))
        #    y = np.random.rand(15)
        x = np.linspace(0, 0.2*np.pi, 10)
        y = np.random.rand(10)

        # Add some noise to the y coordinates
        y += np.random.normal(scale=0.05, size=y.shape)

        # Create the interpolation object
        spline = make_interp_spline(x, y)
            

        # Initialize PsychoPy window and image stimulus
        #win = visual.Window(units="pix", fullscr=True, color=(1,1,1))
        image = visual.ImageStim(win, image=next(imgs), size=[120, 120])

        # Set starting position of the plane
        x_pos = -960  # left edge of the screen
        y_pos = spline(x.min()) * 900 - 500
        image.pos = [x_pos, y_pos]

        # Loop through the spline points and move the image stimulus
        for t in np.linspace(x.min(), x.max(), num=1000):
            x_pos = t * win.size[0] - 1100  # adjust x_pos calculation
            y_pos = spline(t) * 900 - 500
            image.pos = [x_pos, y_pos]
            image.draw()
            win.flip()
            if x_pos > 960:  # check if plane has reached right end of screen
                break

    elif orientation == 'reverse':
        # Generate random x and y coordinates
        x = np.linspace(0, 0.2*np.pi, 10)
        y = np.random.rand(10)

        # Add some noise to the y coordinates
        y += np.random.normal(scale=0.05, size=y.shape)

        # Reverse the order of the x and y arrays

        x = x[::-1]
        y = y[::-1]

        # Sort the x and y coordinates
        #sort_idx = np.argsort(x)
        #x = x[sort_idx]
        #y = y[sort_idx]
        # Create the interpolation object
        x = np.sort(x)
        spline = make_interp_spline(x, y)

        # Initialize PsychoPy window and image stimulus
        image = visual.ImageStim(win, image=next(imgs), size=[120, 120])

        # Set starting position of the plane
        x_pos = 960  # right edge of the screen
        y_pos = spline(x.max()) * 1200 - 500
        image.pos = [x_pos, y_pos]

        # Loop through the spline points and move the image stimulus
        for t in np.linspace(x.min(), x.max(), num=1000):
            x_pos = 960 - (t * win.size[0] - 200)  # adjust x_pos calculation
            y_pos = spline(t) * 900 - 500
            image.pos = [x_pos, y_pos]
            image.draw()
            win.flip()
        #    if x_pos < -960:  # check if plane has reached left end of screen
        #        break


orientation_list = ["normal","reverse"]

imgs_n = ["sun.png","balloon.png","dog.png","bird.png","plane.png","superhero.png"]
imgs_r = ["sun.png","balloon.png","dog.png","bird-inverse.png","plane-inverse.png","superhero-inverse.png"]

imgs_n = cycle(imgs_n)
imgs_r = cycle(imgs_r)


# Create a window to display the stimuli
win = visual.Window(fullscr=True, units='pix', color=(1, 1, 1))


# Create a list to store the data for each trial
trials_data = []

# Read in the conditions from the CSV file
conditions = pd.read_csv("Sample_Conditions.csv").drop('Unnamed: 0',axis=1)
CONDITION_NUM = 2 ## CHANGE THE CONDITION NUMBER TO TOGGLE BETWEEN THE TRIAL TYPE ( Current options 1 or 2 ) 
cond = conditions[conditions['Conditions']==CONDITION_NUM] 
cond = cond.reset_index(drop=True)
trial_range = cond['Trials'] # Trial range - 0 to 9

for trial in trial_range:
    
    # Create the stimuli
    doll = visual.ImageStim(win, image='Cookie-Monster-smaller.png',pos=(0,300))
    number = visual.TextStim(win, text=cond.loc[trial, 'Target'], color='black', height=100)

    # THE AUDIO STIMULUS GOES HERE
    '''
        CONDITION: 1 - Number Names.
        CONDITION: 2 - Sentences aimed to improve attention.
    '''
    
    if CONDITION_NUM == 1:
        audio = sound.Sound("twenty-three-trim.wav") # Instantiation
    else:
        pass
        # OTHER AUDIO
        audio = sound.Sound("twenty-three-trim.wav") # Instantiation
   

    left_number = visual.TextStim(win, text=cond.loc[trial, 'Target'], color='black', height=100, pos=(-300, 0))
    right_number = visual.TextStim(win, text=cond.loc[trial, 'Foil'], color='black', height=100, pos=(300, 0))

    # Display the doll
    doll.draw()
    win.flip()

    # Wait for 3 seconds
    time.sleep(3)

    # Display the target number
    number.draw()
    win.flip()
        
    # Play audio stimulus
    audio.play()
    
    # Wait for audio to finish playing
    core.wait(audio.getDuration())

    # Wait for 3 seconds
    time.sleep(3)

    # Animate the plane
    orientation = choice(orientation_list)
    if orientation == 'normal':
        animation_screen(win, orientation, imgs_n)
    elif orientation == 'reverse':
        animation_screen(win, orientation, imgs_r )



    # start_time = time.time()
    # while time.time() - start_time < 3:
    #     plane.setPos([plane.pos[0] + 0.01, plane.pos[1] + 0.01])
    #     if plane.pos[0] > 1:
    #         plane.setPos([1, 1])
    #     plane.draw()
    #     win.flip()

    # Display the foils
    left_number.draw()
    right_number.draw()
    win.flip()

    # Wait for a key press
    start_time = time.time()
    keys = event.waitKeys(keyList=['left', 'right'])
    response_time = round((time.time()-start_time), 3)
    response_key = keys[0]


    # --- animation sequence from here, doesn't have any prevalence on the response time recording.

    # Animate the selected number
    if response_key == 'left':
        selected_number = left_number
    else:
        selected_number = right_number

    start_pos = selected_number.pos
    end_pos = doll.pos

    start_time = time.time()
    while time.time() - start_time < 0.5:
        pos = [start_pos[0] + (end_pos[0] - start_pos[0]) * (time.time() - start_time) / 0.5,
                start_pos[1] + (end_pos[1] - start_pos[1]) * (time.time() - start_time) / 0.5]
        selected_number.setPos(pos)

        # Draw the doll and the selected number
        doll.draw()
        selected_number.draw()

        # Flip the screen to update the display
        win.flip()

    # Record the trial data
    trial_data = {'target_number': cond.loc[trial, 'Target'],
                    'foil': cond.loc[trial, 'Foil'],
                    'response_key': response_key,
                    'response_time': response_time}
    trials_data.append(trial_data)
    
    


# Write the data to a CSV file
with open('data_condition_2.csv', 'w', newline='') as csvfile:
    fieldnames = ['target_number', 'foil', 'response_key', 'response_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for trial_data in trials_data:
        writer.writerow(trial_data)
