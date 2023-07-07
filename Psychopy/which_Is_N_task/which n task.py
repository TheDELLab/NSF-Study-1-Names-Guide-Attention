from psychopy import visual, core, sound, event, gui, clock
import csv
import os

# Show dialog to input participant ID
participant_info = gui.Dlg(title="Participant Information")
participant_info.addField("Participant ID:")
participant_info.show()

if not participant_info.OK:
    core.quit()

participant_id = participant_info.data[0]

# create a window
win = visual.Window([1024, 768], color="white", units='pix')

# Initial screen
instruction_text = visual.TextStim(win, text="Press space bar to start the prictice trials", color="black")
instruction_text.draw()
win.flip()

# Wait for spacebar to continue
event.waitKeys(keyList=['space'])

# load the data from CSV file
data = []
with open("./which_is_N_numbers.csv", "r", encoding="utf-8-sig") as data_file:
    data_reader = csv.DictReader(data_file)
    column_names = data_reader.fieldnames
    column_names = [name.strip('\ufeff') for name in column_names]  # Remove the BOM character
    print("Column names:", column_names)  # Print the column names

    for row in data_reader:
        data.append(row)

# Print the data rows
for row in data:
    print(row)

# get the path to the audio folder
audio_folder = "./Which_is_N_wavs"

# create a loop to iterate through the data
results = []

for row in data:
    # extract the digits and location for each row
    target_digit = row["Target"]
    foil_digit = row["Foil"]
    location = row["Location"]
    audio_file = row["Audio"]

    # create stimuli for each round
    if location.lower() == "left":
        print(row["Location"])
        target_pos = (-200, 0)
        foil_pos = (200, 0)
        print(target_pos)
    elif location.lower() == "right":
        print(row["Location"])
        target_pos = (200, 0)
        foil_pos = (-200, 0)
        print(target_pos)

    else:
        # Handle cases where location is neither "left" nor "right"
        continue

    target_stim = visual.TextStim(win, text=target_digit, pos=target_pos, color="black", height=150)
    foil_stim = visual.TextStim(win, text=foil_digit, pos=foil_pos, color="black", height=150)
    audio_path = os.path.join(audio_folder, audio_file + ".wav")
    audio = sound.Sound(audio_path)

    # draw the stimuli and flip the window
    target_stim.draw()
    foil_stim.draw()
    win.flip()

    # play the audio
    audio.play()

    # start the response timer
    response_timer = clock.CountdownTimer()

    # wait for a key press
    keys = event.waitKeys(keyList=['left', 'right'], timeStamped=response_timer)

    # blank screen in between trails
    win.flip()
    core.wait(1.0)  # Adjust the duration as needed

    # wait for spacebar to continue
    event.waitKeys(keyList=['space'])

    # collect trial results
    trial_results = {
        "Target": target_digit,
        "Foil": foil_digit,
        "Location": location,
        "Audio": audio_file,
        "Response": keys[0][0],  # Get the key from the response
        "Response Time": round(keys[0][1], 3) if keys else None  # Get the response time to 3rd decimal place
    }
    results.append(trial_results)

# close the window
win.close()

# Create the results folder if it doesn't exist
results_folder = "results"
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# Save participant ID and responses
result_file = f"./results/{participant_id}_results.csv"
fieldnames = ["Target", "Foil", "Location", "Audio", "Response", "Response Time"]


with open(result_file, "w", newline="") as results_file:
    writer = csv.DictWriter(results_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# quit the experiment
core.quit()
