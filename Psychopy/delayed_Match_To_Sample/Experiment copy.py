import time
import csv
import os
from psychopy import visual, event, core, sound, gui
from string import ascii_letters, digits

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
        for t in np.linspace(x.min(), x.max(), num=600):
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
        for t in np.linspace(x.min(), x.max(), num=600):
            x_pos = 960 - (t * win.size[0] - 200)  # adjust x_pos calculation
            y_pos = spline(t) * 900 - 500
            image.pos = [x_pos, y_pos]
            image.draw()
            win.flip()
        #    if x_pos < -960:  # check if plane has reached left end of screen
        #        break
        
#
#def animation_screen(win, orientation, imgs):
#    scn_width, scn_height = win.size
#    
#    scn_width -= 300
#    scn_height -= 300
#    
#    if orientation == 'normal':
#        # Generate random x and y coordinates
#        x = np.linspace(0, 0.2 * np.pi, 10)
#        y = np.random.rand(10)
#
#        # Add some noise to the y coordinates
#        y += np.random.normal(scale=0.05, size=y.shape)
#
#        # Create the interpolation object
#        spline = make_interp_spline(x, y)
#
#        # Initialize PsychoPy window and image stimulus
#        image = visual.ImageStim(win, image=next(imgs), size=[120, 120])
#
#        # Set starting position of the plane
#        x_pos = -scn_width/2  # left edge of the screen
#        y_pos = spline(x.min()) * scn_height - scn_height/2
#        image.pos = [x_pos, y_pos]
#
#        # Loop through the spline points and move the image stimulus
#        for t in np.linspace(x.min(), x.max(), num=700):
#            x_pos = t * scn_width - scn_width/2
#            y_pos = spline(t) * scn_height - scn_height/2
#            image.pos = [x_pos, y_pos]
#            image.draw()
#            win.flip()
#            if x_pos > scn_width/2:  # check if image has reached right end of screen
#                break
#
#    elif orientation == 'reverse':
#        # Generate random x and y coordinates
#        x = np.linspace(0, 0.2 * np.pi, 10)
#        y = np.random.rand(10)
#
#        # Add some noise to the y coordinates
#        y += np.random.normal(scale=0.05, size=y.shape)
#
#        # Reverse the order of the x and y arrays
#        x = x[::-1]
#        y = y[::-1]
#
#        # Create the interpolation object
#        spline = make_interp_spline(x, y)
#
#        # Initialize PsychoPy window and image stimulus
#        image = visual.ImageStim(win, image=next(imgs), size=[120, 120])
#
#        # Set starting position of the plane
#        x_pos = scn_width/2  # right edge of the screen
#        y_pos = spline(x.max()) * scn_height - scn_height/2
#        image.pos = [x_pos, y_pos]
#
#        # Loop through the spline points and move the image stimulus
#        for t in np.linspace(x.min(), x.max(), num=700):
#            x_pos = scn_width/2 - (t * scn_width - scn_width/2)
#            y_pos = spline(t) * scn_height - scn_height/2
#            image.pos = [x_pos, y_pos]
#            image.draw()
#            win.flip()
#        #    if x_pos < -scn_width/2:  # check if image has reached left end of screen
#        #        break

        

file_name = '100'

# Prompt user to specify an EDF data filename
# before we open a fullscreen window
dlg_title = 'Enter Participant Data File Name'
dlg_prompt = 'Please enter a file name with 8 or fewer characters\n' + \
             '[letters, numbers, and underscore].'

# loop until we get a valid filename
while True:
    dlg = gui.Dlg(dlg_title)
    dlg.addText(dlg_prompt)
    dlg.addField('Participant ID:', file_name)
    # show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:  # if ok_data is not None
        print('Participant data filename: {}'.format(ok_data[0]))
    else:
        print('user cancelled')
        core.quit()
        sys.exit()

    # get the string entered by the experimenter
    tmp_str = dlg.data[0]
    # strip trailing characters, ignore the ".edf" extension
    file_name = tmp_str.rstrip().split('.')[0]

    # check if the filename is valid (length <= 8 & no special char)
    allowed_char = ascii_letters + digits + '_'
    if not all([c in allowed_char for c in file_name]):
        print('ERROR: Invalid Participant data filename')
    elif len(file_name) > 8:
        print('ERROR: Participant data filename should not exceed 8 characters')
    else:
        break

# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
    
# Prompt user to specify the condition number
dlg_title = 'Enter Condition Number'
dlg_prompt = 'Please enter the condition number (1 or 2).'

