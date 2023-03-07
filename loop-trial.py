import time
import csv
from psychopy import visual, event, core

# circular list
from itertools import cycle

# data reader
import pandas as pd 

# Create a window to display the stimuli
win = visual.Window(fullscr=True, color=(1, 1, 1))

# Define the list of images to use
image_list = ['plane.png', 'bird.png', 'superhero.png']
image_list = cycle(image_list)

# Create a list to store the data for each trial
trials_data = []

# Read in the conditions from the CSV file
conditions = pd.read_csv("Sample_Conditions.csv").drop('Unnamed: 0',axis=1)
cond_1 = conditions[conditions['Conditions']==1]
trial_range = cond_1['Trials'] # Trial range - 0 to 9
for trial in trial_range:
    # Create the stimuli
    doll = visual.ImageStim(win, image='Cookie-Monster-smaller.png',pos=(0,0.5))
    number = visual.TextStim(win, text=cond_1.loc[trial, 'Target'], color='black', height=0.35)

    # THE AUDIO STIMULUS GOES HERE
    '''
        CONDITION: 1 - Number Names.
        CONDITION: 2 - Sentences aimed to improve attention.
    '''

    plane = visual.ImageStim(win, image=next(image_list))
    plane.setPos([-1, -1])
    left_number = visual.TextStim(win, text=cond_1.loc[trial, 'Target'], color='black', height=0.35, pos=(-0.3, 0))
    right_number = visual.TextStim(win, text=cond_1.loc[trial, 'Foil'], color='black', height=0.35, pos=(0.3, 0))

    # Display the doll
    doll.draw()
    win.flip()

    # Wait for 3 seconds
    time.sleep(3)

    # Display the target number
    number.draw()
    win.flip()

    # Wait for 3 seconds
    time.sleep(3)

    # Animate the plane
    start_time = time.time()
    while time.time() - start_time < 3:
        plane.setPos([plane.pos[0] + 0.01, plane.pos[1] + 0.01])
        if plane.pos[0] > 1:
            plane.setPos([1, 1])
        plane.draw()
        win.flip()

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
    trial_data = {'target_number': cond_1.loc[trial, 'Target'],
                    'foil': cond_1.loc[trial, 'Foil'],
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
