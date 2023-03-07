import time
import csv
from psychopy import visual, event, core

# circular list
from itertools import cycle

# data reader
import pandas as pd 

# random
from random import choice


# ANIMATION VARIATION SUBROUTINES

def lbc_rtc(win):
    # LEFT BOTTOM CORNER TO RIGHT TOP CORNER 
    # Set the starting position of the plane

    # Define the list of images to use
    image_list = ['plane.png', 'bird.png', 'superhero.png']
    #image_list = cycle(image_list)

    plane = visual.ImageStim(win, image= choice(image_list))
    plane.setPos([-1, -1])


    # Animation loop
    start_time = time.time()
    while time.time() - start_time < 2:
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

def lc_rc(win):
    # LEFT MOST CORNER TO RIGHT MOST CORNER
    # Set the starting position of the plane

    image_list = ['plane.png', 'bird.png', 'superhero.png']
    #image_list = cycle(image_list)

    plane = visual.ImageStim(win, image=choice(image_list))
    plane.setPos([-1, 0])


    # Animation loop
    start_time = time.time()
    while plane.pos[0] < 1:
        # Update the position of the plane
        plane.setPos([plane.pos[0]+0.01, plane.pos[1]])
        
        # Check if the plane has reached the rightmost edge of the screen
        if plane.pos[0] > 1:
            # If so, stop updating its position
            break
        
        # Draw the plane
        plane.draw()
        
        # Flip the screen to update the display
        win.flip()

def ltc_rbc(win):
    # LEFT TOP CORNER TO RIGHT BOTTOM CORNER 
    # Set the starting position of the plane
    image_list = ['plane.png', 'bird.png', 'superhero.png']
    #image_list = cycle(image_list)

    plane = visual.ImageStim(win, image=choice(image_list))

    plane.setPos([-1, 1])


    # Animation loop
    start_time = time.time()
    while plane.pos[0] < 1 or plane.pos[1] > -1:
        # Update the position of the plane
        plane.setPos([plane.pos[0]+0.01, plane.pos[1]-0.01])
        
        # Check if the plane has reached the right bottom corner of the screen
        if plane.pos[0] > 1 and plane.pos[1] < -1:
            # If so, stop updating its position
            break
        
        # Draw the plane
        plane.draw()
        
        # Flip the screen to update the display
        win.flip()

def rbc_ltc(win, inverse=True):
    # RIGHT BOTTOM CORNER 

    image_inverse_list = ['plane-inverse.png', 'bird-inverse.png', 'superhero-inverse.png']
    #image_inverse_list = cycle(image_inverse_list)

    
    if inverse:
        plane = visual.ImageStim(win, image=choice(image_inverse_list))
        
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

def rtc_lbc(win, inverse=True):
    # RIGHT TOP CORNER TO LEFT BOTTOM CORNER
    # Create a plane stimulus
    image_inverse_list = ['plane-inverse.png', 'bird-inverse.png', 'superhero-inverse.png']
    #image_inverse_list = cycle(image_inverse_list)

    
    if inverse:
        plane = visual.ImageStim(win, image=choice(image_inverse_list))

        # Set the starting position of the plane
        plane.setPos([1, 1])


        # Animation loop
        start_time = time.time()
        while plane.pos[0] > -1 and plane.pos[1] > -1:
            # Update the position of the plane
            plane.setPos([plane.pos[0]-0.01, plane.pos[1]-0.01])
            
            # Check if the plane has reached the left bottom corner of the screen
            if plane.pos[0] < -1 and plane.pos[1] < -1:
                # If so, stop updating its position
                break
            
            # Draw the plane
            plane.draw()
            
            # Flip the screen to update the display
            win.flip()

def rc_lc(win, inverse=True):

    # RIGHT MOST CORNER TO LEFT MOST CORNER 
    image_inverse_list = ['plane-inverse.png', 'bird-inverse.png', 'superhero-inverse.png']
    #image_inverse_list = cycle(image_inverse_list)

    
    if inverse:
        plane = visual.ImageStim(win, image=choice(image_inverse_list))

        # Set the starting position of the plane
        plane.setPos([1, 0])


        # Animation loop
        start_time = time.time()
        while plane.pos[0] > -1:
            # Update the position of the plane
            plane.setPos([plane.pos[0]-0.01, plane.pos[1]])
            
            # Check if the plane has reached the leftmost edge of the screen
            if plane.pos[0] < -1:
                # If so, stop updating its position
                break
            
            # Draw the plane
            plane.draw()
            
            # Flip the screen to update the display
            win.flip()


    # Create a window to display the stimuli
win = visual.Window(fullscr=True, color=(1, 1, 1))



# LIST OF ANIMATION SUBROUTINES
anime_variations = [lbc_rtc, lc_rc, ltc_rbc, rbc_ltc,rtc_lbc,rc_lc]
anime_variations = cycle(anime_variations)

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
    # plane stimulus
    #plane = visual.ImageStim(win, image=next(image_list))
    #plane.setPos([-1, -1])



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
    animate = next(anime_variations)
    animate(win)



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