# Loop until we get a valid condition number
while True:
    dlg = gui.Dlg(dlg_title)
    dlg.addText(dlg_prompt)
    dlg.addField('Condition Number:', choices=['1', '2'])
    # Show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:  # If ok_data is not None
        CONDITION_NUM = int(ok_data[0])
        print('Condition Number: {}'.format(CONDITION_NUM))
        break
    else:
        print('User cancelled')
        core.quit()
        sys.exit()


# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = file_name + time_str

# create a folder for the current testing session in the "results" folder
session_folder = os.path.join(results_folder, session_identifier)
if not os.path.exists(session_folder):
    os.makedirs(session_folder)


orientation_list = ["normal","reverse"]

imgs_n = ["./images/sun.png","./images/balloon.png","./images/dog.png","./images/bird.png","./images/plane.png","./images/superhero.png"]
imgs_r = ["./images/sun.png","./images/balloon.png","./images/dog.png","./images/bird-inverse.png","./images/plane-inverse.png","./images/superhero-inverse.png"]

imgs_n = cycle(imgs_n)
imgs_r = cycle(imgs_r)


# Create a window to display the stimuli
win = visual.Window(fullscr=True, units='pix', color=(1, 1, 1))
# info screen
info = visual.TextStim(win, text='Press Space to Start Trial', pos=(0,-400), height=25, color='black')


# Create a list to store the data for each trial
trials_data = []

# Read in the conditions from the CSV file
conditions = pd.read_csv("./conditions/Sample_Conditions.csv").drop('Unnamed: 0',axis=1)
#CONDITION_NUM = 2 ## CHANGE THE CONDITION NUMBER TO TOGGLE BETWEEN THE TRIAL TYPE ( Current options 1 or 2 ) 
cond = conditions[conditions['Conditions']==CONDITION_NUM] 
cond = cond.reset_index(drop=True)
cond = cond.sample(frac=1) # sample rows and with replacement ( Shuffles all the samples ) 
trial_range = cond['Trials']# Trial range - 0 to 9
audio = cond['Audio']

# Read in the PRACTICE conditions from the CSV file
conditionsPractice = pd.read_csv("./practiceTrials/Conditions_Practice.csv").drop('Unnamed: 0',axis=1)
condPrac = conditionsPractice[conditionsPractice['Conditions']==CONDITION_NUM] 
condPrac = condPrac.reset_index(drop=True)
condPrac = condPrac.sample(frac=1) # sample rows and with replacement ( Shuffles all the samples ) 
trial_range_practice = condPrac['Trials']# Trial range - 0 to 9
audio_practice = condPrac['Audio']

checkpoint_flag = 0
iterator = 1

