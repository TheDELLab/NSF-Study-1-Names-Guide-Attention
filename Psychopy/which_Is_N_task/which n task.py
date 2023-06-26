from psychopy import visual, core, sound, event
import csv
import os

# create a window
win = visual.Window([1024, 768], color="white", units='pix')

# load the data from CSV files
numbers_data = []
with open("./which_is_N_numbers.csv", "r") as numbers_file:
    numbers_reader = csv.reader(numbers_file)
    for row in numbers_reader:
        numbers_data.append(row)

# get the list of audio files from the folder
audio_folder = "./audioTEST"
audio_files = os.listdir(audio_folder)

# create a list to store the participant's responses
responses = []

# create a loop to iterate through the data
for i in range(len(numbers_data)):
    # extract the numbers for each round
    number1_data = numbers_data[i][0]
    number2_data = numbers_data[i][1]

    # create stimuli for each round
    number1 = visual.TextStim(win, text=number1_data, pos=(-200, 0), color="black")
    number2 = visual.TextStim(win, text=number2_data, pos=(200, 0), color="black")
    audio_file = os.path.join(audio_folder, audio_files[i])
    audio = sound.Sound(audio_file)

    # draw the stimuli and flip the window
    number1.draw()
    number2.draw()
    win.flip()

    # play the audio
    audio.play()

    # wait for a key press
    keys = event.waitKeys(keyList=['left', 'right'])

    # store the participant's response
    response = keys[0]
    responses.append(response)

    # save the response in the results folder
    result_row = numbers_data[i] + [response]
    result_file_path = os.path.join("results", "which_is_N_numbers_with_responses.csv")
    with open(result_file_path, "a", newline="") as result_file:
        result_writer = csv.writer(result_file)
        result_writer.writerow(result_row)

# close the window
win.close()

# quit the experiment
core.quit()