## Practice Trials 
def simulate_trial(win):
    
    #play map path first
    path = visual.ImageStim(win, image='./images/path.png',pos=(0,0))
    path.draw()
    win.flip()
    
    control_key = event.waitKeys(keyList=['space', 'escape'])

    #start practice 
    info = visual.TextStim(win, text='Press space bar to start the prictice trials', pos=(0,0), height=25, color='black')
    note = visual.TextStim(win, text='Which one did you see first?', pos=(0,-400), height=25, color='black')
    info.draw()
    win.flip()

    control_key = event.waitKeys(keyList=['space', 'escape'])

    if control_key[0] == 'space':
        
        for trialPrac, audioPrac in zip(trial_range_practice, audio_practice):
        
            # Create the stimuli
            doll = visual.ImageStim(win, image='./practiceTrials/images/Cookie-Monster-smaller.png',pos=(0,300))
            number = visual.TextStim(win, text=condPrac.loc[trialPrac, 'Target'], color='black', height=300, pos=(-10, 0) )
        
    
        
            # Audio Instantiation
            audio_Prac = sound.Sound(f"./practiceTrials/audio/{audioPrac}.wav") 
       
            # Target position 
            target_location = condPrac.loc[trialPrac,'Location']
            if condPrac.loc[trialPrac,'Location'] == 'left':
                left_number = visual.TextStim(win, text=condPrac.loc[trialPrac, 'Target'], color='black', height=250, pos=(-400, 0))
                right_number = visual.TextStim(win, text=condPrac.loc[trialPrac, 'Foil'], color='black', height=250, pos=(400, 0))
            else:
                left_number = visual.TextStim(win, text=condPrac.loc[trialPrac, 'Foil'], color='black', height=250, pos=(-400, 0))
                right_number = visual.TextStim(win, text=condPrac.loc[trialPrac, 'Target'], color='black', height=250, pos=(400, 0))

       
            # Display the doll
            doll.draw()
            info.draw()
            win.flip()

            # Wait for 3 seconds
            #time.sleep(3)
        
            control_key = event.waitKeys(keyList=['space'])

            if control_key[0] == 'space':
            
                #time.sleep(0.5) # Just to be ready

                # Display the target number
                number.draw()
                win.flip()
                
                # Play audio stimulus
                audio_Prac.play()
            
                # Wait for audio to finish playing
                core.wait(audio_Prac.getDuration())

                # Wait for 4 seconds
                time.sleep(4)

                # Animate the plane
                orientation = choice(orientation_list)
                if orientation == 'normal':
                    animation_screen(win, orientation, imgs_n)
                elif orientation == 'reverse':
                    animation_screen(win, orientation, imgs_r )


                # Display the number and foil
                left_number.draw()
                right_number.draw()
                win.flip()
       
          
                # Wait for a key press
                start_time = time.time()
                keys = event.waitKeys(keyList=['left', 'right','escape'])
                response_time = round((time.time()-start_time), 3)
                response_key = keys[0]
            
            
                # ACCURACY
                if response_key == target_location:
                    accuracy = 1
                else:
                    accuracy = 0


            # --- animation sequence from here, doesn't have any prevalence on the response time recording.

                # Animate the selected number
                if response_key == 'left':
                    selected_number = left_number
                elif response_key == 'right':
                    selected_number = right_number
                elif response_key == 'escape':
                    print('aborting')
                
                
                
                    Practice_trial_data = {
                    
                    'trial_id': trialPrac,
                    'condition': CONDITION_NUM,
                    'num_presentation_type': condPrac.loc[trialPrac, 'Number_type'],
                    'audio_presentation_context': condPrac.loc[trialPrac, 'Audio'],
                    'other_features': condPrac.loc[trialPrac, "Other_features"],
                    'target_number': condPrac.loc[trialPrac, 'Target'],
                    'foil': condPrac.loc[trialPrac, 'Foil'],
                    'response_key': response_key,
                    'response_time': response_time,
                    'accuracy': accuracy,
                                    }
                    Practice_trial_data.append(Practice_trial_data)
                    
                    break
                    

                start_pos = selected_number.pos
                end_pos = doll.pos

                start_time = time.time()
                while time.time() - start_time < 1.5:
                    pos = [start_pos[0] + (end_pos[0] - start_pos[0]) * (time.time() - start_time) / 1.5,
                            start_pos[1] + (end_pos[1] - start_pos[1]) * (time.time() - start_time) / 1.5]
                    selected_number.setPos(pos)

                    # Draw the doll and the selected number
                    doll.draw()
                    selected_number.draw()

                    # Flip the screen to update the display
                    win.flip()

            elif control_key[0] == 'escape':
                return None


    #     for _ in range(2):  # Repeat the block twice
    #         target_image = visual.ImageStim(win, image='./images/turtle.png', pos=(-10, 0))
    #         target_left_image = visual.ImageStim(win, image='./images/turtle.png', pos=(-400, 0))
    #         foil_left_image = visual.ImageStim(win, image='./images/elephant.png', pos=(400, 0))

    #         audio_folder = "./audio/turtle.wav"
    #         audio = sound.Sound(audio_folder)

    #         audio.play()

    #         target_image.draw()
    #         win.flip()

    #         time.sleep(1)
            
    #         win.flip()  # Display a blank screen

    #         time.sleep(5)  # Pause for 1 second

    #         target_left_image.draw()
    #         foil_left_image.draw()
    #         note.draw()
    #         win.flip()

    #         time.sleep(3)

    #         start_time = time.time()
    #         keys = event.waitKeys(keyList=['left', 'right', 'escape'])
    #         response_time = round((time.time() - start_time), 3)
    #         response_key = keys[0]

    #         if response_key == 'left':
    #             duration = 2.5
    #             frames_per_second = 60
    #             num_frames = int(duration * frames_per_second)
    #             pos_change = np.array((410, 0)) / num_frames

    #             for frame in range(num_frames):
    #                 target_left_image.pos += pos_change
    #                 target_left_image.draw()
    #                 foil_left_image.draw()
    #                 win.flip()
    # elif control_key[0] == 'escape':
    #     return None


simulate_trial(win)

path = visual.ImageStim(win, image='./images/path.png',pos=(0,0))
path.draw()
info.draw()
win.flip()

control_key = event.waitKeys(keyList=['space'])

if control_key[0] == 'space':
    
    for trial, audio in zip(trial_range, audio):
        
    

        # Create the stimuli
        doll = visual.ImageStim(win, image='./images/Cookie-Monster-smaller.png',pos=(0,300))
        number = visual.TextStim(win, text=cond.loc[trial, 'Target'], color='black', height=300, pos=(-10, 0) )
        
    
        
        # Audio Instantiation
        audio = sound.Sound(f"./audio/{audio}.wav") 
       
        # Target position 
        target_location = cond.loc[trial,'Location']
        if cond.loc[trial,'Location'] == 'left':
            left_number = visual.TextStim(win, text=cond.loc[trial, 'Target'], color='black', height=250, pos=(-400, 0))
            right_number = visual.TextStim(win, text=cond.loc[trial, 'Foil'], color='black', height=250, pos=(400, 0))
        else:
            left_number = visual.TextStim(win, text=cond.loc[trial, 'Foil'], color='black', height=250, pos=(-400, 0))
            right_number = visual.TextStim(win, text=cond.loc[trial, 'Target'], color='black', height=250, pos=(400, 0))

       
        # Display the doll
        doll.draw()
        info.draw()
        win.flip()

        # Wait for 3 seconds
        #time.sleep(3)
        
        control_key = event.waitKeys(keyList=['space'])

        if control_key[0] == 'space':
            
            #time.sleep(0.5) # Just to be ready

            # Display the target number
            number.draw()
            win.flip()
                
            # Play audio stimulus
            audio.play()
            
            # Wait for audio to finish playing
            core.wait(audio.getDuration())

            # Wait for 4 seconds
            time.sleep(4)

            # Animate the plane
            orientation = choice(orientation_list)
            if orientation == 'normal':
                animation_screen(win, orientation, imgs_n)
            elif orientation == 'reverse':
                animation_screen(win, orientation, imgs_r )


            # Display the number and foil
            left_number.draw()
            right_number.draw()
            win.flip()
       
                
                
                
            # Wait for a key press
            start_time = time.time()
            keys = event.waitKeys(keyList=['left', 'right','escape'])
            response_time = round((time.time()-start_time), 3)
            response_key = keys[0]
            
            
            # ACCURACY
            if response_key == target_location:
                accuracy = 1
            else:
                accuracy = 0


            # --- animation sequence from here, doesn't have any prevalence on the response time recording.

            # Animate the selected number
            if response_key == 'left':
                selected_number = left_number
            elif response_key == 'right':
                selected_number = right_number
            elif response_key == 'escape':
                print('aborting')
                
                
                
                trial_data = {
                
                'trial_id': trial,
                'condition': CONDITION_NUM,
                'num_presentation_type': cond.loc[trial, 'Number_type'],
                'audio_presentation_context': cond.loc[trial, 'Audio'],
                'other_features': cond.loc[trial, "Other_features"],
                'target_number': cond.loc[trial, 'Target'],
                'foil': cond.loc[trial, 'Foil'],
                'response_key': response_key,
                'response_time': response_time,
                'accuracy': accuracy,
                                }
                trials_data.append(trial_data)
                
                break
                

            start_pos = selected_number.pos
            end_pos = doll.pos

            start_time = time.time()
            while time.time() - start_time < 1.5:
                pos = [start_pos[0] + (end_pos[0] - start_pos[0]) * (time.time() - start_time) / 1.5,
                        start_pos[1] + (end_pos[1] - start_pos[1]) * (time.time() - start_time) / 1.5]
                selected_number.setPos(pos)

                # Draw the doll and the selected number
                doll.draw()
                selected_number.draw()

                # Flip the screen to update the display
                win.flip()

            # Record the trial data

            
            trial_data = {
            
            'trial_id': trial,
            'condition': CONDITION_NUM,
            'num_presentation_type': cond.loc[trial, 'Number_type'],
            'audio_presentation_context': cond.loc[trial, 'Audio'],
            'other_features': cond.loc[trial, "Other_features"],
            'target_number': cond.loc[trial, 'Target'],
            'accuracy': accuracy,
            'foil': cond.loc[trial, 'Foil'],
            'response_key': response_key,
            'response_time': response_time
                            }
            trials_data.append(trial_data)
            
            if  iterator % 6 == 0: # 4 Check points and 24 Trials, so 24/4 every Sixth Trial is a check point
                checkpoint_flag += 1 
                checkpoint = visual.ImageStim(win, image=f'./images/checkpoint{checkpoint_flag}.png', pos=(0,0))
                # Display the checkpoint image
                checkpoint.draw()
                win.flip()
                
                # Wait for 3 seconds
                time.sleep(3)
            
            iterator += 1  
           
        else:
            pass

end_message = visual.TextStim(win, text="Saving Data ...", color='black', height=20, pos=(0, 0))
end_message.draw()
win.flip()
time.sleep(2)

# Write the data to a CSV file
with open(f'{session_folder}/{file_name}_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['trial_id', 'condition','num_presentation_type','audio_presentation_context','other_features','target_number','accuracy','foil', 'response_key', 'response_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for trial_data in trials_data:
        writer.writerow(trial_data)
